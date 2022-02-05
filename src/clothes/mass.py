import glm

class Mass:
    def __init__(self, mass, pos):
        self.mass = mass

        self.pos = glm.vec3(*pos)
        self.vel = glm.vec3()
        self.acc = glm.vec3()

    
    def getPosition(self):
        return (self.pos.x, self.pos.y, self.pos.z)


    def getForce(self):
        gravity = self.mass * glm.vec3(0, -0.05, 0)

        return gravity


    def updateState(self, dt):
        self.acc = self.getForce() / self.mass
        self.vel = self.vel + dt * self.acc
        self.pos = self.pos + dt * self.vel
