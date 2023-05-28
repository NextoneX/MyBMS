# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui/BR_widget.ui'
#
# Created by: PyQt5 UI code generator 5.12.3
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_BR_widget(object):
    def setupUi(self, BR_widget):
        BR_widget.setObjectName("BR_widget")
        BR_widget.resize(595, 344)
        self.ReturnButton_2 = QtWidgets.QCommandLinkButton(BR_widget)
        self.ReturnButton_2.setGeometry(QtCore.QRect(480, 10, 101, 48))
        self.ReturnButton_2.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.ReturnButton_2.setObjectName("ReturnButton_2")
        self.Card_no = QtWidgets.QLabel(BR_widget)
        self.Card_no.setGeometry(QtCore.QRect(60, 20, 91, 21))
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setPointSize(11)
        self.Card_no.setFont(font)
        self.Card_no.setObjectName("Card_no")
        self.bno_input = QtWidgets.QTextEdit(BR_widget)
        self.bno_input.setGeometry(QtCore.QRect(220, 210, 241, 31))
        self.bno_input.setObjectName("bno_input")
        self.borrowed_output = QtWidgets.QLabel(BR_widget)
        self.borrowed_output.setGeometry(QtCore.QRect(220, 70, 241, 121))
        self.borrowed_output.setMouseTracking(False)
        self.borrowed_output.setTabletTracking(False)
        self.borrowed_output.setAcceptDrops(False)
        self.borrowed_output.setAutoFillBackground(False)
        self.borrowed_output.setText("")
        self.borrowed_output.setScaledContents(False)
        self.borrowed_output.setWordWrap(False)
        self.borrowed_output.setOpenExternalLinks(False)
        self.borrowed_output.setObjectName("borrowed_output")
        self.Book_no = QtWidgets.QLabel(BR_widget)
        self.Book_no.setGeometry(QtCore.QRect(60, 210, 91, 21))
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setPointSize(11)
        self.Book_no.setFont(font)
        self.Book_no.setObjectName("Book_no")
        self.cno_input = QtWidgets.QTextEdit(BR_widget)
        self.cno_input.setGeometry(QtCore.QRect(220, 20, 241, 31))
        self.cno_input.setObjectName("cno_input")
        self.ReturnButton = QtWidgets.QPushButton(BR_widget)
        self.ReturnButton.setGeometry(QtCore.QRect(320, 280, 151, 51))
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setPointSize(11)
        self.ReturnButton.setFont(font)
        self.ReturnButton.setObjectName("ReturnButton")
        self.Book_borrowed = QtWidgets.QLabel(BR_widget)
        self.Book_borrowed.setGeometry(QtCore.QRect(60, 70, 151, 21))
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setPointSize(11)
        self.Book_borrowed.setFont(font)
        self.Book_borrowed.setObjectName("Book_borrowed")
        self.BorrowButton = QtWidgets.QPushButton(BR_widget)
        self.BorrowButton.setGeometry(QtCore.QRect(110, 280, 151, 51))
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setPointSize(11)
        self.BorrowButton.setFont(font)
        self.BorrowButton.setCheckable(False)
        self.BorrowButton.setChecked(False)
        self.BorrowButton.setAutoDefault(False)
        self.BorrowButton.setDefault(False)
        self.BorrowButton.setFlat(False)
        self.BorrowButton.setObjectName("BorrowButton")

        self.retranslateUi(BR_widget)
        QtCore.QMetaObject.connectSlotsByName(BR_widget)

    def retranslateUi(self, BR_widget):
        _translate = QtCore.QCoreApplication.translate
        BR_widget.setWindowTitle(_translate("BR_widget", "BR_widget"))
        self.ReturnButton_2.setText(_translate("BR_widget", "Return"))
        self.Card_no.setText(_translate("BR_widget", "Card_no:"))
        self.Book_no.setText(_translate("BR_widget", "Book_no:"))
        self.ReturnButton.setText(_translate("BR_widget", "Return"))
        self.Book_borrowed.setText(_translate("BR_widget", "Borrowed books:"))
        self.BorrowButton.setText(_translate("BR_widget", "Borrow"))
