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


    def getDistance(self, mass):
       # print(mass)
       # print("mass", mass.getRadiusVector())
       # print("self", self.getRadiusVector())
       # print("diff", mass.getRadiusVector() - self.getRadiusVector())
        return mass.getRadiusVector() - self.getRadiusVector()


    def getForce(self, gravCoef, dampCoef):
        if self.pinned:
            return glm.vec3()

        gravity = self.mass * glm.vec3(0, -gravCoef, 0)

        internal = glm.vec3()
        for spring in self.springs:
            internal += spring.getForce()

        damping = -dampCoef * self.vel

        x, y, z, t = self.pos.x, self.pos.y, self.pos.z, self.curTime * 100
        wind = glm.vec3(0.1 * sin(t), 0, 0.01 *
                abs(sin(z + t)) + 0.1 * abs(cos(y + t)))
        #wind = glm.vec3(uniform(0, 0.5), 0, uniform(0, 0.5))

        return gravity + internal + damping + wind

    
    def addSpring(self, massTo, len0, k, spType, index):
        spring = Spring(self, massTo, len0, k, spType, index)
        bisect.insort(self.springs, spring, key=lambda sp: sp.getOrderInd())

        #self.springs.append()


    def updateState(self, dt, gravity, damping):
        if self.isPinned():
            return

        self.curTime += dt
        self.acc = self.getForce(gravity, damping) / self.mass
        self.vel = self.vel + dt * self.acc
        self.pos = self.pos + dt * self.vel

        #if self.pos.y < 0:
        #    self.pos = glm.vec3(self.pos.x, 0, self.pos.z)


    def __getOneSideNormal(self, mass1, mass2):
        vec1 = mass1.getPos() - self.pos
        vec2 = mass2.getPos() - self.pos
        return glm.normalize(glm.cross(vec1, vec2))


    def updateNormal(self):
        self.normal = glm.vec3()
        normalSprings = [sp for sp in self.springs if sp.getOrderInd() != 100]

        for i, sp in enumerate(normalSprings):
            self.normal += self.__getOneSideNormal(
                    normalSprings[i - 1].getMassTo(),
                    sp.getMassTo()
                    )

