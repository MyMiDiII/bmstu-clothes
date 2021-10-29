from PyQt5 import QtGui
from PyQt5 import QtOpenGL

import OpenGL.GL as gl
from OpenGL import GLU

from OpenGL.arrays import vbo
import numpy as np

class myGL(QtOpenGL.QGLWidget):
    def __init__(self, parent=None):
        self.parent = parent
        QtOpenGL.QGLWidget.__init__(self, parent)

    def initializeGL(self):
        self.qglClearColor(QtGui.QColor(0, 0, 0))

    def resizeGL(self, width, height):
        pass 

    def paintGL(self):
        pass

    def initGeometry(self):
        pass
