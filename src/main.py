import sys

from PyQt5 import QtWidgets, uic
from darktheme.widget_template import DarkPalette

from PyQt5.QtWidgets import QMessageBox

from ui_mainwindow import Ui_MainWindow

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

    def load(self):
        QMessageBox.warning(
                self,
                ":(", "Уже "
                + date.today().strftime('%d.%m.%Y')
                + "!\nА эта кнопка все ещё не работает!")


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    main = MainWindow()
    main.showMaximized()
    sys.exit(app.exec_())
