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
import load

################################################

from datetime import date

################################################

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

        self.translateVec = [0] * 3

        self.setPalette(DarkPalette())
        self.loadModelBtn.clicked.connect(self.load)

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
        self.zLeftTurnBtn.clicked.connect(self.zLeftRotate)
        self.zRightTurnBtn.clicked.connect(self.zRightRotate)

        self.colorBtn.clicked.connect(self.chooseColor)

        timer = QtCore.QTimer(self)
        timer.setInterval(50)
        timer.timeout.connect(self.timerActions)
        timer.start()


    def load(self):
        load.Load('cube.obj').load()
        self.GL.paintGL()
        QMessageBox.warning(
                self,
                ":(", "Уже "
                + date.today().strftime('%d.%m.%Y')
                + "!\nА эта кнопка все ещё не работает!")


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

        self.GL.transform(self.translateVec, "translate")
        self.GL.update(self.curColor.getRgbF())


    def scalePlus(self):
        self.GL.transform((-1,), "scale")


    def scaleMinus(self):
        self.GL.transform((1,), "scale")


    def moveUp(self):
        self.GL.transform((0, 0.1, 0), "translate")


    def moveDown(self):
        self.GL.transform((0, -0.1, 0), "translate")


    def moveRight(self):
        self.GL.transform((0.1, 0, 0), "translate")


    def moveLeft(self):
        self.GL.transform((-0.1, 0, 0), "translate")


    def moveFrom(self):
        self.GL.transform((0, 0, -0.1), "translate")


    def moveTo(self):
        self.GL.transform((0, 0, 0.1), "translate")


    def xLeftRotate(self):
        self.GL.transform((0, 1, 0), "rotate")


    def xRightRotate(self):
        self.GL.transform((0, -1, 0), "rotate")


    def yUpRotate(self):
        self.GL.transform((1, 0, 0), "rotate")


    def yDownRotate(self):
        self.GL.transform((-1, 0, 0), "rotate")


    def zLeftRotate(self):
        self.GL.transform((0, 0, 1), "rotate")


    def zRightRotate(self):
        self.GL.transform((0, 0, -1), "rotate")


    def keyPressEvent(self, event):
        if event.key() == Qt.Key_W:
            self.translateVec[2] = -0.1
        elif event.key() == Qt.Key_S:
            self.translateVec[2] = 0.1
        elif event.key() == Qt.Key_A:
            self.translateVec[0] = -0.05
        elif event.key() == Qt.Key_D:
            self.translateVec[0] = 0.05


    def keyReleaseEvent(self, event):
        if event.key() == Qt.Key_W:
            self.translateVec[2] = 0
        elif event.key() == Qt.Key_S:
            self.translateVec[2] = 0
        elif event.key() == Qt.Key_A:
            self.translateVec[0] = 0
        elif event.key() == Qt.Key_D:
            self.translateVec[0] = 0


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    main = MainWindow()
    main.showMaximized()
    sys.exit(app.exec_())
