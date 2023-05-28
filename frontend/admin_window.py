# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui/admin_window.ui'
#
# Created by: PyQt5 UI code generator 5.12.3
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_admin_window(object):
    def setupUi(self, admin_window):
        admin_window.setObjectName("admin_window")
        admin_window.resize(601, 340)
        self.centralwidget = QtWidgets.QWidget(admin_window)
        self.centralwidget.setObjectName("centralwidget")
        self.BookRegButton = QtWidgets.QPushButton(self.centralwidget)
        self.BookRegButton.setGeometry(QtCore.QRect(120, 30, 261, 41))
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setPointSize(11)
        self.BookRegButton.setFont(font)
        self.BookRegButton.setObjectName("BookRegButton")
        self.BookOpButton = QtWidgets.QPushButton(self.centralwidget)
        self.BookOpButton.setGeometry(QtCore.QRect(120, 90, 261, 41))
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setPointSize(11)
        self.BookOpButton.setFont(font)
        self.BookOpButton.setObjectName("BookOpButton")
        self.BookSearchButton = QtWidgets.QPushButton(self.centralwidget)
        self.BookSearchButton.setGeometry(QtCore.QRect(120, 150, 261, 41))
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setPointSize(11)
        self.BookSearchButton.setFont(font)
        self.BookSearchButton.setObjectName("BookSearchButton")
        self.CardManageButton = QtWidgets.QPushButton(self.centralwidget)
        self.CardManageButton.setGeometry(QtCore.QRect(120, 210, 261, 41))
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setPointSize(11)
        self.CardManageButton.setFont(font)
        self.CardManageButton.setObjectName("CardManageButton")
        admin_window.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(admin_window)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 601, 26))
        self.menubar.setObjectName("menubar")
        admin_window.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(admin_window)
        self.statusbar.setObjectName("statusbar")
        admin_window.setStatusBar(self.statusbar)

        self.retranslateUi(admin_window)
        QtCore.QMetaObject.connectSlotsByName(admin_window)

    def retranslateUi(self, admin_window):
        _translate = QtCore.QCoreApplication.translate
        admin_window.setWindowTitle(_translate("admin_window", "admin_window"))
        self.BookRegButton.setText(_translate("admin_window", "Book registration"))
        self.BookOpButton.setText(_translate("admin_window", "Borrow/Return operation"))
        self.BookSearchButton.setText(_translate("admin_window", "Search book"))
        self.CardManageButton.setText(_translate("admin_window", "Library card management"))
