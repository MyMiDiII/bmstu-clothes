import numpy as np
from copy import deepcopy

from clothes.templates import *

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

        seams = []
        for i in range(n):
            for j in range(m):
                if TSHIRT_SEAMS[i][j]:
                    if i == 2:
                        front[i - 1][j] = back[i][j]
                        back[i - 1][j] = front[i][j]

                    if i == 8 and j in [2, 3, 4, 28, 29, 30]:
                        front[i + 1][j] = back[i][j]
                        back[i + 1][j] = front[i][j]

                    if i == 9 and j == 5:
                        front[i + 1][j - 1] = back[i][j]
                        back[i + 1][j - 1] = front[i][j]

                    if i > 9 and j == 6:
                        front[i][j - 1] = back[i][j]
                        back[i][j - 1] = front[i][j]
                        



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
        return front, TSHIRT_FRONT, back, TSHIRT_BACK
