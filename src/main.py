import sys

from PyQt5 import QtWidgets, uic
from darktheme.widget_template import DarkPalette

import PyQt5.QtCore as QtCore
from PyQt5.QtCore import Qt
import PyQt5.QtWidgets
from PyQt5.QtWidgets import QMessageBox
from PyQt5.QtWidgets import QColorDialog
from PyQt5.QtGui import QColor

from graphic.ui_mainwindow import Ui_MainWindow

from widgets.colordialog import MiniColorDialog

BACKGROUNDSTRING = "background-color: %s"


class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    """
        Класс главного окна
    """

    def __init__(self, *args, **kwargs):
        """
            Инициализация главного окна
        """
        super(MainWindow, self).__init__(*args, **kwargs)
        self.setupUi(self)

        self.curColor = QColor(255, 255, 255, 1)
        self.colorWindow = None
        self.wind = True

        self.translateVec = {"w" : False, "s" : False,
                             "a" : False, "d" : False}

        self.setPalette(DarkPalette())

        self.plusBtn.clicked.connect(self.scalePlus)
        self.minusBtn.clicked.connect(self.scaleMinus)

        self.upBtn.clicked.connect(self.moveUp)
        self.downBtn.clicked.connect(self.moveDown)
        self.rightBtn.clicked.connect(self.moveRight)
        self.leftBtn.clicked.connect(self.moveLeft)
        self.fromBtn.clicked.connect(self.moveFrom)
        self.toBtn.clicked.connect(self.moveTo)

        self.xLeftTurnBtn.clicked.connect(self.xLeftRotate)
        self.xRightTurnBtn.clicked.connect(self.xRightRotate)
        self.yUpTurnBtn.clicked.connect(self.yUpRotate)
        self.yDownTurnBtn.clicked.connect(self.yDownRotate)

        self.colorBtn.clicked.connect(self.chooseColor)
        self.windChBox.stateChanged.connect(self.switchWind)

        self.ambDSB.valueChanged.connect(self.setAmb)
        self.diffDSB.valueChanged.connect(self.setDiff)
        self.specDSB.valueChanged.connect(self.setSpec)

        self.stifDSB.valueChanged.connect(self.setStif)
        self.massDSB.valueChanged.connect(self.setMass)
        self.gravDSB.valueChanged.connect(self.setGrav)

        self.clothRbtn.toggled.connect(self.switchMode)
        self.tshirtRBtn.toggled.connect(self.switchMode)

        self.sizeSB.valueChanged.connect(self.setSize)

        timer = QtCore.QTimer(self)
        self.dt = 5
        timer.setInterval(self.dt)
        timer.timeout.connect(self.timerActions)
        timer.start()

        fpsTimer = QtCore.QTimer(self)
        fpsTimer.setInterval(1000)
        fpsTimer.timeout.connect(self.fpsTimerActions)
        fpsTimer.start()


    def setSize(self):
        size = self.sizeSB.value()
        self.GL.setCloth(size)


    def switchMode(self):
        btn = self.sender()

        if btn.isChecked():
            if btn == self.clothRbtn:
                self.sizeSB.setEnabled(True)
                size = self.sizeSB.value()
                self.GL.setCloth(size)
            else:
                self.sizeSB.setEnabled(False)
                self.GL.setTShirt()


    def setGrav(self):
        self.GL.setGrav(self.gravDSB.value())


    def setMass(self):
        self.GL.setMass(self.massDSB.value())


    def setStif(self):
        self.GL.setStif(self.stifDSB.value())


    def setAmb(self):
        self.GL.setAmb(self.ambDSB.value())


    def setDiff(self):
        self.GL.setDiff(self.diffDSB.value())


    def setSpec(self):
        self.GL.setSpec(self.specDSB.value())


    def switchWind(self):
        wind = self.windChBox.isChecked()
        self.GL.updatePhys("wind", wind)


    def chooseColor(self):
        self.colorWindow = MiniColorDialog(self)
        self.colorWindow.setCurrentColor(self.curColor)
        self.colorWindow.show()


    def timerActions(self):
        if self.colorWindow:
            self.curColor = self.colorWindow.currentColor()
            self.colorBtn.setStyleSheet(
                BACKGROUNDSTRING % self.curColor.name()
            )

        self.GL.update(self.dt / 1000, self.curColor.getRgbF(),
                self.translateVec)


    def fpsTimerActions(self):
        fps = self.GL.getFps()
        self.fpsLbl.setText("FPS: {:2}".format(fps))


    def scalePlus(self):
        self.GL.scale(1)


    def scaleMinus(self):
        self.GL.scale(-1)


    def moveUp(self):
        self.GL.translate((0, 0.5, 0))


    def moveDown(self):
        self.GL.translate((0, -0.5, 0))


    def moveRight(self):
        self.GL.translate((0.5, 0, 0))


    def moveLeft(self):
        self.GL.translate((-0.5, 0, 0))


    def moveFrom(self):
        self.GL.translate((0, 0, -0.5))


    def moveTo(self):
        self.GL.translate((0, 0, 0.5))


    def xLeftRotate(self):
        self.GL.rotate((0, -1, 0))


    def xRightRotate(self):
        self.GL.rotate((0, 1, 0))


    def yUpRotate(self):
        self.GL.rotate((-1, 0, 0))


    def yDownRotate(self):
        self.GL.rotate((1, 0, 0))


    def keyPressEvent(self, event):
        if event.key() == Qt.Key_W:
            self.translateVec["w"] = True
        elif event.key() == Qt.Key_S:
            self.translateVec["s"] = True
        elif event.key() == Qt.Key_A:
            self.translateVec["a"] = True
        elif event.key() == Qt.Key_D:
            self.translateVec["d"] = True
        elif event.key() == Qt.Key_P:
            self.GL.switchPolyMode()


    def keyReleaseEvent(self, event):
        if event.key() == Qt.Key_W:
            self.translateVec["w"] = False
        elif event.key() == Qt.Key_S:
            self.translateVec["s"] = False
        elif event.key() == Qt.Key_A:
            self.translateVec["a"] = False
        elif event.key() == Qt.Key_D:
            self.translateVec["d"] = False


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    main = MainWindow()
    main.showMaximized()
    sys.exit(app.exec_())
