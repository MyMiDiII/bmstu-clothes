import OpenGL.GL as gl
import numpy as np

from graphic.objects.object import Object
from clothes.mass import Mass


class Mesh(Object):
    def __init__(self, m, n):
        super().__init__()

        self.masses = []
        for i in range(m):
            for j in range(n):
                self.masses.append(Mass(1, (i, j, 0)))

        for i in range(m):
            for j in range(n):
                self.masses.append(Mass(1, (i, j, 5)))
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

        for i in range(m - 1):
            for j in range(n - 1):
                curInd = n * m + i * n + j 
                self.indices.extend([curInd, curInd + 1, curInd + n])
                self.indices.extend([curInd + n + 1, curInd + 1, curInd + n])

        self.indices = np.array(self.indices, dtype='int32')


    def update(self, dt):
        for mass in self.masses:
            mass.updateState(dt)

    def getVertexes(self):
        return np.array([mass.getPosition() for mass in self.masses],
                        dtype='float32')

    def getIndices(self):
        return self.indices
