import numpy as np

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
        arr = TSHIRT_FRONT

        n, m = arr.shape
        for i in range(n):
            for j in range(m):
                if arr[i][j]:
                    arr[i][j] = self.index
                    self.index += 1

        return arr

    def getBack(self):
        arr = TSHIRT_BACK

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

        dirs = ["up", "left", "right", "down"]

        seams = dict()
        for i in range(n):
            for j in range(m):
                if TSHIRT_SEAMS[i][j]:
                    curDir = "up" if i == 2 else (
                                 "down" if i == 7 else (
                                     "left" if j == 5 or j == 6 else "right"
                                 )
                             )
                    seams[back[i][j]] = (front[i][j], curDir)

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
        return front, back, seams
