import glm
import bisect

from math import sin, cos
from random import uniform

from clothes.spring import Spring

class Mass:
    def __init__(self, mass, pos, isPin=False):
        self.mass = mass
        self.springs = []
        self.pinned = isPin

        self.prevPos = glm.vec3(*pos)
        self.pos = glm.vec3(*pos)
        self.vel = glm.vec3()
        self.acc = glm.vec3()

        self.normal = glm.vec3()

        self.curTime = 0


    def isPinned(self):
        return self.pinned


    def getPos(self):
        return self.pos

    
    def getNorm(self):
        return self.normal


    def getSprings(self):
        return self.springs


    def getRadiusVector(self):
        return self.pos


    def move(self, vec):
        self.pos += vec

    
    def getPosition(self):
        return [self.pos.x, self.pos.y, self.pos.z]

    def getNormal(self):
        return [self.normal.x, self.normal.y, self.normal.z]


    def getNegNormal(self):
        return [-self.normal.x, -self.normal.y, -self.normal.z]


    def getDistance(self, mass):
       # print(mass)
       # print("mass", mass.getRadiusVector())
       # print("self", self.getRadiusVector())
       # print("diff", mass.getRadiusVector() - self.getRadiusVector())
        return mass.getRadiusVector() - self.getRadiusVector()


    def getForce(self, gravCoef, dampCoef, windCoef):
        if self.pinned:
            return glm.vec3()

        gravity = self.mass * glm.vec3(0, -gravCoef, 0)

        internal = glm.vec3()
        for spring in self.springs:
            internal += spring.getForce()

        damping = -dampCoef * self.vel

        x, y, z, t = self.pos.x, self.pos.y, self.pos.z, self.curTime / 1000
        #wind = (windCoef * glm.dot(self.normal,
        #       glm.vec3(
        #            0.1 * sin(5 * t),
        #            0,
        #            1.5 * abs(sin(z + 5 * t)) + 0.1 * cos(y + 5 * t))
        #       - self.vel) * self.normal)
        wind = glm.vec3()
        #wind = glm.vec3(
        #            0.5 * sin(x * y * t),
        #            - 0.5 * cos(z * t),
        #            0.5 * sin(cos(5 * x * y * z * t))
        #            )

        return gravity + internal + damping + wind

    
    def addSpring(self, massTo, len0, k, spType, index):
        spring = Spring(self, massTo, len0, k, spType, index)
        bisect.insort(self.springs, spring, key=lambda sp: sp.getOrderInd())

        #self.springs.append()


    def updateState(self, dt, gravity, damping, wind):
        if self.isPinned():
            return

        self.curTime += dt
        #self.pos = self.pos + dt * self.vel
        curPos = self.pos
        self.acc = self.getForce(gravity, damping, wind) / self.mass
        self.pos = 2 * self.pos - self.prevPos + self.acc * dt * dt
        self.vel = (self.pos - curPos) / dt
        self.prevPos = curPos

        #if self.pos.y < 0:
        #    self.pos = glm.vec3(self.pos.x, 0, self.pos.z)


    def __getOneSideNormal(self, mass1, mass2):
        vec1 = mass1.getPos() - self.pos
        vec2 = mass2.getPos() - self.pos
        crossProd = glm.cross(vec1, vec2)
        norm = glm.length(crossProd)
        #crossProd = crossProd if norm > 1e-3 else glm.vec3()

        return glm.normalize(crossProd)


    def updateNormal(self):
        self.normal = glm.vec3()
        normalSprings = [sp for sp in self.springs if sp.getOrderInd() not in
                [100]]
        #normalSprings = normalSprings[:3]

        for i, sp in enumerate(normalSprings):
            self.normal += self.__getOneSideNormal(
                    sp.getMassTo(),
                    normalSprings[i - 1].getMassTo()
                    )

        self.normal /= len(normalSprings)
        self.normal = glm.normalize(self.normal)

