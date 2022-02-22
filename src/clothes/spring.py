import glm

import enum
DIAG_COEF = 2 ** (1 / 2)

class SpringType(enum.Enum):
    struct = {
            "lenCoef" : 1,
            "k" : 1,
            "which" : [(-1, 0), (0, 1), (1, 0), (0, -1)],
            "indexes" : [2, 4, 6, 8]
        }
    shear = {
            "lenCoef" : DIAG_COEF,
            "k" : 2,
            "which" : [(-1, -1), (-1, 1), (1, 1), (1, -1)],
            "indexes" : [1, 3, 5, 7]
        }
    bend = {
            "lenCoef" : 2 * 0.8,
            "k" : 2,
            "which" : [(-2, 0), (0, 2), (2, 0), (0, -2)],
            "indexes" : [100] * 4
        }


class Spring:

    def __init__(self, massFrom, massTo, len0, k, index, springType : SpringType):
        self.massFrom = massFrom
        self.massTo   = massTo
        self.len0     = len0 * springType.value["lenCoef"]
        self.k        = k * springType.value["k"]
        self.orderIndex = springType.value["indexes"][index]
        self.type     = springType


    def setLen(self, val):
        self.len0 = val


    def setStif(self, val):
        self.k = val


    def getMassTo(self):
        return self.massTo


    def getOrderInd(self):
        return self.orderIndex


    def getMasses(self):
        return self.massFrom, self.massTo


    def getLen0(self):
        return self.len0


    def getVector(self):
        return self.massFrom.getDistance(self.massTo)


    def getLen(self):
        return glm.length(self.getVector())


    def getForce(self):
        curLen = self.getVector()
        vecLen0 = curLen / glm.length(curLen) * self.len0

        return self.k * (curLen - vecLen0)


    def stabilize(self):
        if (self.type == SpringType.bend
                or self.massFrom.isPinned() and self.massTo.isPinned()
                or abs(self.len0) < 1e-6):
            return

        curLen = self.getLen()
        tau = (curLen - self.len0) / self.len0


        while tau > 0.01:
            diff = (curLen - self.len0) / curLen
            correctionVec = diff * self.getVector()
            notPinnedNum = (2. - self.massFrom.isPinned()
                              - self.massTo.isPinned())

            if not self.massFrom.isPinned():
                self.massFrom.move(correctionVec / notPinnedNum)

            if not self.massTo.isPinned():
                self.massTo.move(-correctionVec / notPinnedNum)

            curLen = self.getLen()
            tau = (curLen - self.len0) / self.len0

