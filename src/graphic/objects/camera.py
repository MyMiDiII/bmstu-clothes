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
        self.speed = 0.01
        self.sensitivity = 0.05

        self.__updateVectors()


    def __updateVectors(self):
        sinYaw, cosYaw = (glm.sin(glm.radians(self.yaw)),
                          glm.cos(glm.radians(self.yaw)))
        sinPitch, cosPitch = (glm.sin(glm.radians(self.pitch)),
                          glm.cos(glm.radians(self.pitch)))
        sinRoll, cosRoll = (glm.sin(glm.radians(self.roll)),
                          glm.cos(glm.radians(self.roll)))

        newFront = glm.vec3()
        newFront.x = cosYaw * cosPitch
        newFront.y = sinPitch
        newFront.z = sinYaw * cosPitch

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
        self.pitch += angle
        self.__updateVectors()


    def rotateY(self, angle):
        self.yaw += angle
        self.__updateVectors()


    def rotateZ(self, angle):
        self.roll += angle
        self.__updateVectors()


    def changePerspective(self, angle=45, ratio=1, near=0.01, far=100):
        self.angle = angle
        self.ratio = ratio
        self.near = near
        self.far = far


    def continousTranslate(self, directions):
        self.position += self.speed * self.front * directions["w"]
        self.position -= self.speed * self.front * directions["s"]
        self.position -= self.speed * self.right * directions["a"]
        self.position += self.speed * self.right * directions["d"]


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

