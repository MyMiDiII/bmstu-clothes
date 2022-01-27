import sys

from PyQt5 import QtWidgets, uic
from darktheme.widget_template import DarkPalette

import PyQt5.QtCore as QtCore
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

        self.setPalette(DarkPalette())
        self.loadModelBtn.clicked.connect(self.load)
        self.yLeftTurnBtn.clicked.connect(self.leftTurn)
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


    def timerActions(self):
        if self.colorWindow:
            self.curColor = self.colorWindow.currentColor()
            self.colorBtn.setStyleSheet(
                BACKGROUNDSTRING % self.curColor.name()
            )

        self.GL.update(self.curColor.getRgbF())


    def leftTurn(self):
        pass


    def changeColor(self, color: QColor):
        self.curColor = color

    def chooseColor(self):
        """
            Выбор цвета отрезков
        """
        self.colorWindow = MiniColorDialog(self)
        self.colorWindow.setCurrentColor(self.curColor)
        self.colorWindow.show()


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    main = MainWindow()
    main.showMaximized()
    sys.exit(app.exec_())
