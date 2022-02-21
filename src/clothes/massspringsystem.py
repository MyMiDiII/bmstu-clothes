import OpenGL.GL as gl
import glm
import numpy as np
from random import uniform

from graphic.objects.object import Object
from clothes.mass import Mass
from clothes.spring import Spring, SpringType
from clothes.pattern import TShirt

ZSTEP = 1 / 100

class MassSpringModel(Object):
    def __init__(self, pattern : TShirt):
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
        front, back, seams, triag = pattern.getPatterns()
        self.indices.extend(triag)

        n, m = front.shape

        for i in range(n):
            for j in range(m):
                if front[i][j]:
                    self.addMass(i, j, (0, 0, 0.15 if i != 2 else 0.1), 0)
                    self.addTriangles(front, i, j)

        for i in range(n):
            for j in range(m):
                if back[i][j]:
                    self.addMass(i, j, (0, 0, -0.15 if i != 2 else -0.1), 1)
                    self.addTriangles(back, i, j)

        for i in range(n):
            for j in range(m):
                if front[i][j]:
                    self.addSprings(front, i, j, SpringType.struct)
                    self.addSprings(front, i, j, SpringType.shear)
                    self.addSprings(front, i, j, SpringType.bend)

                if back[i][j]:
                    self.addSprings(back, i, j, SpringType.struct)
                    self.addSprings(back, i, j, SpringType.shear)
                    self.addSprings(back, i, j, SpringType.bend)

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


    def addMass(self, i, j, move, plus):
        self.masses.append(
            Mass(
                self.mass,
                #(move[0] + j * self.len0, move[1] - i * self.len0,
                #    move[2] + uniform(-ZSTEP, ZSTEP)),
                (move[0] + j * self.len0, move[1] - i * self.len0,
                    move[2] + 0),
                #(move[0] + j * self.len0, move[1], move[2] + i * self.len0),
                #True
                False
                #(i == 2 + plus or i == 4 + plus)
                #(j * self.len0, 0, -i * self.len0),
                #(i == 2 and j == 2 or i == 2 and j == 6)
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
        for i, mass in enumerate(self.masses):
            mass.updateState(dt, self.gravity, self.damping, self.wind)

        for i, mass in enumerate(self.masses):
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

