import glm

class Object(object):

    def __init__(self):
        self.modelMatrix= glm.mat4(1.0)


    def getModelMatrix(self):
        return self.modelMatrix


    def transform(self, matrix):
        self.modelMatrix = self.modelMatrix * matrix


    def translate(self, x, y, z):
        self.modelMatrix = glm.translate(self.modelMatrix, glm.vec3(x, y, z))


    def rotateX(self, angle):
        self.modelMatrix = glm.rotate(self.modelMatrix, glm.radians(angle),
                                        glm.vec3(1, 0, 0))


    def rotateY(self, angle):
        self.modelMatrix = glm.rotate(self.modelMatrix, glm.radians(angle),
                                        glm.vec3(0, 1, 0))


    def rotateZ(self, angle):
        self.modelMatrix = glm.rotate(self.modelMatrix, glm.radians(angle),
                                        glm.vec3(0, 0, 1))


    def scale(self, k):
        self.modelMatrix = glm.scale(self.modelMatrix, glm.vec3(k))


    def getPosition(self):
        return [self.modelMatrix[3, 0],
                self.modelMatrix[3, 1],
                self.modelMatrix[3, 2]]


    def setPosition(self, position):
        self.modelMatrix[3, 0] = position[0]
        self.modelMatrix[3, 1] = position[1]
        self.modelMatrix[3, 2] = position[2]

