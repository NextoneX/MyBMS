# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui/card_manage_widget.ui'
#
# Created by: PyQt5 UI code generator 5.12.3
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_card_manage_widget(object):
    def setupUi(self, card_manage_widget):
        card_manage_widget.setObjectName("card_manage_widget")
        card_manage_widget.resize(650, 238)
        self.Card_no = QtWidgets.QLabel(card_manage_widget)
        self.Card_no.setGeometry(QtCore.QRect(100, 80, 91, 21))
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setPointSize(11)
        self.Card_no.setFont(font)
        self.Card_no.setObjectName("Card_no")
        self.DeleteButton = QtWidgets.QPushButton(card_manage_widget)
        self.DeleteButton.setGeometry(QtCore.QRect(360, 150, 151, 51))
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setPointSize(11)
        self.DeleteButton.setFont(font)
        self.DeleteButton.setObjectName("DeleteButton")
        self.ReturnButton = QtWidgets.QCommandLinkButton(card_manage_widget)
        self.ReturnButton.setGeometry(QtCore.QRect(530, 10, 101, 48))
        self.ReturnButton.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.ReturnButton.setObjectName("ReturnButton")
        self.AddButton = QtWidgets.QPushButton(card_manage_widget)
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
        self.cno_input = QtWidgets.QTextEdit(card_manage_widget)
        self.cno_input.setGeometry(QtCore.QRect(260, 80, 241, 31))
        self.cno_input.setObjectName("cno_input")

        self.retranslateUi(card_manage_widget)
        QtCore.QMetaObject.connectSlotsByName(card_manage_widget)

    def retranslateUi(self, card_manage_widget):
        _translate = QtCore.QCoreApplication.translate
        card_manage_widget.setWindowTitle(_translate("card_manage_widget", "card_manage_widget"))
        self.Card_no.setText(_translate("card_manage_widget", "Card_no:"))
        self.DeleteButton.setText(_translate("card_manage_widget", "Delete"))
        self.ReturnButton.setText(_translate("card_manage_widget", "Return"))
        self.AddButton.setText(_translate("card_manage_widget", "Add"))
