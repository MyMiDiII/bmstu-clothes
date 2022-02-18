import OpenGL.GL as gl
import numpy as np
from random import uniform

from graphic.objects.object import Object
from clothes.mass import Mass
from clothes.spring import Spring
from clothes.pattern import TShirt

ZSTEP = 1 / 100
DIAG_COEF = 2 ** (1 / 2)


class MassSpringModel(Object):
    def __init__(self, pattern : TShirt):
        super().__init__()

        self.timer = 0

        self.gravity = 4
        self.mass = 0.01
        self.stiffness = 2
        self.damping = 0.2
        self.len0 = 0.05

        self.damp = 0.9

        self.masses = []
        self.indices = []
        self.springs = []

        index = 0
        front, back = pattern.getPatterns()
        n, m = front.shape

        for i in range(2, n - 2):
            for j in range(2, m - 2):
                if front[i][j]:
                    self.addMass(i, j, 0)
                    self.addTriangles(front, i, j)

        n, m = back.shape

        for i in range(2, n - 2):
            for j in range(2, m - 2):
                if back[i][j]:
                    self.addMass(i, j, -2)
                    self.addTriangles(back, i, j)

        self.indices = np.array(self.indices, dtype='int32')

        for i in range(2, n - 2):
            for j in range(2, m - 2):
                if front[i][j]:
                    self.addStructSprings(front, i, j)
                    self.addShearSprings(front, i, j)
                    self.addBendingSprings(front, i, j)

                if back[i][j]:
                    self.addStructSprings(back, i, j)
                    self.addShearSprings(back, i, j)
                    self.addBendingSprings(back, i, j)


    def addStructSprings(self, grid, i, j):
        ind = grid[i][j]
        indexes = [
                grid[i - 1][j],
                grid[i][j - 1],
                grid[i][j + 1],
                grid[i + 1][j]
            ]

        for nearInd in indexes:
            if nearInd:
                self.masses[ind - 1].addSpring(
                        self.masses[nearInd - 1],
                        self.len0,
                        self.stiffness,
                        0
                        )


    def addShearSprings(self, grid, i, j):
        ind = grid[i][j]
        indexes = [
                grid[i - 1][j - 1],
                grid[i - 1][j + 1],
                grid[i + 1][j - 1],
                grid[i + 1][j + 1]
            ]

        for nearInd in indexes:
            if nearInd:
                self.masses[ind - 1].addSpring(
                        self.masses[nearInd - 1],
                        DIAG_COEF * self.len0,
                        self.stiffness,
                        1
                        )


    def addBendingSprings(self, grid, i, j):
        ind = grid[i][j]
        indexes = [
                grid[i - 2][j],
                grid[i][j - 2],
                grid[i][j - 2],
                grid[i + 2][j]
            ]

        for nearInd in indexes:
            if nearInd:
                self.masses[ind - 1].addSpring(
                        self.masses[nearInd - 1],
                        2 * self.damp * self.len0,
                        self.stiffness,
                        2
                        )


    def addMass(self, i, j, z):
        self.masses.append(
            Mass(
                self.mass,
                (z + j * self.len0, -i * self.len0, uniform(-ZSTEP, ZSTEP)),
                i == 2
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
        for mass in self.masses:
            for spring in mass.getSprings():
                if spring.type != 2:
                    spring.stabilize()


    def update(self, dt):
        for mass in self.masses:
            mass.updateState(dt, self.gravity, self.damping)

        self.__keepStable()


    def getVertexes(self):
        return np.array([mass.getPosition() for mass in self.masses],
                        dtype='float32')


    def getIndices(self):
        return self.indices

