import glm

from graphic.objects.object import Object

class Camera(Object):
    def __init__(self, angle=45, ratio=1, near=0.01, far=100):
        super().__init__()
        self.angle = angle
        self.ratio = ratio
        self.near = near
        self.far = far

        self.position = glm.vec3()

        self.front = glm.vec3(0, 0, -1)
        self.up = glm.vec3(0, 1, 0)
        self.right = glm.vec3()

        self.pitch = 0.0
        self.yaw = -90.0
        self.roll = 0.0

        self.worldUp = glm.vec3(0, 1, 0)
        self.speed = 0.04
        self.sensitivity = 0.05

        self.__updateVectors()


    def __updateVectors(self):
        newFront = glm.vec3()
        newFront.x = (glm.cos(glm.radians(self.yaw))
                         * glm.cos(glm.radians(self.pitch)))
        newFront.y = glm.sin(glm.radians(self.pitch)) 
        newFront.z = (glm.sin(glm.radians(self.yaw))
                         * glm.cos(glm.radians(self.pitch)))

        self.front = glm.normalize(newFront)
        self.right = glm.normalize(glm.cross(self.front, self.worldUp))
        self.up = glm.normalize(glm.cross(self.right, self.front))


    def getProjMatrix(self):
        return glm.perspective(glm.radians(self.angle), self.ratio, self.near,
                self.far)


    def getVeiwMatrix(self):
        return glm.lookAt(self.position, self.position + self.front, self.up)


    def setPosition(self, position):
        self.position = glm.vec3(*position)


    def translate(self, x, y, z):
        self.position += glm.vec3(x, y, z)


    def rotateX(self, angle):
        super().rotateX(angle)


    def rotateY(self, angle):
        super().rotateY(angle)


    def rotateZ(self, angle):
        super().rotateZ(angle)


    def rotateByAxis(self, axis, angle):
        super().rotateByAxis(axis, angle)

    
    def changePerspective(self, angle=45, ratio=1, near=0.01, far=100):
        self.angle = angle
        self.ratio = ratio
        self.near = near
        self.far = far


    def continousTranslate(self, directions):
        self.position += self.speed * self.front * directions["w"]
        self.position -= self.speed * self.front * directions["s"]
        self.position += (self.speed
                          * glm.normalize(glm.cross(self.position, self.up))
                          * directions["a"])
        self.position -= (self.speed
                          * glm.normalize(glm.cross(self.position, self.up))
                          * directions["d"])


    def rotation(self, deltaX, deltaY):
        self.yaw += deltaX * self.sensitivity
        self.pitch += deltaY * self.sensitivity

        if self.pitch > 89.0:
            self.pitch = 89.0

        if self.pitch < -89.0:
            self.pitch = -89.0

        self.__updateVectors()


    def zoom(self, k):
        self.angle -= k
        if self.angle < 1.0:
            self.angle = 1.0
        if self.angle > 100.0:
            self.angle = 100.0

