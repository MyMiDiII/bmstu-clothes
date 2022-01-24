import glm

class Camera:
    def __init__(self, pos=(0,0,3), target=(0,0,0)):
        self.position = glm.vec3(*pos)
        self.target = glm.vec3(*target)
        self.direction = glm.normalize(self.position = self.target)
        self.right = glm.normalize(glm.cross(glm.vec3(0, 1, 0),
            self.direction))
        self.up = glm.cross(self.direction, self.right)
