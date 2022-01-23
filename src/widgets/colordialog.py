from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QLayout, QWidget, QApplication

class MiniColorDialog(QtWidgets.QColorDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setModal(False)
        self.setSizeGripEnabled(True)
        self.layout().setSizeConstraint(QLayout.SetNoConstraint)

        self.setWindowTitle("Цвет")
        self.setFixedSize(200, 150)
        self.__minimize()
        self.__move()

    def __minimize(self):
        for children in self.findChildren(QtWidgets.QWidget):
            classname = children.metaObject().className()
            if classname not in ("QColorPicker", "QColorLuminancePicker"):
                children.hide()


    def __move(self):
        screenSize = QApplication.desktop().availableGeometry().getRect()[2:]
        winSize = self.geometry().getRect()[2:]
        moveVec = (screenSize[0] - winSize[0], screenSize[1] - winSize[1])
        self.move(*moveVec)
