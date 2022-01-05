from PyQt5 import QtGui
from PyQt5 import QtOpenGL
from PyQt5.QtGui import QMatrix4x4

import OpenGL.GL as gl
from OpenGL import GLU

from OpenGL.arrays import vbo
import glm
import glfw
import numpy as np

class myGL(QtOpenGL.QGLWidget):
    def __init__(self, parent=None):
        self.parent = parent
        QtOpenGL.QGLWidget.__init__(self, parent)
        self.proj = QMatrix4x4()

        # !!! в класс модельки
        self.vrtxs = np.array(
        ((-0.5, -0.5, 0),
         ( 0.5, -0.5, 0),
         ( 0.5,  0.5, 0),
         (-0.5,  0.5, 0)
        ),
        dtype='float32')

        self.indices = np.array([0, 1, 3, 1, 2, 3], dtype='int32')


    def initializeGL(self):
        self.qglClearColor(QtGui.QColor(50, 50, 50))
        gl.glEnable(gl.GL_DEPTH_TEST)

    def resizeGL(self, width, height):
        gl.glViewport(0, 0, width, height)
        self.proj.setToIdentity()
        self.proj.perspective(45, width / height, 0.01, 100)

    def paintGL(self):
        print("PAINT!")
        print(list(self.indices))
        #gl.glClear(gl.GL_COLOR_BUFFER_BIT | gl.GL_DEPTH_BUFFER_BIT)

        #VAO = gl.glGenVertexArrays(1)
        #gl.glBindVertexArray(VAO)

        #VBO = gl.glGenBuffers(1)
        #gl.glBindBuffer(gl.GL_ARRAY_BUFFER, VBO)
        #gl.glBufferData(gl.GL_ARRAY_BUFFER, self.vrtxs, gl.GL_STATIC_DRAW)

        #gl.glVertexAttribPointer(0, 3, gl.GL_FLOAT, False, 0, None)
        #gl.glEnableVertexAttribArray(0)

        #gl.glBindBuffer(gl.GL_ARRAY_BUFFER, 0)
        #gl.glBindVertexArray(0)

        #gl.glBindVertexArray(VAO)
        #gl.glDrawArrays(gl.GL_TRIANGLES, 0, 3)

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

        # рисуем
        gl.glBindVertexArray(VAO)
        gl.glDrawElements(gl.GL_TRIANGLES, 6, gl.GL_UNSIGNED_INT, None)
        gl.glPolygonMode(gl.GL_FRONT_AND_BACK, gl.GL_LINE)
        print("PAINT END!")


    def transform(self, turn):
        print("TURN!")
