from PyQt5 import QtGui
from PyQt5 import QtOpenGL
from PyQt5.QtGui import QMatrix4x4, QCursor

import OpenGL.GL as gl
from OpenGL import GLU

from PyQt5.QtCore import Qt, QPoint
from OpenGL.arrays import vbo
import glm
import glfw
import numpy as np

from graphic.shader import Shader

from graphic.objects.object import Object
from graphic.objects.camera import Camera

class myGL(QtOpenGL.QGLWidget):
    def __init__(self, parent=None):
        self.parent = parent
        QtOpenGL.QGLWidget.__init__(self, parent)

        self.camMode = False
        self.setMouseTracking(self.camMode)
        self.cursor = QCursor()
        self.cursorShapes = [Qt.ArrowCursor, Qt.BlankCursor]

        self.color = (255, 255, 255, 1.0)
        self.angle = 0
        self.object = Object()
        self.camera = Camera()

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
        #print("INIT")
        #print(self.proj)
        self.qglClearColor(QtGui.QColor(50, 50, 50))
        gl.glEnable(gl.GL_DEPTH_TEST)


    def resizeGL(self, width, height):
        #print("resize")
        gl.glViewport(0, 0, width, height)
        self.camera.changePerspective(ratio=width/height)
        self.camera.setPosition([0, 0, 3])


    def paintGL(self):
        #print("PAINT!")
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
        shader.setMat4("perspective", self.camera.getProjMatrix())
        shader.setMat4("view", self.camera.getVeiwMatrix())
        shader.setMat4("model", self.object.getModelMatrix())

        # устанавливаем цвет
        shader.setVec4("curColor", *self.color)

        # рисуем
        gl.glBindVertexArray(VAO)
        gl.glDrawElements(gl.GL_TRIANGLES, 6, gl.GL_UNSIGNED_INT, None)
        #gl.glPolygonMode(gl.GL_FRONT_AND_BACK, gl.GL_LINE)
        #print("PAINT END!")


    def translate(self, vec):
        self.camera.translate(*vec)


    def scale(self, coef):
        self.camera.zoom(coef)


    def rotate(self, vec):
        self.camera.rotateX(vec[0])
        self.camera.rotateY(vec[1])
        self.camera.rotateZ(vec[2])

    
    def mousePressEvent(self, event):
        selfPos = self.pos()
        self.lastPos = QPoint(selfPos.x() + self.width() // 2,
                              selfPos.y() + self.height() // 2
                       )
        self.cursor.setPos(self.lastPos)

        if event.button() == Qt.LeftButton:
            self.camMode = not self.camMode
            self.cursor.setShape(self.cursorShapes[self.camMode])
            self.setCursor(self.cursor)
            self.setMouseTracking(self.camMode)

        if self.camMode:
            print("on")
        else:
            print("off")


    def mouseMoveEvent(self, event):
        curPos = event.globalPos()

        if self.lastPos == curPos:
            return

        deltaX = curPos.x() - self.lastPos.x()
        deltaY = self.lastPos.y() - curPos.y()
        self.lastPos = curPos

        self.camera.rotation(deltaX, deltaY)


    def leaveEvent(self, event):
        if self.camMode:
            selfPos = self.pos()
            self.lastPos = QPoint(selfPos.x() + self.width() // 2,
                                  selfPos.y() + self.height() // 2
                           )
            self.cursor.setPos(self.lastPos)


    def wheelEvent(self, event):
        zoomCoef = event.pixelDelta().y() / 100
        self.camera.zoom(zoomCoef)


    def update(self, color, transVec):
        self.camera.continousTranslate(transVec)
        self.color = color
        self.updateGL()

