# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainwindow.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setEnabled(True)
        MainWindow.resize(1444, 843)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.loadBox = QtWidgets.QGroupBox(self.centralwidget)
        self.loadBox.setObjectName("loadBox")
        self.gridLayout = QtWidgets.QGridLayout(self.loadBox)
        self.gridLayout.setObjectName("gridLayout")
        self.loadModelBtn = QtWidgets.QPushButton(self.loadBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.loadModelBtn.sizePolicy().hasHeightForWidth())
        self.loadModelBtn.setSizePolicy(sizePolicy)
        self.loadModelBtn.setMaximumSize(QtCore.QSize(16777215, 50))
        self.loadModelBtn.setObjectName("loadModelBtn")
        self.gridLayout.addWidget(self.loadModelBtn, 0, 0, 1, 2)
        self.deleteModelBtn = QtWidgets.QPushButton(self.loadBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.deleteModelBtn.sizePolicy().hasHeightForWidth())
        self.deleteModelBtn.setSizePolicy(sizePolicy)
        self.deleteModelBtn.setMaximumSize(QtCore.QSize(16777215, 50))
        self.deleteModelBtn.setObjectName("deleteModelBtn")
        self.gridLayout.addWidget(self.deleteModelBtn, 1, 0, 1, 2)
        self.verticalLayout.addWidget(self.loadBox)
        self.scaleBox = QtWidgets.QGroupBox(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.scaleBox.sizePolicy().hasHeightForWidth())
        self.scaleBox.setSizePolicy(sizePolicy)
        self.scaleBox.setObjectName("scaleBox")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.scaleBox)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.minusBtn = QtWidgets.QPushButton(self.scaleBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.minusBtn.sizePolicy().hasHeightForWidth())
        self.minusBtn.setSizePolicy(sizePolicy)
        self.minusBtn.setMaximumSize(QtCore.QSize(40, 40))
        self.minusBtn.setObjectName("minusBtn")
        self.horizontalLayout.addWidget(self.minusBtn)
        self.plusBtn = QtWidgets.QPushButton(self.scaleBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.plusBtn.sizePolicy().hasHeightForWidth())
        self.plusBtn.setSizePolicy(sizePolicy)
        self.plusBtn.setMaximumSize(QtCore.QSize(40, 40))
        self.plusBtn.setObjectName("plusBtn")
        self.horizontalLayout.addWidget(self.plusBtn)
        self.verticalLayout.addWidget(self.scaleBox)
        self.translateBox = QtWidgets.QGroupBox(self.centralwidget)
        self.translateBox.setObjectName("translateBox")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.translateBox)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.translateLayout = QtWidgets.QGridLayout()
        self.translateLayout.setObjectName("translateLayout")
        self.upBtn = QtWidgets.QPushButton(self.translateBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.upBtn.sizePolicy().hasHeightForWidth())
        self.upBtn.setSizePolicy(sizePolicy)
        self.upBtn.setMinimumSize(QtCore.QSize(30, 30))
        self.upBtn.setMaximumSize(QtCore.QSize(30, 30))
        self.upBtn.setObjectName("upBtn")
        self.translateLayout.addWidget(self.upBtn, 0, 1, 1, 1)
        self.rightBtn = QtWidgets.QPushButton(self.translateBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.rightBtn.sizePolicy().hasHeightForWidth())
        self.rightBtn.setSizePolicy(sizePolicy)
        self.rightBtn.setMinimumSize(QtCore.QSize(30, 30))
        self.rightBtn.setMaximumSize(QtCore.QSize(30, 30))
        self.rightBtn.setObjectName("rightBtn")
        self.translateLayout.addWidget(self.rightBtn, 1, 2, 1, 1)
        self.downBtn = QtWidgets.QPushButton(self.translateBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.downBtn.sizePolicy().hasHeightForWidth())
        self.downBtn.setSizePolicy(sizePolicy)
        self.downBtn.setMinimumSize(QtCore.QSize(30, 30))
        self.downBtn.setMaximumSize(QtCore.QSize(30, 30))
        self.downBtn.setObjectName("downBtn")
        self.translateLayout.addWidget(self.downBtn, 1, 1, 1, 1)
        self.fromBtn = QtWidgets.QPushButton(self.translateBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.fromBtn.sizePolicy().hasHeightForWidth())
        self.fromBtn.setSizePolicy(sizePolicy)
        self.fromBtn.setMinimumSize(QtCore.QSize(30, 30))
        self.fromBtn.setMaximumSize(QtCore.QSize(30, 30))
        self.fromBtn.setObjectName("fromBtn")
        self.translateLayout.addWidget(self.fromBtn, 0, 2, 1, 1)
        self.leftBtn = QtWidgets.QPushButton(self.translateBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.leftBtn.sizePolicy().hasHeightForWidth())
        self.leftBtn.setSizePolicy(sizePolicy)
        self.leftBtn.setMinimumSize(QtCore.QSize(30, 30))
        self.leftBtn.setMaximumSize(QtCore.QSize(30, 30))
        self.leftBtn.setObjectName("leftBtn")
        self.translateLayout.addWidget(self.leftBtn, 1, 0, 1, 1)
        self.toBtn = QtWidgets.QPushButton(self.translateBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.toBtn.sizePolicy().hasHeightForWidth())
        self.toBtn.setSizePolicy(sizePolicy)
        self.toBtn.setMinimumSize(QtCore.QSize(30, 30))
        self.toBtn.setMaximumSize(QtCore.QSize(30, 30))
        self.toBtn.setObjectName("toBtn")
        self.translateLayout.addWidget(self.toBtn, 0, 0, 1, 1)
        self.gridLayout_2.addLayout(self.translateLayout, 0, 0, 2, 1)
        self.verticalLayout.addWidget(self.translateBox)
        self.turnBox = QtWidgets.QGroupBox(self.centralwidget)
        self.turnBox.setObjectName("turnBox")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.turnBox)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.turnLayout = QtWidgets.QGridLayout()
        self.turnLayout.setObjectName("turnLayout")
        self.yUpTurnBtn = QtWidgets.QPushButton(self.turnBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.yUpTurnBtn.sizePolicy().hasHeightForWidth())
        self.yUpTurnBtn.setSizePolicy(sizePolicy)
        self.yUpTurnBtn.setMinimumSize(QtCore.QSize(30, 30))
        self.yUpTurnBtn.setMaximumSize(QtCore.QSize(30, 30))
        self.yUpTurnBtn.setObjectName("yUpTurnBtn")
        self.turnLayout.addWidget(self.yUpTurnBtn, 0, 1, 1, 1)
        self.xRightTurnBtn = QtWidgets.QPushButton(self.turnBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.xRightTurnBtn.sizePolicy().hasHeightForWidth())
        self.xRightTurnBtn.setSizePolicy(sizePolicy)
        self.xRightTurnBtn.setMinimumSize(QtCore.QSize(30, 30))
        self.xRightTurnBtn.setMaximumSize(QtCore.QSize(30, 30))
        self.xRightTurnBtn.setObjectName("xRightTurnBtn")
        self.turnLayout.addWidget(self.xRightTurnBtn, 1, 2, 1, 1)
        self.yDownTurnBtn = QtWidgets.QPushButton(self.turnBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.yDownTurnBtn.sizePolicy().hasHeightForWidth())
        self.yDownTurnBtn.setSizePolicy(sizePolicy)
        self.yDownTurnBtn.setMinimumSize(QtCore.QSize(30, 30))
        self.yDownTurnBtn.setMaximumSize(QtCore.QSize(30, 30))
        self.yDownTurnBtn.setObjectName("yDownTurnBtn")
        self.turnLayout.addWidget(self.yDownTurnBtn, 1, 1, 1, 1)
        self.zLeftTurnBtn = QtWidgets.QPushButton(self.turnBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.zLeftTurnBtn.sizePolicy().hasHeightForWidth())
        self.zLeftTurnBtn.setSizePolicy(sizePolicy)
        self.zLeftTurnBtn.setMinimumSize(QtCore.QSize(30, 30))
        self.zLeftTurnBtn.setMaximumSize(QtCore.QSize(30, 30))
        self.zLeftTurnBtn.setObjectName("zLeftTurnBtn")
        self.turnLayout.addWidget(self.zLeftTurnBtn, 0, 2, 1, 1)
        self.xLeftTurnBtn = QtWidgets.QPushButton(self.turnBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.xLeftTurnBtn.sizePolicy().hasHeightForWidth())
        self.xLeftTurnBtn.setSizePolicy(sizePolicy)
        self.xLeftTurnBtn.setMinimumSize(QtCore.QSize(30, 30))
        self.xLeftTurnBtn.setMaximumSize(QtCore.QSize(30, 30))
        self.xLeftTurnBtn.setObjectName("xLeftTurnBtn")
        self.turnLayout.addWidget(self.xLeftTurnBtn, 1, 0, 1, 1)
        self.zRightTurnBtn = QtWidgets.QPushButton(self.turnBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.zRightTurnBtn.sizePolicy().hasHeightForWidth())
        self.zRightTurnBtn.setSizePolicy(sizePolicy)
        self.zRightTurnBtn.setMinimumSize(QtCore.QSize(30, 30))
        self.zRightTurnBtn.setMaximumSize(QtCore.QSize(30, 30))
        self.zRightTurnBtn.setObjectName("zRightTurnBtn")
        self.turnLayout.addWidget(self.zRightTurnBtn, 0, 0, 1, 1)
        self.gridLayout_3.addLayout(self.turnLayout, 0, 0, 2, 1)
        self.verticalLayout.addWidget(self.turnBox)
        self.colorBtn = QtWidgets.QPushButton(self.centralwidget)
        self.colorBtn.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.colorBtn.setText("")
        self.colorBtn.setObjectName("colorBtn")
        self.verticalLayout.addWidget(self.colorBtn)
        self.gridLayout_4.addLayout(self.verticalLayout, 0, 0, 1, 1)
        self.GL = myGL(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.GL.sizePolicy().hasHeightForWidth())
        self.GL.setSizePolicy(sizePolicy)
        self.GL.setObjectName("GL")
        self.gridLayout_4.addWidget(self.GL, 0, 1, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "ClothSim"))
        self.loadBox.setTitle(_translate("MainWindow", "Модель"))
        self.loadModelBtn.setText(_translate("MainWindow", "Загрузить"))
        self.deleteModelBtn.setText(_translate("MainWindow", "  Удалить  "))
        self.scaleBox.setTitle(_translate("MainWindow", "Масштаб"))
        self.minusBtn.setText(_translate("MainWindow", "-"))
        self.plusBtn.setText(_translate("MainWindow", "+"))
        self.translateBox.setTitle(_translate("MainWindow", "Перемещение"))
        self.upBtn.setText(_translate("MainWindow", "↑"))
        self.rightBtn.setText(_translate("MainWindow", "→"))
        self.downBtn.setText(_translate("MainWindow", "↓"))
        self.fromBtn.setText(_translate("MainWindow", "↗"))
        self.leftBtn.setText(_translate("MainWindow", "←"))
        self.toBtn.setText(_translate("MainWindow", "↙"))
        self.turnBox.setTitle(_translate("MainWindow", "Поворот"))
        self.yUpTurnBtn.setText(_translate("MainWindow", "↑"))
        self.xRightTurnBtn.setText(_translate("MainWindow", "→"))
        self.yDownTurnBtn.setText(_translate("MainWindow", "↓"))
        self.zLeftTurnBtn.setText(_translate("MainWindow", "⭯"))
        self.xLeftTurnBtn.setText(_translate("MainWindow", "←"))
        self.zRightTurnBtn.setText(_translate("MainWindow", "⭮"))
from graphic.mygl import myGL
