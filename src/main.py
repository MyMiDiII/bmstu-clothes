import sys

from PyQt5 import QtWidgets, uic
from darktheme.widget_template import DarkPalette

import PyQt5.QtWidgets
from PyQt5.QtWidgets import QMessageBox
from PyQt5.QtWidgets import QColorDialog
from PyQt5.QtGui import QColor

from ui_mainwindow import Ui_MainWindow

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

        self.setPalette(DarkPalette())
        self.loadModelBtn.clicked.connect(self.load)
        self.yLeftTurnBtn.clicked.connect(self.leftTurn)
        self.colorBtn.clicked.connect(self.chooseColor)

    def load(self):
        load.Load('cube.obj').load()
        self.GL.paintGL()
        QMessageBox.warning(
                self,
                ":(", "Уже "
                + date.today().strftime('%d.%m.%Y')
                + "!\nА эта кнопка все ещё не работает!")

    def leftTurn(self):
        pass


    def changeColor(self, color: QColor):
        self.colorBtn.setStyleSheet(
            BACKGROUNDSTRING % color.name()
        )
        self.GL.changeColor(color.getRgbF())

    def chooseColor(self):
        """
            Выбор цвета отрезков
        """
        colorWindow = MiniColorDialog(self)
        colorWindow.currentColorChanged.connect(self.changeColor)
        colorWindow.show()


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    main = MainWindow()
    main.showMaximized()
    sys.exit(app.exec_())
