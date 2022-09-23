import OpenGL.GL as gl
import glm
import numpy as np
from random import uniform
from math import pi, cos, sin

from graphic.objects.object import Object
from clothes.mass import Mass
from clothes.spring import Spring, SpringType
from clothes.pattern import Pattern

ZSTEP = 1 / 100

class MassSpringModel(Object):
    def __init__(self, pattern : Pattern):
        super().__init__()

        self.timer = 0

        self.gravity = 9.81
        self.wind = True
        self.mass = 0.01
        self.striffness = 1
        self.damping = 0.1
        self.len0 = 0.05

        self.masses = []
        self.indices = []
        self.springs = []

        index = 0
        parts, seams, triag, fixCond = pattern.getPatterns()
        self.indices.extend(triag)


        for part in parts:
            n, m = part[0].shape

            for i in range(n):
                for j in range(m):
                    if part[0][i][j]:
                        self.addMass(i, j, (-(n - 1) / 2 * self.len0,
                                            0,
                                            self.len0 / 2), part[1], fixCond)
                        self.addTriangles(part[0], i, j)

        for part in parts:
            n, m = part[0].shape

            for i in range(n):
                for j in range(m):
                    if part[0][i][j]:
                        self.addSprings(part[0], i, j, SpringType.struct)
                        self.addSprings(part[0], i, j, SpringType.shear)
                        self.addSprings(part[0], i, j, SpringType.bend)

        for seam in seams:
            self.addSpring(*seam)

        self.indices = np.array(self.indices, dtype="int32")


    def addSpring(self, ind1, ind2, orderInd, springType):
        self.masses[ind1 - 1].addSpring(
                self.masses[ind2 - 1],
                self.len0,
                self.striffness,
                orderInd,
                springType
                )


    def addSprings(self, grid, i, j, springType):
        ind = grid[i][j]
        spPos = [(i + k, j + l) for k, l in springType.value["which"]]
        indices = [grid[x][y] for x, y in spPos]

        for orderInd, nearInd in enumerate(indices):
            if nearInd:
                self.addSpring(ind, nearInd, orderInd, springType)


    def addMass(self, i, j, move, plus, cond):
        x = move[0] + j * self.len0
        y = move[1] - (i - 4) * self.len0
        z = plus * move[2] + uniform(-ZSTEP, ZSTEP)

        R = self.len0
        if cond(i, j):
            y = R * cos(pi / 14 + (i - 2) * pi / 7) - abs(x / 10)
            z = plus * R * sin(pi / 14 + (i - 2) * pi / 7)

        self.masses.append(
            Mass(
                self.mass,
                (x, y, z),
                cond(i, j)
            )
        )


    def addTriangles(self, grid, i, j):
        n, m = grid.shape

        if grid[i + 1][j + 1]:
            if grid[i + 1][j]:
                self.indices.extend([grid[i][j] - 1,
                                     grid[i + 1][j + 1] - 1,
                                     grid[i + 1][j] - 1])

            if grid[i][j + 1]:
                self.indices.extend([grid[i][j] - 1,
                                     grid[i][j + 1] - 1,
                                     grid[i + 1][j + 1] - 1])

        elif grid[i][j + 1] and grid[i + 1][j]:
            self.indices.extend([grid[i][j] - 1,
                                 grid[i + 1][j] - 1,
                                 grid[i][j + 1] - 1])

        if not grid[i][j - 1] and grid[i + 1][j - 1]:
            self.indices.extend([grid[i][j] - 1,
                                 grid[i + 1][j - 1] - 1,
                                 grid[i + 1][j] - 1])


    def __keepStable(self):
        for mass in reversed(self.masses):
            for spring in mass.getSprings():
                    spring.stabilize()


    def update(self, dt):
        for mass in self.masses:
            mass.updateState(dt, self.gravity, self.damping, self.wind)

        for mass in self.masses:
            mass.updateNormal()

        for _ in range(2):
            self.__keepStable()


    def getVertexes(self):
        return np.array([mass.getPosition() + mass.getNegNormal()
                         for mass in self.masses],
                        dtype='float32')


    def getIndices(self):
        return self.indices


    def setWind(self, how):
        self.wind = how


    def setStif(self, val):
        self.striffness = val

        for mass in self.masses:
            for sp in mass.getSprings():
                sp.setStif(val)


    def setMass(self, val):
        self.mass = val

        for mass in self.masses:
            mass.setMass(val)


    def setGrav(self, val):
        self.gravity = val

