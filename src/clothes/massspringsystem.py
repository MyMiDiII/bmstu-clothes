import OpenGL.GL as gl
import numpy as np
from random import uniform

from graphic.objects.object import Object
from clothes.mass import Mass
from clothes.spring import Spring


class MassSpringModel(Object):
    def __init__(self, m, n):
        super().__init__()

        self.timer = 0

        self.gravity = 9.81
        self.mass = 0.01
        self.stiffness = 1
        self.damping = 1
        self.len0 = 0.05

        self.damp = 0.8

        self.masses = []
        self.springs = []

        for i in range(m):
            for j in range(n):
                self.masses.append(Mass(self.mass, (i * self.len0, j * self.len0, uniform(-1 /
                    100, 1 / 100)),
                        j == n - 1 and (not i or i == m - 1)))

        for i in range(m):
            for j in range(n):
                # !!!
                if i != m - 1:
                    self.masses[i * n + j].addSpring(
                            self.masses[(i + 1) * n + j],
                            self.len0,
                            self.stiffness,
                            0
                            )
                # !!!
                if j != n - 1:
                    self.masses[i * n + j].addSpring(
                            self.masses[i * n + j + 1],
                            self.len0,
                            self.stiffness,
                            0
                            )

                # !!!
                if i != m - 1 and j:
                    self.masses[i * n + j].addSpring(
                            self.masses[(i + 1) * n + j - 1],
                            self.len0 * 2 ** 0.5,
                            self.stiffness,
                            1
                            )

                # !!!
                if i != m - 1 and j != n - 1:
                    self.masses[i * n + j].addSpring(
                            self.masses[(i + 1) * n + j + 1],
                            self.len0 * 2 ** 0.5,
                            self.stiffness,
                            1
                            )


                # !!!
                if i < m - 2:
                    self.masses[i * n + j].addSpring(
                            self.masses[(i + 2) * n + j],
                            self.damp * self.len0 * 2,
                            self.stiffness,
                            2
                            )

                # !!!
                if j < n - 2:
                    self.masses[i * n + j].addSpring(
                            self.masses[i * n + j + 2],
                            self.damp * self.len0 * 2,
                            self.stiffness,
                            2
                            )

                if i:
                    self.masses[i * n + j].addSpring(
                            self.masses[(i - 1) * n + j],
                            self.len0,
                            self.stiffness,
                            0
                            )

                if j:
                    self.masses[i * n + j].addSpring(
                            self.masses[i * n + j - 1],
                            self.len0,
                            self.stiffness,
                            0
                            )


                if i and j:
                    self.masses[i * n + j].addSpring(
                            self.masses[(i - 1) * n + j - 1],
                            self.len0 * 2 ** 0.5,
                            self.stiffness,
                            1
                            )

                if i and j != n - 1:
                    self.masses[i * n + j].addSpring(
                            self.masses[(i - 1) * n + j + 1],
                            self.len0 * 2 ** 0.5,
                            self.stiffness,
                            1
                            )
                if i > 1:
                    self.masses[i * n + j].addSpring(
                            self.masses[(i - 2) * n + j],
                            self.damp * self.len0 * 2,
                            self.stiffness,
                            2
                            )

                if j > 1:
                    self.masses[i * n + j].addSpring(
                            self.masses[i * n + j - 2],
                            self.damp * self.len0 * 2,
                            self.stiffness,
                            2
                           )

                #curIndex = i * n + j 

                #if i:
                #    curSpring = Spring(
                #                    self.masses[curIndex],
                #                    self.masses[curIndex - n],
                #                    self.damp * self.len0,
                #                    self.stiffness
                #                )
                #    self.masses[curIndex].addSpring(curSpring)
                #    self.springs.append(curSpring)

                #if i != m - 1:
                #    curSpring = Spring(
                #                    self.masses[curIndex],
                #                    self.masses[curIndex + n],
                #                    self.damp * self.len0,
                #                    self.stiffness
                #                )
                #    self.masses[curIndex].addSpring(curSpring)
                #    self.springs.append(curSpring)

                #if j:
                #    curSpring = Spring(
                #                    self.masses[curIndex],
                #                    self.masses[curIndex - 1],
                #                    self.damp * self.len0,
                #                    self.stiffness
                #                )
                #    self.masses[curIndex].addSpring(curSpring)
                #    self.springs.append(curSpring)

                #if j != n - 1:
                #    curSpring = Spring(
                #                    self.masses[curIndex],
                #                    self.masses[curIndex + 1],
                #                    self.damp * self.len0,
                #                    self.stiffness
                #                )
                #    self.masses[curIndex].addSpring(curSpring)
                #    self.springs.append(curSpring)

                #if i and j:
                #    curSpring = Spring(
                #                    self.masses[curIndex],
                #                    self.masses[curIndex - n - 1],
                #                    self.damp * self.len0 * 2 ** 0.5,
                #                    self.stiffness
                #                )
                #    self.masses[curIndex].addSpring(curSpring)
                #    self.springs.append(curSpring)

                #if i and j != n - 1:
                #    curSpring = Spring(
                #                    self.masses[curIndex],
                #                    self.masses[curIndex - n + 1],
                #                    self.damp * self.len0 * 2 ** 0.5,
                #                    self.stiffness
                #                )
                #    self.masses[curIndex].addSpring(curSpring)
                #    self.springs.append(curSpring)

                #if i != m - 1 and j:
                #    curSpring = Spring(
                #                    self.masses[curIndex],
                #                    self.masses[curIndex + n - 1],
                #                    self.damp * self.len0 * 2 ** 0.5,
                #                    self.stiffness
                #                )
                #    self.masses[curIndex].addSpring(curSpring)
                #    self.springs.append(curSpring)

                #if i != m - 1 and j != n - 1:
                #    curSpring = Spring(
                #                    self.masses[curIndex],
                #                    self.masses[curIndex + n + 1],
                #                    self.damp * self.len0 * 2 ** 0.5,
                #                    self.stiffness
                #                )
                #    self.masses[curIndex].addSpring(curSpring)
                #    self.springs.append(curSpring)

                #if i > 1:
                #    curSpring = Spring(
                #                    self.masses[curIndex],
                #                    self.masses[curIndex - 2 * n],
                #                    self.damp * self.len0 * 2,
                #                    self.stiffness
                #                )
                #    self.masses[curIndex].addSpring(curSpring)
                #    self.springs.append(curSpring)

                #if i < m - 2:
                #    curSpring = Spring(
                #                    self.masses[curIndex],
                #                    self.masses[curIndex + 2 * n],
                #                    self.damp * self.len0 * 2,
                #                    self.stiffness
                #                )
                #    self.masses[curIndex].addSpring(curSpring)
                #    self.springs.append(curSpring)

                #if j > 1:
                #    curSpring = Spring(
                #                    self.masses[curIndex],
                #                    self.masses[curIndex - 2],
                #                    self.damp * self.len0 * 2,
                #                    self.stiffness
                #                )
                #    self.masses[curIndex].addSpring(curSpring)
                #    self.springs.append(curSpring)

                #if j < n - 2:
                #    curSpring = Spring(
                #                    self.masses[curIndex],
                #                    self.masses[curIndex + 2],
                #                    self.damp * self.len0 * 2,
                #                    self.stiffness
                #                )
                #    self.masses[curIndex].addSpring(curSpring)
                #    self.springs.append(curSpring)


        #for i in range(m):
        #    for j in range(n):
        #        curInd = i * n + j 
        #       # print(len(self.masses[curInd].springs))


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
                self.indices.extend([curInd, curInd + 1, curInd + n + 1])
                self.indices.extend([curInd, curInd + n, curInd + n + 1])

        #for i in range(m - 1):
        #    for j in range(n - 1):
        #        curInd = n * m + i * n + j 
        #        self.indices.extend([curInd, curInd + 1, curInd + n])
        #        self.indices.extend([curInd + n + 1, curInd + 1, curInd + n])

        self.indices = np.array(self.indices, dtype='int32')

    def __keepStable(self):
        for mass in self.masses:
            for spring in mass.getSprings():
                if spring.type != 2:
                    spring.stabilize()


    def update(self, dt):
        #print("update")
        for mass in self.masses:
            mass.updateState(dt, self.gravity, self.damping)

        for _ in range(2):
            self.__keepStable()


    def getVertexes(self):
        return np.array([mass.getPosition() for mass in self.masses],
                        dtype='float32')


    def getIndices(self):
        return self.indices
