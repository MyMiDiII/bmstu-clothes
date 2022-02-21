import numpy as np
from copy import deepcopy

from clothes.templates import *
from clothes.spring import SpringType

class Pattern:

    def __init__(self, matrix=np.zeros((1, 1))):
        self.matrix = matrix

class TShirt:

    def __init__(self, length=65, width=25, sleeve=(10, 15), neck=10):
        self.len0 = 5
        self.length = length
        self.width = width
        self.sleeveLength = sleeve[0]
        self.sleeveWidth  = sleeve[1]
        self.neck = neck

        self.index = 1


    def getFront(self):
        arr = deepcopy(TSHIRT_FRONT)

        n, m = arr.shape
        for i in range(n):
            for j in range(m):
                if arr[i][j]:
                    arr[i][j] = self.index
                    self.index += 1

        return arr

    def getBack(self):
        arr = deepcopy(TSHIRT_BACK)

        n, m = arr.shape
        for i in range(n):
            for j in range(m):
                if arr[i][j]:
                    arr[i][j] = self.index
                    self.index += 1

        print('max ind', self.index)

        return arr


    def getPatterns(self):
        front = self.getFront()
        back = self.getBack()
        n, m = TSHIRT_SEAMS.shape

        types = [SpringType.struct, SpringType.shear]

        seams = []
        triangles = []
        for i in range(n):
            for j in range(m):
                if TSHIRT_SEAMS[i][j] == 1:
                    for k in range(j - 1, j + 2):
                        if back[i][k]:
                            seams.append([
                                front[i][j],
                                back[i][k],
                                j - k + 2,
                                types[abs(j - k)]
                                ])
                            seams.append([
                                back[i][k],
                                front[i][j],
                                j - k + 2,
                                types[abs(j - k)]
                                ])

                    if back[i][j] and front[i][j + 1]:
                        triangles.extend([
                            back[i][j] - 1,
                            front[i][j + 1] - 1,
                            front[i][j] - 1
                            ])

                    if back[i][j] and back[i][j + 1] and front[i][j + 1]:
                        triangles.extend([
                            back[i][j] - 1,
                            back[i][j + 1] - 1,
                            front[i][j + 1] - 1
                            ])


        #arr = np.array(
        #        [[0, 0, 0, 0, 0, 0, 0, 0, 0],
        #        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        #        [0, 0, 1, 1, 1, 1, 1, 0, 0],
        #        [0, 0, 1, 1, 1, 1, 1, 0, 0],
        #        [0, 0, 1, 1, 1, 1, 1, 0, 0],
        #        [0, 0, 1, 1, 1, 1, 1, 0, 0],
        #        [0, 0, 1, 1, 1, 1, 1, 0, 0],
        #        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        #        [0, 0, 0, 0, 0, 0, 0, 0, 0]]
        #        )

        #arr = np.array(
        #        [[0, 0, 0, 0, 0, 0],
        #        [0, 0, 0, 0, 0, 0],
        #        [0, 0, 1, 1, 0, 0],
        #        [0, 0, 1, 1, 0, 0],
        #        [0, 0, 0, 0, 0, 0],
        #        [0, 0, 0, 0, 0, 0]]
        #        )

        #n, m = arr.shape
        #for i in range(n):
        #    for j in range(m):
        #        if arr[i][j]:
        #            arr[i][j] = self.index
        #            self.index += 1

        #return arr
        return front, back, seams, triangles
