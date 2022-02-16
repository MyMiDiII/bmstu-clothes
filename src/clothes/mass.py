import glm

from clothes.spring import Spring

class Mass:
    def __init__(self, mass, pos, isPinned=False):
        self.mass = mass

        self.pos = glm.vec3(*pos)
        self.vel = glm.vec3()
        self.acc = glm.vec3()

        self.pinned = isPinned

        self.springs = []


    def getRadiusVector(self):
        return self.pos

    
    def getPosition(self):
        return (self.pos.x, self.pos.y, self.pos.z)


    def getDistance(self, mass):
        return mass.getRadiusVector() - self.getRadiusVector()


    def getForce(self, gravCoef, dampCoef):
        if self.pinned:
            return glm.vec3()

        gravity = self.mass * glm.vec3(0, -gravCoef, 0)

        internal = glm.vec3()
        for spring in self.springs:
            internal += spring.getForce()

        damping = -dampCoef * self.vel

        return gravity + internal + damping

    
    def addSpring(self, massTo, len0, k):
        self.springs.append(Spring(self, massTo, len0, k))


    def updateState(self, dt, gravity, damping):
        self.acc = self.getForce(gravity, damping) / self.mass
        self.vel = self.vel + dt * self.acc
        self.pos = self.pos + dt * self.vel
