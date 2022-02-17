import glm

class Spring:

    def __init__(self, massFrom, massTo, len0, k):
        self.massFrom = massFrom
        self.massTo   = massTo
        self.len0     = len0
        self.k        = k


    def getVector(self):
        return self.massFrom.getDistance(self.massTo)


    def getLength(self):
        return glm.length(self.getVector())


    def getForce(self):
        curLen = self.getVector()
        vecLen0 = curLen / glm.length(curLen) * self.len0

        return self.k * (curLen - vecLen0)
