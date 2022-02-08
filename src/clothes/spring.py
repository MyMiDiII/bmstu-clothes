import glm

class Spring:

    def __init__(self, massFrom, massTo, len0, k):
        self.massFrom = massFrom
        self.massTo   = massTo
        self.len0     = len0
        self.k        = k


    def getForce(self):
        curLen = self.massFrom.getDistance(self.massTo)
        vecLen0 = curLen / glm.length(curLen) * self.len0

        return self.k * (curLen - vecLen0)
