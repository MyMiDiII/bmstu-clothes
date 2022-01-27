import glm

from graphic.objects.object import Object

class Camera(Object):
    def __init__(self):
        super().__init__()
        self.viewMatrix = glm.mat4(1.0)


    def __updateViewMatrix(self):
        self.viewMatrix = glm.inverse(self.getModelMatrix())


    def getVeiwMatrix(self):
        return self.viewMatrix


    def setPosition(self, position):
        super().setPosition(position)
        self.__updateViewMatrix()
