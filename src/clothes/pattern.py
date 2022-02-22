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
                                (j - k + 3) // 2 % 4,
                                types[abs(j - k)]
                                ])
                            seams.append([
                                back[i][k],
                                front[i][j],
                                (j - k + 3) // 2 % 4,
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

                if TSHIRT_SEAMS[i][j] == 5:
                    for k in range(j - 1, j + 2):
                        if back[i][k]:
                            seams.append([
                                front[i][j],
                                back[i][k],
                                (k - j + 7) // 2 % 4,
                                types[abs(j - k)]
                                ])
                            seams.append([
                                back[i][k],
                                front[i][j],
                                (k - j + 7) // 2 % 4,
                                types[abs(j - k)]
                                ])

                    if front[i][j + 1]:
                        triangles.extend([
                            back[i][j] - 1,
                            front[i][j + 1] - 1,
                            front[i][j] - 1
                            ])

                    if back[i][j + 1] and front[i][j + 1]:
                        triangles.extend([
                            back[i][j] - 1,
                            back[i][j + 1] - 1,
                            front[i][j + 1] - 1
                            ])


                if TSHIRT_SEAMS[i][j] == 3:
                    for k in range(i - 1, i + 2):
                        if back[k][j]:
                            seams.append([
                                front[i][j],
                                back[k][j],
                                (k - i + 5) // 2 % 4,
                                types[abs(i - k)]
                                ])
                            seams.append([
                                back[k][j],
                                front[i][j],
                                (k - i + 5) // 2 % 4,
                                types[abs(i - k)]
                                ])

                    if back[i + 1][j]:
                        triangles.extend([
                            front[i][j] - 1,
                            back[i][j] - 1,
                            back[i + 1][j] - 1,
                            ])

                    if back[i + 1][j] and front[i + 1][j]:
                        triangles.extend([
                            front[i][j] - 1,
                            back[i + 1][j] - 1,
                            front[i + 1][j] - 1
                            ])

                if TSHIRT_SEAMS[i][j] == 7:
                    for k in range(i - 1, i + 2):
                        if back[k][j]:
                            seams.append([
                                front[i][j],
                                back[k][j],
                                (k - i + 9) // 2 % 4,
                                types[abs(i - k)]
                                ])
                            seams.append([
                                back[k][j],
                                front[i][j],
                                (k - i + 9) // 2 % 4,
                                types[abs(i - k)]
                                ])

                    if back[i + 1][j]:
                        triangles.extend([
                            front[i][j] - 1,
                            back[i][j] - 1,
                            back[i + 1][j] - 1,
                            ])

                    if back[i + 1][j] and front[i + 1][j]:
                        triangles.extend([
                            front[i][j] - 1,
                            back[i + 1][j] - 1,
                            front[i + 1][j] - 1
                            ])

                if TSHIRT_SEAMS[i][j] == 4:
                    for k in range(-1, 2):
                        if back[i + k][j + k]:
                            seams.append([
                                front[i][j],
                                back[i + k][j + k],
                                0,
                                types[abs(k)]
                                ])
                            seams.append([
                                back[i + k][j + k],
                                front[i][j],
                                0,
                                types[abs(k)]
                                ])

                    triangles.extend([
                        front[i - 1][j + 1] - 1,
                        back[i - 1][j + 1] - 1,
                        back[i][j] - 1
                        ])

                    triangles.extend([
                        front[i - 1][j + 1] - 1,
                        back[i][j] - 1,
                        front[i][j] - 1
                        ])

                    triangles.extend([
                        front[i][j] - 1,
                        back[i][j] - 1,
                        back[i + 1][j - 1] - 1
                        ])

                    triangles.extend([
                        front[i][j] - 1,
                        back[i + 1][j - 1] - 1,
                        front[i + 1][j - 1] - 1
                        ])

                if TSHIRT_SEAMS[i][j] == 6:
                    for k in range(-1, 2):
                        if back[i + k][j + k]:
                            seams.append([
                                front[i][j],
                                back[i + k][j + k],
                                0,
                                types[abs(k)]
                                ])
                            seams.append([
                                back[i + k][j + k],
                                front[i][j],
                                0,
                                types[abs(k)]
                                ])

                    triangles.extend([
                        back[i - 1][j - 1] - 1,
                        front[i - 1][j - 1] - 1,
                        front[i][j] - 1,
                        ])

                    triangles.extend([
                        back[i - 1][j - 1] - 1,
                        front[i][j] - 1,
                        back[i][j] - 1
                        ])

                    triangles.extend([
                        back[i][j] - 1,
                        front[i][j] - 1,
                        front[i + 1][j + 1] - 1
                        ])

                    triangles.extend([
                        back[i][j] - 1,
                        front[i + 1][j + 1] - 1,
                        back[i + 1][j + 1] - 1
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

        k = 66
        arr = np.array([[0] * (k + 4), [0] * (k + 4)] + [[0] * 2 + [1] * k + [0]
            * 2 for _ in range(k)] + [[0] * (k + 4), [0] * (k + 4)])
        print(arr)
        #arr = np.array([[0] * (k + 2), [0] * (k + 2)] + [[[0] * 2 + [1] * k + [0]
        #    * 2] for _ in range(k)] + [[0] * (k + 2), [0] * (k + 2)])
        #print(arr)
        #arr = np.array(
        #        [[0, 0, 0, 0, 0, 0],
        #        [0, 0, 0, 0, 0, 0],
        #        [0, 0, 1, 1, 0, 0],
        #        [0, 0, 1, 1, 0, 0],
        #        [0, 0, 0, 0, 0, 0],
        #        [0, 0, 0, 0, 0, 0]]
        #        )

        self.index = 0
        n, m = arr.shape
        for i in range(n):
            for j in range(m):
                if arr[i][j]:
                    arr[i][j] = self.index
                    self.index += 1

        return arr
        #return front, back, seams, triangles

    #def getPatterns(self):
    #    front = self.getFront()
    #    back = self.getBack()
    #    n, m = TSHIRT_SEAMS.shape

    #    seams = []
    #    for i in range(n):
    #        for j in range(m):
    #            if TSHIRT_SEAMS[i][j]:
    #                if i == 2:
    #                    front[i - 1][j] = back[i][j]
    #                    back[i - 1][j] = front[i][j]

    #                if i == 8 and j in [2, 3, 4, 28, 29, 30]:
    #                    front[i + 1][j] = back[i][j]
    #                    back[i + 1][j] = front[i][j]

    #                if i == 9 and j == 5:
    #                    front[i + 1][j - 1] = back[i][j]
    #                    back[i + 1][j - 1] = front[i][j]

    #                if i > 9 and j == 6:
    #                    front[i][j - 1] = back[i][j]
    #                    back[i][j - 1] = front[i][j]

    #    return front, TSHIRT_FRONT, back, TSHIRT_BACK
