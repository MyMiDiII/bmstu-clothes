import sys

from PyQt5 import QtWidgets, uic
from darktheme.widget_template import DarkPalette

from PyQt5.QtWidgets import QMessageBox

from ui_mainwindow import Ui_MainWindow

import load

################################################

from datetime import date

################################################


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

    def load(self):
        load.Load('cube.obj').load()
        self.GL.paintGL()
        QMessageBox.warning(
                self,
                ":(", "Уже "
                + date.today().strftime('%d.%m.%Y')
                + "!\nА эта кнопка все ещё не работает!")

    def leftTurn(self):
        self.GL.transform((10, 0, 1, 0))


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    main = MainWindow()
    main.showMaximized()
    sys.exit(app.exec_())
