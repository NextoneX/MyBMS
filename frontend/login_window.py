# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui/login_window.ui'
#
# Created by: PyQt5 UI code generator 5.12.3
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_login_window(object):
    def setupUi(self, login_window):
        login_window.setObjectName("login_window")
        login_window.resize(546, 438)
        self.centralwidget = QtWidgets.QWidget(login_window)
        self.centralwidget.setObjectName("centralwidget")
        self.Login_no = QtWidgets.QLabel(self.centralwidget)
        self.Login_no.setGeometry(QtCore.QRect(70, 140, 121, 21))
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setPointSize(11)
        self.Login_no.setFont(font)
        self.Login_no.setObjectName("Login_no")
        self.title = QtWidgets.QLabel(self.centralwidget)
        self.title.setGeometry(QtCore.QRect(90, 10, 381, 71))
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setPointSize(24)
        self.title.setFont(font)
        self.title.setObjectName("title")
        self.ano_input = QtWidgets.QTextEdit(self.centralwidget)
        self.ano_input.setGeometry(QtCore.QRect(240, 130, 211, 31))
        self.ano_input.setObjectName("ano_input")
        self.password_input = QtWidgets.QTextEdit(self.centralwidget)
        self.password_input.setGeometry(QtCore.QRect(240, 190, 211, 31))
        self.password_input.setObjectName("password_input")
        self.Login_password = QtWidgets.QLabel(self.centralwidget)
        self.Login_password.setGeometry(QtCore.QRect(70, 190, 151, 31))
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setPointSize(11)
        self.Login_password.setFont(font)
        self.Login_password.setObjectName("Login_password")
        self.LoginButton = QtWidgets.QPushButton(self.centralwidget)
        self.LoginButton.setGeometry(QtCore.QRect(210, 260, 151, 51))
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setPointSize(11)
        self.LoginButton.setFont(font)
        self.LoginButton.setObjectName("LoginButton")
        self.Non_admin_login = QtWidgets.QCommandLinkButton(self.centralwidget)
        self.Non_admin_login.setGeometry(QtCore.QRect(340, 340, 201, 41))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(9)
        self.Non_admin_login.setFont(font)
        self.Non_admin_login.setObjectName("Non_admin_login")
        login_window.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(login_window)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 546, 26))
        self.menubar.setObjectName("menubar")
        login_window.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(login_window)
        self.statusbar.setObjectName("statusbar")
        login_window.setStatusBar(self.statusbar)

        self.retranslateUi(login_window)
        QtCore.QMetaObject.connectSlotsByName(login_window)

    def retranslateUi(self, login_window):
        _translate = QtCore.QCoreApplication.translate
        login_window.setWindowTitle(_translate("login_window", "login_window"))
        self.Login_no.setText(_translate("login_window", "Login_no:"))
        self.title.setText(_translate("login_window", "Welcome to MyBMS!"))
        self.Login_password.setText(_translate("login_window", "Login_password:"))
        self.LoginButton.setText(_translate("login_window", "Login"))
        self.Non_admin_login.setText(_translate("login_window", "Non-administrator login"))
