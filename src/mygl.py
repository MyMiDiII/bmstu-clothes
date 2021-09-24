from PyQt5 import QtGui
from PyQt5 import QtOpenGL

import OpenGL.GL as gl

from OpenGL.arrays import vbo
import numpy as np

class myGL(QtOpenGL.QGLWidget):
    def __init__(self, parent=None):
        self.parent = parent
        QtOpenGL.QGLWidget.__init__(self, parent)

    def initializeGL(self):
        self.qglClearColor(QtGui.QColor(0, 0, 255))
        gl.glEnable(gl.GL_DEPTH_TEST)

        self.initGeometry()

    def initGeometry(self):
        self.cubeVtxArray = np.array(
            [[0.0, 0.0, 0.0],
             [1.0, 0.0, 0.0],
             [1.0, 1.0, 0.0],
             [0.0, 1.0, 0.0],
             [0.0, 0.0, 1.0],
             [1.0, 0.0, 1.0],
             [1.0, 1.0, 1.0],
             [0.0, 1.0, 1.0]])
        self.vertVBO = vbo.VBO(np.reshape(self.cubeVtxArray,
                          (1, -1)).astype(np.float32))
        self.vertVBO.bind()

    def paintGL(self):
        gl.glClear(gl.GL_COLOR_BUFFER_BIT | gl.GL_DEPTH_BUFFER_BIT)

        gl.glPushMatrix()    # push the current matrix to the current stack

        gl.glTranslate(0.0, 0.0, -50.0)    # third, translate cube to specified depth
        gl.glScale(20.0, 20.0, 20.0)       # second, scale cube
        gl.glTranslate(-0.5, -0.5, -0.5)   # first, translate cube center to origin

        gl.glEnableClientState(gl.GL_VERTEX_ARRAY)
        gl.glEnableClientState(gl.GL_COLOR_ARRAY)

        gl.glVertexPointer(3, gl.GL_FLOAT, 0, self.vertVBO)
        #gl.glColorPointer(3, gl.GL_FLOAT, 0, self.colorVBO)

        #gl.glDrawElements(gl.GL_QUADS, len(self.cubeIdxArray), gl.GL_UNSIGNED_INT, self.cubeIdxArray)

        gl.glDisableClientState(gl.GL_VERTEX_ARRAY)
        gl.glDisableClientState(gl.GL_COLOR_ARRAY)

        gl.glPopMatrix()    # restore the previous modelview matrix
