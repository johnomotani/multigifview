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
        MainWindow.resize(793, 626)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(0, 560, 251, 26))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.play_button = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.play_button.setText("")
        icon = QtGui.QIcon.fromTheme("media-playback-start")
        self.play_button.setIcon(icon)
        self.play_button.setObjectName("play_button")
        self.horizontalLayout.addWidget(self.play_button)
        self.previous_button = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.previous_button.setText("")
        icon = QtGui.QIcon.fromTheme("media-skip-backward")
        self.previous_button.setIcon(icon)
        self.previous_button.setObjectName("previous_button")
        self.horizontalLayout.addWidget(self.previous_button)
        self.next_button = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.next_button.setText("")
        icon = QtGui.QIcon.fromTheme("media-skip-forward")
        self.next_button.setIcon(icon)
        self.next_button.setObjectName("next_button")
        self.horizontalLayout.addWidget(self.next_button)
        self.gif_widget = QtWidgets.QLabel(self.centralwidget)
        self.gif_widget.setGeometry(QtCore.QRect(0, 0, 791, 561))
        self.gif_widget.setText("")
        self.gif_widget.setObjectName("gif_widget")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 793, 20))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "multigifview"))
        self.play_button.setShortcut(_translate("MainWindow", "Space"))
        self.previous_button.setShortcut(_translate("MainWindow", "P"))
        self.next_button.setShortcut(_translate("MainWindow", "N"))
