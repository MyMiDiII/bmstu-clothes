import glm

from graphic.objects.object import Object

class Camera(Object):
    def __init__(self, angle=45, ratio=1, near=0.01, far=100):
        super().__init__()
        self.angle = angle
        self.ratio = ratio
        self.near = near
        self.far = far
        self.viewMatrix = glm.mat4(1.0)


    def __updateViewMatrix(self):
        self.viewMatrix = glm.inverse(self.getModelMatrix())


    def getProjMatrix(self):
        return glm.perspective(glm.radians(self.angle), self.ratio, self.near,
                self.far)


    def getVeiwMatrix(self):
        return self.viewMatrix


    def setPosition(self, position):
        super().setPosition(position)
        self.__updateViewMatrix()


    def translate(self, x, y, z):
        super().translate(x, y, z)
        self.__updateViewMatrix()


    def scale(self, k):
        super().scale(k)
        self.__updateViewMatrix()


    def rotateX(self, angle):
        super().rotateX(angle)
        self.__updateViewMatrix()


    def rotateY(self, angle):
        super().rotateY(angle)
        self.__updateViewMatrix()


    def rotateZ(self, angle):
        super().rotateZ(angle)
        self.__updateViewMatrix()


    def rotateByAxis(self, axis, angle):
        super().rotateByAxis(axis, angle)
        self.__updateViewMatrix()

    
    def changePerspective(self, angle=45, ratio=1, near=0.01, far=100):
        self.angle = angle
        self.ratio = ratio
        self.near = near
        self.far = far


    def zoom(self, k):
        self.angle -= k
        if self.angle < 1.0:
            self.angle = 1.0
        if self.angle > 100.0:
            self.angle = 100.0
        print(self.angle)

