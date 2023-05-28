# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui/card_manage_window.ui'
#
# Created by: PyQt5 UI code generator 5.12.3
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_card_manage_window(object):
    def setupUi(self, card_manage_window):
        card_manage_window.setObjectName("card_manage_window")
        card_manage_window.resize(641, 287)
        self.centralwidget = QtWidgets.QWidget(card_manage_window)
        self.centralwidget.setObjectName("centralwidget")
        self.AddButton = QtWidgets.QPushButton(self.centralwidget)
        self.AddButton.setGeometry(QtCore.QRect(150, 150, 151, 51))
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setPointSize(11)
        self.AddButton.setFont(font)
        self.AddButton.setCheckable(False)
        self.AddButton.setChecked(False)
        self.AddButton.setAutoDefault(False)
        self.AddButton.setDefault(False)
        self.AddButton.setFlat(False)
        self.AddButton.setObjectName("AddButton")
        self.Card_no = QtWidgets.QLabel(self.centralwidget)
        self.Card_no.setGeometry(QtCore.QRect(100, 80, 91, 21))
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setPointSize(11)
        self.Card_no.setFont(font)
        self.Card_no.setObjectName("Card_no")
        self.cno_input = QtWidgets.QTextEdit(self.centralwidget)
        self.cno_input.setGeometry(QtCore.QRect(260, 80, 241, 31))
        self.cno_input.setObjectName("cno_input")
        self.DeleteButton = QtWidgets.QPushButton(self.centralwidget)
        self.DeleteButton.setGeometry(QtCore.QRect(360, 150, 151, 51))
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setPointSize(11)
        self.DeleteButton.setFont(font)
        self.DeleteButton.setObjectName("DeleteButton")
        self.ReturnButton_2 = QtWidgets.QCommandLinkButton(self.centralwidget)
        self.ReturnButton_2.setGeometry(QtCore.QRect(530, 10, 101, 48))
        self.ReturnButton_2.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.ReturnButton_2.setObjectName("ReturnButton_2")
        card_manage_window.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(card_manage_window)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 641, 26))
        self.menubar.setObjectName("menubar")
        card_manage_window.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(card_manage_window)
        self.statusbar.setObjectName("statusbar")
        card_manage_window.setStatusBar(self.statusbar)

        self.retranslateUi(card_manage_window)
        QtCore.QMetaObject.connectSlotsByName(card_manage_window)

    def retranslateUi(self, card_manage_window):
        _translate = QtCore.QCoreApplication.translate
        card_manage_window.setWindowTitle(_translate("card_manage_window", "card_manage_window"))
        self.AddButton.setText(_translate("card_manage_window", "Add"))
        self.Card_no.setText(_translate("card_manage_window", "Card_no:"))
        self.DeleteButton.setText(_translate("card_manage_window", "Delete"))
        self.ReturnButton_2.setText(_translate("card_manage_window", "Return"))
