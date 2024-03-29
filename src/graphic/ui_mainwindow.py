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
        MainWindow.resize(1211, 758)
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
        self.modeLyt = QtWidgets.QVBoxLayout()
        self.modeLyt.setObjectName("modeLyt")
        self.modeBox = QtWidgets.QGroupBox(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.modeBox.sizePolicy().hasHeightForWidth())
        self.modeBox.setSizePolicy(sizePolicy)
        self.modeBox.setObjectName("modeBox")
        self.gridLayout_5 = QtWidgets.QGridLayout(self.modeBox)
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.tshirtRBtn = QtWidgets.QRadioButton(self.modeBox)
        self.tshirtRBtn.setChecked(True)
        self.tshirtRBtn.setObjectName("tshirtRBtn")
        self.gridLayout_5.addWidget(self.tshirtRBtn, 0, 0, 1, 1)
        self.sizeSB = QtWidgets.QSpinBox(self.modeBox)
        self.sizeSB.setEnabled(False)
        self.sizeSB.setMinimum(2)
        self.sizeSB.setObjectName("sizeSB")
        self.gridLayout_5.addWidget(self.sizeSB, 3, 0, 1, 1)
        self.sizeLbl = QtWidgets.QLabel(self.modeBox)
        self.sizeLbl.setObjectName("sizeLbl")
        self.gridLayout_5.addWidget(self.sizeLbl, 2, 0, 1, 1)
        self.clothRbtn = QtWidgets.QRadioButton(self.modeBox)
        self.clothRbtn.setChecked(False)
        self.clothRbtn.setObjectName("clothRbtn")
        self.gridLayout_5.addWidget(self.clothRbtn, 1, 0, 1, 1)
        self.fpsLbl = QtWidgets.QLabel(self.modeBox)
        self.fpsLbl.setObjectName("fpsLbl")
        self.gridLayout_5.addWidget(self.fpsLbl, 4, 0, 1, 1)
        self.modeLyt.addWidget(self.modeBox)
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
        self.minusBtn.setMaximumSize(QtCore.QSize(30, 30))
        self.minusBtn.setObjectName("minusBtn")
        self.horizontalLayout.addWidget(self.minusBtn)
        self.plusBtn = QtWidgets.QPushButton(self.scaleBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.plusBtn.sizePolicy().hasHeightForWidth())
        self.plusBtn.setSizePolicy(sizePolicy)
        self.plusBtn.setMaximumSize(QtCore.QSize(30, 30))
        self.plusBtn.setObjectName("plusBtn")
        self.horizontalLayout.addWidget(self.plusBtn)
        self.modeLyt.addWidget(self.scaleBox)
        self.translateBox = QtWidgets.QGroupBox(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.translateBox.sizePolicy().hasHeightForWidth())
        self.translateBox.setSizePolicy(sizePolicy)
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
        self.modeLyt.addWidget(self.translateBox)
        self.turnBox = QtWidgets.QGroupBox(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.turnBox.sizePolicy().hasHeightForWidth())
        self.turnBox.setSizePolicy(sizePolicy)
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
        self.gridLayout_3.addLayout(self.turnLayout, 0, 0, 2, 1)
        self.modeLyt.addWidget(self.turnBox)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.modeLyt.addItem(spacerItem)
        self.gridLayout_4.addLayout(self.modeLyt, 3, 2, 1, 1)
        self.paramLyt = QtWidgets.QVBoxLayout()
        self.paramLyt.setObjectName("paramLyt")
        self.clothBox = QtWidgets.QGroupBox(self.centralwidget)
        self.clothBox.setObjectName("clothBox")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.clothBox)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.colorBtn = QtWidgets.QPushButton(self.clothBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.colorBtn.sizePolicy().hasHeightForWidth())
        self.colorBtn.setSizePolicy(sizePolicy)
        self.colorBtn.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.colorBtn.setObjectName("colorBtn")
        self.verticalLayout_5.addWidget(self.colorBtn)
        self.siffLbl = QtWidgets.QLabel(self.clothBox)
        self.siffLbl.setObjectName("siffLbl")
        self.verticalLayout_5.addWidget(self.siffLbl)
        self.stifDSB = QtWidgets.QDoubleSpinBox(self.clothBox)
        self.stifDSB.setPrefix("")
        self.stifDSB.setSuffix(" · 10⁴ Н/м")
        self.stifDSB.setMinimum(0.1)
        self.stifDSB.setMaximum(2.5)
        self.stifDSB.setSingleStep(0.1)
        self.stifDSB.setProperty("value", 1.0)
        self.stifDSB.setObjectName("stifDSB")
        self.verticalLayout_5.addWidget(self.stifDSB)
        self.massLbl = QtWidgets.QLabel(self.clothBox)
        self.massLbl.setObjectName("massLbl")
        self.verticalLayout_5.addWidget(self.massLbl)
        self.massDSB = QtWidgets.QDoubleSpinBox(self.clothBox)
        self.massDSB.setDecimals(3)
        self.massDSB.setMinimum(0.001)
        self.massDSB.setMaximum(1.0)
        self.massDSB.setSingleStep(0.01)
        self.massDSB.setProperty("value", 0.01)
        self.massDSB.setObjectName("massDSB")
        self.verticalLayout_5.addWidget(self.massDSB)
        self.paramLyt.addWidget(self.clothBox)
        self.physBox = QtWidgets.QGroupBox(self.centralwidget)
        self.physBox.setObjectName("physBox")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.physBox)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.windChBox = QtWidgets.QCheckBox(self.physBox)
        self.windChBox.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.windChBox.setAutoFillBackground(False)
        self.windChBox.setChecked(True)
        self.windChBox.setTristate(False)
        self.windChBox.setObjectName("windChBox")
        self.verticalLayout_2.addWidget(self.windChBox)
        self.gravLbl = QtWidgets.QLabel(self.physBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.gravLbl.sizePolicy().hasHeightForWidth())
        self.gravLbl.setSizePolicy(sizePolicy)
        self.gravLbl.setObjectName("gravLbl")
        self.verticalLayout_2.addWidget(self.gravLbl)
        self.gravDSB = QtWidgets.QDoubleSpinBox(self.physBox)
        self.gravDSB.setMinimum(1.0)
        self.gravDSB.setMaximum(20.0)
        self.gravDSB.setSingleStep(0.1)
        self.gravDSB.setProperty("value", 9.81)
        self.gravDSB.setObjectName("gravDSB")
        self.verticalLayout_2.addWidget(self.gravDSB)
        self.paramLyt.addWidget(self.physBox)
        self.lightBox = QtWidgets.QGroupBox(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lightBox.sizePolicy().hasHeightForWidth())
        self.lightBox.setSizePolicy(sizePolicy)
        self.lightBox.setObjectName("lightBox")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.lightBox)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.ambLbl = QtWidgets.QLabel(self.lightBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.ambLbl.sizePolicy().hasHeightForWidth())
        self.ambLbl.setSizePolicy(sizePolicy)
        self.ambLbl.setObjectName("ambLbl")
        self.verticalLayout_3.addWidget(self.ambLbl)
        self.ambDSB = QtWidgets.QDoubleSpinBox(self.lightBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.ambDSB.sizePolicy().hasHeightForWidth())
        self.ambDSB.setSizePolicy(sizePolicy)
        self.ambDSB.setMinimum(0.01)
        self.ambDSB.setMaximum(1.0)
        self.ambDSB.setSingleStep(0.1)
        self.ambDSB.setProperty("value", 0.3)
        self.ambDSB.setObjectName("ambDSB")
        self.verticalLayout_3.addWidget(self.ambDSB)
        self.diffLbl = QtWidgets.QLabel(self.lightBox)
        self.diffLbl.setObjectName("diffLbl")
        self.verticalLayout_3.addWidget(self.diffLbl)
        self.diffDSB = QtWidgets.QDoubleSpinBox(self.lightBox)
        self.diffDSB.setMinimum(0.01)
        self.diffDSB.setMaximum(1.0)
        self.diffDSB.setSingleStep(0.1)
        self.diffDSB.setProperty("value", 0.55)
        self.diffDSB.setObjectName("diffDSB")
        self.verticalLayout_3.addWidget(self.diffDSB)
        self.specLbl = QtWidgets.QLabel(self.lightBox)
        self.specLbl.setObjectName("specLbl")
        self.verticalLayout_3.addWidget(self.specLbl)
        self.specDSB = QtWidgets.QDoubleSpinBox(self.lightBox)
        self.specDSB.setDecimals(3)
        self.specDSB.setMinimum(0.001)
        self.specDSB.setMaximum(1.0)
        self.specDSB.setSingleStep(0.01)
        self.specDSB.setProperty("value", 0.01)
        self.specDSB.setObjectName("specDSB")
        self.verticalLayout_3.addWidget(self.specDSB)
        self.paramLyt.addWidget(self.lightBox)
        self.gridLayout_4.addLayout(self.paramLyt, 3, 0, 1, 1)
        self.GL = myGL(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.GL.sizePolicy().hasHeightForWidth())
        self.GL.setSizePolicy(sizePolicy)
        self.GL.setObjectName("GL")
        self.gridLayout_4.addWidget(self.GL, 3, 1, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "ClothSim"))
        self.modeBox.setTitle(_translate("MainWindow", "Режим"))
        self.tshirtRBtn.setText(_translate("MainWindow", "Футболка"))
        self.sizeLbl.setText(_translate("MainWindow", "Размер:"))
        self.clothRbtn.setText(_translate("MainWindow", "Ткань"))
        self.fpsLbl.setText(_translate("MainWindow", "FPS:"))
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
        self.xLeftTurnBtn.setText(_translate("MainWindow", "←"))
        self.clothBox.setTitle(_translate("MainWindow", "Ткань"))
        self.colorBtn.setText(_translate("MainWindow", "Цвет"))
        self.siffLbl.setText(_translate("MainWindow", "Жесткость:"))
        self.massLbl.setText(_translate("MainWindow", "Масса:"))
        self.massDSB.setSuffix(_translate("MainWindow", " г"))
        self.physBox.setTitle(_translate("MainWindow", "Физика"))
        self.windChBox.setText(_translate("MainWindow", "Ветер"))
        self.gravLbl.setText(_translate("MainWindow", "Гравитация:"))
        self.gravDSB.setSuffix(_translate("MainWindow", " м/c²"))
        self.lightBox.setTitle(_translate("MainWindow", "Освещение"))
        self.ambLbl.setText(_translate("MainWindow", "Среды:"))
        self.diffLbl.setText(_translate("MainWindow", "Диффузное:"))
        self.specLbl.setText(_translate("MainWindow", "Отражения:"))
from graphic.mygl import myGL
