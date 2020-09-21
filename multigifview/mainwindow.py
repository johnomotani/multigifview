# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainwindow.ui'
#
# Created by: PyQt5 UI code generator 5.12.3
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(230, 134)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.centralwidget.sizePolicy().hasHeightForWidth())
        self.centralwidget.setSizePolicy(sizePolicy)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout_main = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout_main.setObjectName("verticalLayout_main")
        self.gif_layout = QtWidgets.QHBoxLayout()
        self.gif_layout.setObjectName("gif_layout")
        self.column0 = QtWidgets.QVBoxLayout()
        self.column0.setObjectName("column0")
        spacerItem = QtWidgets.QSpacerItem(0, 0, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.column0.addItem(spacerItem)
        self.gif_layout.addLayout(self.column0)
        self.verticalLayout_main.addLayout(self.gif_layout)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setSizeConstraint(QtWidgets.QLayout.SetFixedSize)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.beginning_button = QtWidgets.QPushButton(self.centralwidget)
        self.beginning_button.setText("")
        icon = QtGui.QIcon.fromTheme("media-skip-backward")
        self.beginning_button.setIcon(icon)
        self.beginning_button.setObjectName("beginning_button")
        self.horizontalLayout.addWidget(self.beginning_button)
        self.previous_button = QtWidgets.QPushButton(self.centralwidget)
        self.previous_button.setText("")
        icon = QtGui.QIcon.fromTheme("media-seek-backward")
        self.previous_button.setIcon(icon)
        self.previous_button.setObjectName("previous_button")
        self.horizontalLayout.addWidget(self.previous_button)
        self.play_button = QtWidgets.QPushButton(self.centralwidget)
        self.play_button.setText("")
        icon = QtGui.QIcon.fromTheme("media-playback-start")
        self.play_button.setIcon(icon)
        self.play_button.setObjectName("play_button")
        self.horizontalLayout.addWidget(self.play_button)
        self.next_button = QtWidgets.QPushButton(self.centralwidget)
        self.next_button.setText("")
        icon = QtGui.QIcon.fromTheme("media-seek-forward")
        self.next_button.setIcon(icon)
        self.next_button.setObjectName("next_button")
        self.horizontalLayout.addWidget(self.next_button)
        self.end_button = QtWidgets.QPushButton(self.centralwidget)
        self.end_button.setText("")
        icon = QtGui.QIcon.fromTheme("media-skip-forward")
        self.end_button.setIcon(icon)
        self.end_button.setObjectName("end_button")
        self.horizontalLayout.addWidget(self.end_button)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem1)
        self.verticalLayout_main.addLayout(self.horizontalLayout)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 230, 20))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "multigifview"))
        self.beginning_button.setShortcut(_translate("MainWindow", "B"))
        self.previous_button.setShortcut(_translate("MainWindow", "P"))
        self.play_button.setShortcut(_translate("MainWindow", "Space"))
        self.next_button.setShortcut(_translate("MainWindow", "N"))
        self.end_button.setShortcut(_translate("MainWindow", "E"))
