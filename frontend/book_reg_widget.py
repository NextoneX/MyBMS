# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui/book_reg_widget.ui'
#
# Created by: PyQt5 UI code generator 5.12.3
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_book_reg_widget(object):
    def setupUi(self, book_reg_widget):
        book_reg_widget.setObjectName("book_reg_widget")
        book_reg_widget.resize(599, 392)
        self.press_input = QtWidgets.QTextEdit(book_reg_widget)
        self.press_input.setGeometry(QtCore.QRect(200, 140, 241, 31))
        self.press_input.setObjectName("press_input")
        self.Price = QtWidgets.QLabel(book_reg_widget)
        self.Price.setGeometry(QtCore.QRect(60, 260, 91, 21))
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setPointSize(11)
        self.Price.setFont(font)
        self.Price.setObjectName("Price")
        self.year_input = QtWidgets.QTextEdit(book_reg_widget)
        self.year_input.setGeometry(QtCore.QRect(200, 180, 91, 31))
        self.year_input.setObjectName("year_input")
        self.category_input = QtWidgets.QTextEdit(book_reg_widget)
        self.category_input.setGeometry(QtCore.QRect(200, 60, 241, 31))
        self.category_input.setObjectName("category_input")
        self.price_input = QtWidgets.QTextEdit(book_reg_widget)
        self.price_input.setGeometry(QtCore.QRect(200, 260, 91, 31))
        self.price_input.setObjectName("price_input")
        self.Category = QtWidgets.QLabel(book_reg_widget)
        self.Category.setGeometry(QtCore.QRect(60, 60, 91, 21))
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setPointSize(11)
        self.Category.setFont(font)
        self.Category.setObjectName("Category")
        self.Year = QtWidgets.QLabel(book_reg_widget)
        self.Year.setGeometry(QtCore.QRect(60, 180, 91, 21))
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setPointSize(11)
        self.Year.setFont(font)
        self.Year.setObjectName("Year")
        self.Press = QtWidgets.QLabel(book_reg_widget)
        self.Press.setGeometry(QtCore.QRect(60, 140, 91, 21))
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setPointSize(11)
        self.Press.setFont(font)
        self.Press.setObjectName("Press")
        self.Author = QtWidgets.QLabel(book_reg_widget)
        self.Author.setGeometry(QtCore.QRect(60, 220, 91, 21))
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setPointSize(11)
        self.Author.setFont(font)
        self.Author.setObjectName("Author")
        self.author_input = QtWidgets.QTextEdit(book_reg_widget)
        self.author_input.setGeometry(QtCore.QRect(200, 220, 241, 31))
        self.author_input.setObjectName("author_input")
        self.Title = QtWidgets.QLabel(book_reg_widget)
        self.Title.setGeometry(QtCore.QRect(60, 100, 91, 21))
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setPointSize(11)
        self.Title.setFont(font)
        self.Title.setObjectName("Title")
        self.title_input = QtWidgets.QTextEdit(book_reg_widget)
        self.title_input.setGeometry(QtCore.QRect(200, 100, 241, 31))
        self.title_input.setObjectName("title_input")
        self.ReturnButton = QtWidgets.QCommandLinkButton(book_reg_widget)
        self.ReturnButton.setGeometry(QtCore.QRect(490, 10, 101, 48))
        self.ReturnButton.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.ReturnButton.setObjectName("ReturnButton")
        self.SearchButton = QtWidgets.QPushButton(book_reg_widget)
        self.SearchButton.setGeometry(QtCore.QRect(200, 300, 151, 51))
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setPointSize(11)
        self.SearchButton.setFont(font)
        self.SearchButton.setObjectName("SearchButton")

        self.retranslateUi(book_reg_widget)
        QtCore.QMetaObject.connectSlotsByName(book_reg_widget)

    def retranslateUi(self, book_reg_widget):
        _translate = QtCore.QCoreApplication.translate
        book_reg_widget.setWindowTitle(_translate("book_reg_widget", "book_reg_widget"))
        self.Price.setText(_translate("book_reg_widget", "Price:"))
        self.Category.setText(_translate("book_reg_widget", "Category:"))
        self.Year.setText(_translate("book_reg_widget", "Year:"))
        self.Press.setText(_translate("book_reg_widget", "Press:"))
        self.Author.setText(_translate("book_reg_widget", "Author:"))
        self.Title.setText(_translate("book_reg_widget", "Title:"))
        self.ReturnButton.setText(_translate("book_reg_widget", "Return"))
        self.SearchButton.setText(_translate("book_reg_widget", "Registration"))
