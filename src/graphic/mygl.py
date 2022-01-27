from PyQt5 import QtGui
from PyQt5 import QtOpenGL
from PyQt5.QtGui import QMatrix4x4

import OpenGL.GL as gl
from OpenGL import GLU

from OpenGL.arrays import vbo
import glm
import glfw
import numpy as np

from graphic.shader import Shader

from graphic.objects.object import Object

class myGL(QtOpenGL.QGLWidget):
    def __init__(self, parent=None):
        self.parent = parent
        QtOpenGL.QGLWidget.__init__(self, parent)
        self.proj = None
        self.color = (255, 255, 255, 1.0)
        self.angle = 0
        self.object = Object()

        # !!! в класс модельки
        self.vrtxs = np.array(
        ((-0.5, -0.5, 0),
         ( 0.5, -0.5, 0),
         ( 0.5,  0.5, 0),
         (-0.5,  0.5, 0)
        ),
        dtype='float32')

        self.indices = np.array([0, 1, 3, 1, 2, 3], dtype='int32')

    def update(self, color):
        self.color = color
        self.updateGL()


    def initializeGL(self):
        print("INIT")
        #print(self.proj)
        self.qglClearColor(QtGui.QColor(50, 50, 50))
        gl.glEnable(gl.GL_DEPTH_TEST)


    def resizeGL(self, width, height):
        gl.glViewport(0, 0, width, height)
        self.proj = glm.perspective(glm.radians(45), width / height, 0.01, 100)
        self.proj = glm.translate(self.proj, glm.vec3(0, 0, -3))


    def paintGL(self):
        print("PAINT!")
        #print(list(self.indices))

        # очищаем экран
        gl.glClear(gl.GL_COLOR_BUFFER_BIT | gl.GL_DEPTH_BUFFER_BIT)

        # создаем объекст вершинного массива
        VAO = gl.glGenVertexArrays(1)
        gl.glBindVertexArray(VAO)

        # копируем массив вершин в вершинный буфер
        VBO = gl.glGenBuffers(1)
        gl.glBindBuffer(gl.GL_ARRAY_BUFFER, VBO)
        gl.glBufferData(gl.GL_ARRAY_BUFFER, self.vrtxs, gl.GL_STATIC_DRAW)

        # копируем индексный массив в элементный буфер
        EBO = gl.glGenBuffers(1)
        gl.glBindBuffer(gl.GL_ELEMENT_ARRAY_BUFFER, EBO)
        gl.glBufferData(gl.GL_ELEMENT_ARRAY_BUFFER,
                self.indices, gl.GL_STATIC_DRAW)

        # устанавливаем указатели вершинных атрибутов
        gl.glVertexAttribPointer(0, 3, gl.GL_FLOAT, False, 0, None)
        gl.glEnableVertexAttribArray(0)

        # устанавливаем шейдры
        shader = Shader("shader.vs", "shader.fs")
        shader.use()

        # преобразование
        print(self.proj * self.object.getModelMatrix())
        self.object.rotateZ(0.5)
        shader.setMat4("perspective", self.proj)
        shader.setMat4("model", self.object.getModelMatrix())

        # устанавливаем цвет
        shader.setVec4("curColor", *self.color)

        # рисуем
        gl.glBindVertexArray(VAO)
        gl.glDrawElements(gl.GL_TRIANGLES, 6, gl.GL_UNSIGNED_INT, None)
        #gl.glPolygonMode(gl.GL_FRONT_AND_BACK, gl.GL_LINE)
        #print("PAINT END!")


    def transform(self, turn):
        print("TURN!")
