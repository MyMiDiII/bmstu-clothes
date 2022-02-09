import OpenGL.GL as gl
import numpy as np

from graphic.objects.object import Object
from clothes.mass import Mass
from clothes.spring import Spring


class Mesh(Object):
    def __init__(self, m, n):
        super().__init__()

        k = 50
        len0 = 0.5

        self.masses = []
        for i in range(m):
            for j in range(n):
                self.masses.append(Mass(0.1, (i / 2, 0, j / 2),
                        j == n - 1 and (not i or i == m - 1)))

        for i in range(m):
            for j in range(n):
                if i:
                    self.masses[i * n + j].addSpring(
                            self.masses[(i - 1) * n + j],
                            0.9 * len0,
                            k
                            )

                if i != m - 1:
                    self.masses[i * n + j].addSpring(
                            self.masses[(i + 1) * n + j],
                            0.9 * len0,
                            k
                            )

                if j:
                    self.masses[i * n + j].addSpring(
                            self.masses[i * n + j - 1],
                            0.9 * len0,
                            k
                            )

                if j != n - 1:
                    self.masses[i * n + j].addSpring(
                            self.masses[i * n + j + 1],
                            0.9 * len0,
                            k
                            )

                if i and j:
                    self.masses[i * n + j].addSpring(
                            self.masses[(i - 1) * n + j - 1],
                            0.9 * len0 * 2 ** 0.5,
                            k
                            )

                if i and j != n - 1:
                    self.masses[i * n + j].addSpring(
                            self.masses[(i - 1) * n + j + 1],
                            0.9 * len0 * 2 ** 0.5,
                            k
                            )

                if i != m - 1 and j:
                    self.masses[i * n + j].addSpring(
                            self.masses[(i + 1) * n + j - 1],
                            0.9 * len0 * 2 ** 0.5,
                            k
                            )

                if i != m - 1 and j != n - 1:
                    self.masses[i * n + j].addSpring(
                            self.masses[(i + 1) * n + j + 1],
                            0.9 * len0 * 2 ** 0.5,
                            k
                            )

                if i > 1:
                    self.masses[i * n + j].addSpring(
                            self.masses[(i - 2) * n + j],
                            0.9 * len0 * 1.9,
                            k
                            )

                if i < m - 2:
                    self.masses[i * n + j].addSpring(
                            self.masses[(i + 2) * n + j],
                            0.9 * len0 * 1.9,
                            k
                            )

                if j > 1:
                    self.masses[i * n + j].addSpring(
                            self.masses[i * n + j - 2],
                            0.9 * len0 * 1.9,
                            k
                            )

                if j < n - 2:
                    self.masses[i * n + j].addSpring(
                            self.masses[i * n + j + 2],
                            0.9 * len0 * 1.9,
                            k
                            )

        for i in range(m):
            for j in range(n):
                print(len(self.masses[i * n + j].springs))


        #for i in range(m):
        #    for j in range(n):
        #        self.masses.append(Mass(1, (i, j, 5)))
       # self.masses = [
       #         Mass(1, (-0.5, -0.5, 0)),
       #         Mass(1, ( 0.5, -0.5, 0)),
       #         Mass(1, ( 0.5,  0.5, 0)),
       #         Mass(1, (-0.5,  0.5, 0)),
       #         ]

        self.indices = []
        for i in range(m - 1):
            for j in range(n - 1):
                curInd = i * n + j 
                self.indices.extend([curInd, curInd + 1, curInd + n])
                self.indices.extend([curInd + n + 1, curInd + 1, curInd + n])

        #for i in range(m - 1):
        #    for j in range(n - 1):
        #        curInd = n * m + i * n + j 
        #        self.indices.extend([curInd, curInd + 1, curInd + n])
        #        self.indices.extend([curInd + n + 1, curInd + 1, curInd + n])

        self.indices = np.array(self.indices, dtype='int32')


    def update(self, dt):
        for mass in self.masses:
            mass.updateState(dt)

    def getVertexes(self):
        return np.array([mass.getPosition() for mass in self.masses],
                        dtype='float32')

    def getIndices(self):
        return self.indices
