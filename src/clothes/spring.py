import glm

class Spring:

    def __init__(self, massFrom, massTo, len0, k, springType, index):
        self.massFrom = massFrom
        self.massTo   = massTo
        self.len0     = len0
        self.k        = k
        self.type     = springType

        self.orderIndex = index


    def getMassTo(self):
        return self.massTo


    def getOrderInd(self):
        return self.orderIndex


    def getMasses(self):
        return self.massFrom, self.massTo


    def getLen0(self):
        return self.len0


    def getVector(self):
        #print("two mass", self.massFrom, self.massTo)
        #print(self.massFrom.getDistance(self.massTo))
        return self.massFrom.getDistance(self.massTo)


    def getLen(self):
        #print(self.getVector())
        return glm.length(self.getVector())


    def getForce(self):
        curLen = self.getVector()
        vecLen0 = curLen / glm.length(curLen) * self.len0

        return self.k * (curLen - vecLen0)


    def stabilize(self):
        # print("STABILIZE")
        if self.massFrom.isPinned() and self.massTo.isPinned():
            return

        curLen = self.getLen()
        tau = (curLen - self.len0) / self.len0


        while tau > 0.01:
            #print("len0", self.len0)
            #print("mF", self.massFrom.getPos())
            #print("mT", self.massTo.getPos())
            #print("cl", curLen)
            #print("tau", tau)
            diff = (curLen - self.len0) / curLen
            correctionVec = diff * self.getVector()
            #print("cv", correctionVec)
            notPinnedNum = (2. - self.massFrom.isPinned()
                              - self.massTo.isPinned())
            #print("pn", notPinnedNum)

            if not self.massFrom.isPinned():
                self.massFrom.move(correctionVec / notPinnedNum)

            if not self.massTo.isPinned():
                self.massTo.move(-correctionVec / notPinnedNum)

            curLen = self.getLen()
            tau = (curLen - self.len0) / self.len0

