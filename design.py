# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/home/mq/Designs/gdwngrade/mainwindow.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(312, 172)
        self.centralWidget = QtWidgets.QWidget(MainWindow)
        self.centralWidget.setObjectName("centralWidget")
        self.label = QtWidgets.QLabel(self.centralWidget)
        self.label.setGeometry(QtCore.QRect(10, 10, 241, 17))
        self.label.setObjectName("label")
        self.from_le = QtWidgets.QLineEdit(self.centralWidget)
        self.from_le.setGeometry(QtCore.QRect(40, 40, 71, 21))
        self.from_le.setText("")
        self.from_le.setObjectName("from_le")
        self.search_button = QtWidgets.QPushButton(self.centralWidget)
        self.search_button.setGeometry(QtCore.QRect(10, 80, 291, 27))
        self.search_button.setObjectName("search_button")
        self.label_2 = QtWidgets.QLabel(self.centralWidget)
        self.label_2.setGeometry(QtCore.QRect(20, 40, 21, 17))
        self.label_2.setObjectName("label_2")
        self.till_le = QtWidgets.QLineEdit(self.centralWidget)
        self.till_le.setGeometry(QtCore.QRect(220, 40, 71, 21))
        self.till_le.setText("")
        self.till_le.setObjectName("till_le")
        self.label_3 = QtWidgets.QLabel(self.centralWidget)
        self.label_3.setGeometry(QtCore.QRect(190, 40, 21, 17))
        self.label_3.setObjectName("label_3")
        self.progressBar = QtWidgets.QProgressBar(self.centralWidget)
        self.progressBar.setGeometry(QtCore.QRect(10, 80, 291, 27))
        self.progressBar.setProperty("value", 0)
        self.progressBar.setObjectName("progressBar")
        self.result_label = QtWidgets.QLabel(self.centralWidget)
        self.result_label.setGeometry(QtCore.QRect(13, 110, 281, 20))
        self.result_label.setText("")
        self.result_label.setAlignment(QtCore.Qt.AlignCenter)
        self.result_label.setObjectName("result_label")
        MainWindow.setCentralWidget(self.centralWidget)
        self.menuBar = QtWidgets.QMenuBar(MainWindow)
        self.menuBar.setGeometry(QtCore.QRect(0, 0, 312, 27))
        self.menuBar.setObjectName("menuBar")
        MainWindow.setMenuBar(self.menuBar)
        self.mainToolBar = QtWidgets.QToolBar(MainWindow)
        self.mainToolBar.setObjectName("mainToolBar")
        MainWindow.addToolBar(QtCore.Qt.TopToolBarArea, self.mainToolBar)
        self.statusBar = QtWidgets.QStatusBar(MainWindow)
        self.statusBar.setObjectName("statusBar")
        MainWindow.setStatusBar(self.statusBar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "gdwngrade"))
        self.label.setText(_translate("MainWindow", "Поиск минимума функции Растригина"))
        self.search_button.setText(_translate("MainWindow", "Поиск"))
        self.label_2.setText(_translate("MainWindow", "от"))
        self.label_3.setText(_translate("MainWindow", "до"))
