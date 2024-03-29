from PyQt5 import QtGui
from PyQt5 import QtOpenGL
from PyQt5.QtGui import QMatrix4x4, QCursor

import OpenGL.GL as gl
import glm
from OpenGL import GLU

from PyQt5.QtCore import Qt, QPoint
from OpenGL.arrays import vbo
import glfw
import numpy as np
from time import time

import ctypes

from graphic.shader import Shader

from graphic.objects.camera import Camera
from clothes.massspringsystem import MassSpringModel
from clothes.pattern import Cloth, TShirt

import graphic.config as cfg


class myGL(QtOpenGL.QGLWidget):
    def __init__(self, parent=None):
        self.frames = 0
        self.startTime = time()
        self.fps = 0

        self.parent = parent
        QtOpenGL.QGLWidget.__init__(self, parent)
        self.setFocusPolicy(Qt.ClickFocus)

        self.polyMode = False
        self.camMode = False
        self.setMouseTracking(self.camMode)
        self.cursor = QCursor()
        self.cursorShapes = [Qt.ArrowCursor, Qt.BlankCursor]

        self.color = (1, 1, 1, 1.0)
        self.angle = 0
        self.tshirt = TShirt()
        self.object = MassSpringModel(self.tshirt)
        self.object.translate(0, 0, 0)
        self.camera = Camera()

        self.ambient = 0.3
        self.diffuse = 0.55
        self.specular = 0.01


    def initializeGL(self):
        self.qglClearColor(QtGui.QColor(50, 50, 50))
        gl.glEnable(gl.GL_DEPTH_TEST)

        # устанавливаем шейдры
        self.shader = Shader("shader.vs", "shader.fs")
        self.shader.use()



    def resizeGL(self, width, height):
        gl.glViewport(0, 0, width, height)
        self.camera.changePerspective(ratio=width/height)
        self.camera.setPosition([-1.2, 0.25, 1.2])
        self.camera.rotateX(-13)
        self.camera.rotateY(23)


    def paintGL(self):
        # очищаем экран
        gl.glClear(gl.GL_COLOR_BUFFER_BIT | gl.GL_DEPTH_BUFFER_BIT)

        # копируем массив вершин в вершинный буфер
        VBO = gl.glGenBuffers(1)
        gl.glBindBuffer(gl.GL_ARRAY_BUFFER, VBO)
        gl.glBufferData(gl.GL_ARRAY_BUFFER, self.object.getVertexes(),
                        gl.GL_STATIC_DRAW)

        # копируем индексный массив в элементный буфер
        EBO = gl.glGenBuffers(1)
        gl.glBindBuffer(gl.GL_ELEMENT_ARRAY_BUFFER, EBO)
        gl.glBufferData(gl.GL_ELEMENT_ARRAY_BUFFER, self.object.getIndices(),
                gl.GL_STATIC_DRAW)

        # устанавливаем указатели вершинных атрибутов
        gl.glVertexAttribPointer(0, 3, gl.GL_FLOAT, False,
                                     6 * glm.sizeof(glm.float32), None)
        gl.glEnableVertexAttribArray(0)

        gl.glVertexAttribPointer(1, 3, gl.GL_FLOAT, False,
                                     6 * glm.sizeof(glm.float32),
                                     ctypes.c_void_p(3 *
                                                      glm.sizeof(glm.float32)))
        gl.glEnableVertexAttribArray(1)

        # преобразование
        self.shader.setMat4("perspective", self.camera.getProjMatrix())
        self.shader.setMat4("view", self.camera.getVeiwMatrix())
        self.shader.setMat4("model", self.object.getModelMatrix())

        # устанавливаем цвет
        self.shader.setVec4("curColor", *self.color)

        # настройки света
        self.shader.setVec4("light", *cfg.LIGHT_COLOR)
        self.shader.setFloat("ambientCoef", self.ambient)
        self.shader.setFloat("diffuseCoef", self.diffuse)
        self.shader.setFloat("specularCoef", self.specular)
        self.shader.setVec3("lightPos", *self.camera.getPosition())
        self.shader.setVec3("viewPos", *self.camera.getPosition())

        # рисуем
        gl.glDrawElements(gl.GL_TRIANGLES, self.object.getIndices().size,
                          gl.GL_UNSIGNED_INT, None)

        if self.polyMode:
            gl.glPolygonMode(gl.GL_FRONT_AND_BACK, gl.GL_LINE)
        else:
            gl.glPolygonMode(gl.GL_FRONT_AND_BACK, gl.GL_FILL)


        gl.glLightModelf(gl.GL_LIGHT_MODEL_TWO_SIDE, gl.GL_TRUE)


    def translate(self, vec):
        self.camera.translate(*vec)


    def scale(self, coef):
        self.camera.zoom(coef)


    def rotate(self, vec):
        self.camera.rotateX(vec[0])
        self.camera.rotateY(vec[1])
        self.camera.rotateZ(vec[2])


    def mousePressEvent(self, event):
        selfPos = self.parent.mapToGlobal(self.pos())
        self.lastPos = QPoint(selfPos.x() + self.width() // 2,
                              selfPos.y() + self.height() // 2
                       )
        self.cursor.setPos(self.lastPos)

        if event.button() == Qt.LeftButton:
            self.camMode = not self.camMode
            self.cursor.setShape(self.cursorShapes[self.camMode])
            self.setCursor(self.cursor)
            self.setMouseTracking(self.camMode)

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
            selfPos = self.parent.mapToGlobal(self.pos())
            self.lastPos = QPoint(selfPos.x() + self.width() // 2,
                                  selfPos.y() + self.height() // 2
                           )
            self.cursor.setPos(self.lastPos)


    def wheelEvent(self, event):
        zoomCoef = event.pixelDelta().y() / 100
        self.camera.zoom(zoomCoef)


    def update(self, dt, color, transVec):
        self.camera.continousTranslate(transVec)
        self.color = color
        self.object.update(dt)
        self.updateGL()

        self.frames += 1


    def getFps(self):
        fps = self.frames
        self.frames = 0

        return fps


    def updatePhys(self, what, how):
        if what == "wind":
            self.object.setWind(how)


    def switchPolyMode(self):
        self.polyMode = not self.polyMode


    def setAmb(self, val):
        self.ambient = val


    def setDiff(self, val):
        self.diffuse = val


    def setSpec(self, val):
        self.specular = val


    def setStif(self, val):
        self.object.setStif(val)


    def setMass(self, val):
        self.object.setMass(val)


    def setGrav(self, val):
        self.object.setGrav(val)


    def setCloth(self, size):
        self.tshirt = Cloth(size, size)
        self.object = MassSpringModel(self.tshirt)


    def setTShirt(self):
        self.tshirt = TShirt()
        self.object = MassSpringModel(self.tshirt)
