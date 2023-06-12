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

class Ui_book_reg_widget(object):
    def setupUi(self, book_reg_widget):
        book_reg_widget.setObjectName("book_reg_widget")
        book_reg_widget.resize(586, 494)
        self.press_input = QtWidgets.QTextEdit(book_reg_widget)
        self.press_input.setGeometry(QtCore.QRect(180, 170, 281, 31))
        self.press_input.setObjectName("press_input")
        self.Price = QtWidgets.QLabel(book_reg_widget)
        self.Price.setGeometry(QtCore.QRect(40, 290, 91, 21))
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setPointSize(11)
        self.Price.setFont(font)
        self.Price.setObjectName("Price")
        self.year_input = QtWidgets.QTextEdit(book_reg_widget)
        self.year_input.setGeometry(QtCore.QRect(180, 210, 91, 31))
        self.year_input.setObjectName("year_input")
        self.category_input = QtWidgets.QTextEdit(book_reg_widget)
        self.category_input.setGeometry(QtCore.QRect(180, 90, 281, 31))
        self.category_input.setObjectName("category_input")
        self.price_input = QtWidgets.QTextEdit(book_reg_widget)
        self.price_input.setGeometry(QtCore.QRect(180, 290, 91, 31))
        self.price_input.setObjectName("price_input")
        self.Category = QtWidgets.QLabel(book_reg_widget)
        self.Category.setGeometry(QtCore.QRect(40, 90, 91, 21))
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setPointSize(11)
        self.Category.setFont(font)
        self.Category.setObjectName("Category")
        self.Year = QtWidgets.QLabel(book_reg_widget)
        self.Year.setGeometry(QtCore.QRect(40, 210, 91, 21))
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setPointSize(11)
        self.Year.setFont(font)
        self.Year.setObjectName("Year")
        self.Press = QtWidgets.QLabel(book_reg_widget)
        self.Press.setGeometry(QtCore.QRect(40, 170, 91, 21))
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setPointSize(11)
        self.Press.setFont(font)
        self.Press.setObjectName("Press")
        self.Author = QtWidgets.QLabel(book_reg_widget)
        self.Author.setGeometry(QtCore.QRect(40, 250, 91, 21))
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setPointSize(11)
        self.Author.setFont(font)
        self.Author.setObjectName("Author")
        self.author_input = QtWidgets.QTextEdit(book_reg_widget)
        self.author_input.setGeometry(QtCore.QRect(180, 250, 281, 31))
        self.author_input.setObjectName("author_input")
        self.Title = QtWidgets.QLabel(book_reg_widget)
        self.Title.setGeometry(QtCore.QRect(40, 130, 91, 21))
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setPointSize(11)
        self.Title.setFont(font)
        self.Title.setObjectName("Title")
        self.title_input = QtWidgets.QTextEdit(book_reg_widget)
        self.title_input.setGeometry(QtCore.QRect(180, 130, 281, 31))
        self.title_input.setObjectName("title_input")
        self.ReturnButton = QtWidgets.QCommandLinkButton(book_reg_widget)
        self.ReturnButton.setGeometry(QtCore.QRect(460, 10, 101, 48))
        self.ReturnButton.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.ReturnButton.setObjectName("ReturnButton")
        self.RegButton = QtWidgets.QPushButton(book_reg_widget)
        self.RegButton.setGeometry(QtCore.QRect(90, 370, 161, 61))
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setPointSize(11)
        self.RegButton.setFont(font)
        self.RegButton.setObjectName("RegButton")
        self.bno_input = QtWidgets.QTextEdit(book_reg_widget)
        self.bno_input.setGeometry(QtCore.QRect(180, 50, 281, 31))
        self.bno_input.setObjectName("bno_input")
        self.Book_no = QtWidgets.QLabel(book_reg_widget)
        self.Book_no.setGeometry(QtCore.QRect(40, 50, 91, 21))
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setPointSize(11)
        self.Book_no.setFont(font)
        self.Book_no.setObjectName("Book_no")
        self.num_input = QtWidgets.QTextEdit(book_reg_widget)
        self.num_input.setGeometry(QtCore.QRect(180, 330, 91, 31))
        self.num_input.setObjectName("num_input")
        self.Number = QtWidgets.QLabel(book_reg_widget)
        self.Number.setGeometry(QtCore.QRect(40, 330, 91, 21))
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setPointSize(11)
        self.Number.setFont(font)
        self.Number.setObjectName("Number")
        self.add_tips = QtWidgets.QTextBrowser(book_reg_widget)
        self.add_tips.setGeometry(QtCore.QRect(40, 440, 531, 31))
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setPointSize(11)
        self.add_tips.setFont(font)
        self.add_tips.setObjectName("add_tips")
        self.AddButton = QtWidgets.QPushButton(book_reg_widget)
        self.AddButton.setGeometry(QtCore.QRect(310, 370, 161, 61))
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setPointSize(11)
        self.AddButton.setFont(font)
        self.AddButton.setObjectName("AddButton")

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
        self.RegButton.setText(_translate("book_reg_widget", "Registration"))
        self.Book_no.setText(_translate("book_reg_widget", "Book_no:"))
        self.Number.setText(_translate("book_reg_widget", "Number:"))
        self.add_tips.setHtml(_translate("book_reg_widget", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Consolas\'; font-size:11pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'SimSun\';\">Tips: The add button will only read Book_no and Number.</span></p></body></html>"))
        self.AddButton.setText(_translate("book_reg_widget", "Add"))

class Ui_BR_widget(object):
    def setupUi(self, BR_widget):
        BR_widget.setObjectName("BR_widget")
        BR_widget.resize(710, 398)
        self.ReturnButton = QtWidgets.QCommandLinkButton(BR_widget)
        self.ReturnButton.setGeometry(QtCore.QRect(590, 10, 101, 48))
        self.ReturnButton.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.ReturnButton.setObjectName("ReturnButton_2")
        self.Card_no = QtWidgets.QLabel(BR_widget)
        self.Card_no.setGeometry(QtCore.QRect(60, 20, 91, 21))
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setPointSize(11)
        self.Card_no.setFont(font)
        self.Card_no.setObjectName("Card_no")
        self.bno_input = QtWidgets.QTextEdit(BR_widget)
        self.bno_input.setGeometry(QtCore.QRect(220, 230, 241, 31))
        self.bno_input.setObjectName("bno_input")
        self.Book_no = QtWidgets.QLabel(BR_widget)
        self.Book_no.setGeometry(QtCore.QRect(60, 230, 91, 21))
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setPointSize(11)
        self.Book_no.setFont(font)
        self.Book_no.setObjectName("Book_no")
        self.cno_input = QtWidgets.QTextEdit(BR_widget)
        self.cno_input.setGeometry(QtCore.QRect(220, 20, 241, 31))
        self.cno_input.setObjectName("cno_input")
        self.ReturnBookButton = QtWidgets.QPushButton(BR_widget)
        self.ReturnBookButton.setGeometry(QtCore.QRect(460, 290, 151, 51))
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setPointSize(11)
        self.ReturnBookButton.setFont(font)
        self.ReturnBookButton.setObjectName("ReturnButton")
        self.Book_borrowed = QtWidgets.QLabel(BR_widget)
        self.Book_borrowed.setGeometry(QtCore.QRect(60, 70, 151, 21))
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setPointSize(11)
        self.Book_borrowed.setFont(font)
        self.Book_borrowed.setObjectName("Book_borrowed")
        self.BorrowButton = QtWidgets.QPushButton(BR_widget)
        self.BorrowButton.setGeometry(QtCore.QRect(180, 290, 151, 51))
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
        self.CardInputButton = QtWidgets.QPushButton(BR_widget)
        self.CardInputButton.setGeometry(QtCore.QRect(470, 20, 81, 31))
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setPointSize(11)
        self.CardInputButton.setFont(font)
        self.CardInputButton.setCheckable(False)
        self.CardInputButton.setChecked(False)
        self.CardInputButton.setAutoDefault(False)
        self.CardInputButton.setDefault(False)
        self.CardInputButton.setFlat(False)
        self.CardInputButton.setObjectName("CardInputButton")
        self.borrowed_output = QtWidgets.QTextBrowser(BR_widget)
        self.borrowed_output.setGeometry(QtCore.QRect(220, 70, 471, 141))
        self.borrowed_output.setObjectName("borrowed_output")

        self.retranslateUi(BR_widget)
        QtCore.QMetaObject.connectSlotsByName(BR_widget)

    def retranslateUi(self, BR_widget):
        _translate = QtCore.QCoreApplication.translate
        BR_widget.setWindowTitle(_translate("BR_widget", "BR_widget"))
        self.ReturnButton.setText(_translate("BR_widget", "Return"))
        self.Card_no.setText(_translate("BR_widget", "Card_no:"))
        self.Book_no.setText(_translate("BR_widget", "Book_no:"))
        self.ReturnBookButton.setText(_translate("BR_widget", "Return"))
        self.Book_borrowed.setText(_translate("BR_widget", "Borrowed books:"))
        self.BorrowButton.setText(_translate("BR_widget", "Borrow"))
        self.CardInputButton.setText(_translate("BR_widget", "Input"))

class Ui_card_manage_widget(object):
    def setupUi(self, card_manage_widget):
        card_manage_widget.setObjectName("card_manage_widget")
        card_manage_widget.resize(659, 434)
        self.Card_no = QtWidgets.QLabel(card_manage_widget)
        self.Card_no.setGeometry(QtCore.QRect(100, 80, 121, 21))
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setPointSize(11)
        self.Card_no.setFont(font)
        self.Card_no.setObjectName("Card_no")
        self.DeleteButton = QtWidgets.QPushButton(card_manage_widget)
        self.DeleteButton.setGeometry(QtCore.QRect(370, 320, 151, 51))
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
        self.AddButton.setGeometry(QtCore.QRect(130, 320, 151, 51))
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
        self.cno_input.setGeometry(QtCore.QRect(260, 80, 361, 31))
        self.cno_input.setObjectName("cno_input")
        self.delete_tips = QtWidgets.QTextBrowser(card_manage_widget)
        self.delete_tips.setGeometry(QtCore.QRect(60, 390, 561, 31))
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setPointSize(11)
        self.delete_tips.setFont(font)
        self.delete_tips.setObjectName("delete_tips")
        self.Card_no_2 = QtWidgets.QLabel(card_manage_widget)
        self.Card_no_2.setGeometry(QtCore.QRect(100, 130, 121, 21))
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setPointSize(11)
        self.Card_no_2.setFont(font)
        self.Card_no_2.setObjectName("Card_no_2")
        self.name_input = QtWidgets.QTextEdit(card_manage_widget)
        self.name_input.setGeometry(QtCore.QRect(260, 130, 361, 31))
        self.name_input.setObjectName("name_input")
        self.Card_no_3 = QtWidgets.QLabel(card_manage_widget)
        self.Card_no_3.setGeometry(QtCore.QRect(100, 180, 121, 21))
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setPointSize(11)
        self.Card_no_3.setFont(font)
        self.Card_no_3.setObjectName("Card_no_3")
        self.department_input = QtWidgets.QTextEdit(card_manage_widget)
        self.department_input.setGeometry(QtCore.QRect(260, 180, 361, 31))
        self.department_input.setObjectName("department_input")
        self.Card_no_4 = QtWidgets.QLabel(card_manage_widget)
        self.Card_no_4.setGeometry(QtCore.QRect(100, 230, 121, 21))
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setPointSize(11)
        self.Card_no_4.setFont(font)
        self.Card_no_4.setObjectName("Card_no_4")
        self.type_input = QtWidgets.QSpinBox(card_manage_widget)
        self.type_input.setGeometry(QtCore.QRect(260, 230, 51, 31))
        self.type_input.setMinimum(1)
        self.type_input.setMaximum(3)
        self.type_input.setObjectName("type_input")
        self.type_tips = QtWidgets.QTextBrowser(card_manage_widget)
        self.type_tips.setGeometry(QtCore.QRect(330, 230, 291, 81))
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setPointSize(11)
        self.type_tips.setFont(font)
        self.type_tips.setObjectName("type_tips")

        self.retranslateUi(card_manage_widget)
        QtCore.QMetaObject.connectSlotsByName(card_manage_widget)

    def retranslateUi(self, card_manage_widget):
        _translate = QtCore.QCoreApplication.translate
        card_manage_widget.setWindowTitle(_translate("card_manage_widget", "card_manage_widget"))
        self.Card_no.setText(_translate("card_manage_widget", "Card_no:"))
        self.DeleteButton.setText(_translate("card_manage_widget", "Delete"))
        self.ReturnButton.setText(_translate("card_manage_widget", "Return"))
        self.AddButton.setText(_translate("card_manage_widget", "Add"))
        self.delete_tips.setHtml(_translate("card_manage_widget", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Consolas\'; font-size:11pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'SimSun\';\">Tips: The delete button will only read Card_no.</span></p></body></html>"))
        self.Card_no_2.setText(_translate("card_manage_widget", "Name:"))
        self.Card_no_3.setText(_translate("card_manage_widget", "Department:"))
        self.Card_no_4.setText(_translate("card_manage_widget", "Type:"))
        self.type_tips.setHtml(_translate("card_manage_widget", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Consolas\'; font-size:11pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'SimSun\';\">1: undergraduate student</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'SimSun\';\">2: graduate student</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'SimSun\';\">3: teacher</span></p></body></html>"))

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

class Ui_search_book_widget(object):
    def setupUi(self, search_book_widget):
        search_book_widget.setObjectName("search_book_widget")
        search_book_widget.resize(537, 464)
        self.author_input = QtWidgets.QTextEdit(search_book_widget)
        self.author_input.setGeometry(QtCore.QRect(200, 240, 241, 31))
        font = QtGui.QFont()
        font.setFamily("Consolas")
        self.author_input.setFont(font)
        self.author_input.setObjectName("author_input")
        self.Press = QtWidgets.QLabel(search_book_widget)
        self.Press.setGeometry(QtCore.QRect(60, 160, 91, 21))
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setPointSize(11)
        self.Press.setFont(font)
        self.Press.setObjectName("Press")
        self.Category = QtWidgets.QLabel(search_book_widget)
        self.Category.setGeometry(QtCore.QRect(60, 80, 91, 21))
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setPointSize(11)
        self.Category.setFont(font)
        self.Category.setObjectName("Category")
        self.press_input = QtWidgets.QTextEdit(search_book_widget)
        self.press_input.setGeometry(QtCore.QRect(200, 160, 241, 31))
        font = QtGui.QFont()
        font.setFamily("Consolas")
        self.press_input.setFont(font)
        self.press_input.setObjectName("press_input")
        self.Author = QtWidgets.QLabel(search_book_widget)
        self.Author.setGeometry(QtCore.QRect(60, 240, 91, 21))
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setPointSize(11)
        self.Author.setFont(font)
        self.Author.setObjectName("Author")
        self.SearchButton = QtWidgets.QPushButton(search_book_widget)
        self.SearchButton.setGeometry(QtCore.QRect(200, 370, 181, 51))
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setPointSize(11)
        self.SearchButton.setFont(font)
        self.SearchButton.setObjectName("SearchButton")
        self.category_input = QtWidgets.QTextEdit(search_book_widget)
        self.category_input.setGeometry(QtCore.QRect(200, 80, 241, 31))
        font = QtGui.QFont()
        font.setFamily("Consolas")
        self.category_input.setFont(font)
        self.category_input.setObjectName("category_input")
        self.ReturnButton = QtWidgets.QCommandLinkButton(search_book_widget)
        self.ReturnButton.setGeometry(QtCore.QRect(430, 10, 101, 48))
        self.ReturnButton.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.ReturnButton.setObjectName("ReturnButton")
        self.Year = QtWidgets.QLabel(search_book_widget)
        self.Year.setGeometry(QtCore.QRect(60, 200, 91, 21))
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setPointSize(11)
        self.Year.setFont(font)
        self.Year.setObjectName("Year")
        self.price_input_to = QtWidgets.QTextEdit(search_book_widget)
        self.price_input_to.setGeometry(QtCore.QRect(350, 280, 91, 31))
        font = QtGui.QFont()
        font.setFamily("Consolas")
        self.price_input_to.setFont(font)
        self.price_input_to.setObjectName("price_input_to")
        self.Year_from = QtWidgets.QLabel(search_book_widget)
        self.Year_from.setGeometry(QtCore.QRect(150, 200, 51, 21))
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setPointSize(11)
        self.Year_from.setFont(font)
        self.Year_from.setObjectName("Year_from")
        self.Price = QtWidgets.QLabel(search_book_widget)
        self.Price.setGeometry(QtCore.QRect(60, 280, 91, 21))
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setPointSize(11)
        self.Price.setFont(font)
        self.Price.setObjectName("Price")
        self.Title = QtWidgets.QLabel(search_book_widget)
        self.Title.setGeometry(QtCore.QRect(60, 120, 91, 21))
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setPointSize(11)
        self.Title.setFont(font)
        self.Title.setObjectName("Title")
        self.year_input_from = QtWidgets.QTextEdit(search_book_widget)
        self.year_input_from.setGeometry(QtCore.QRect(200, 200, 91, 31))
        font = QtGui.QFont()
        font.setFamily("Consolas")
        self.year_input_from.setFont(font)
        self.year_input_from.setObjectName("year_input_from")
        self.Price_to = QtWidgets.QLabel(search_book_widget)
        self.Price_to.setGeometry(QtCore.QRect(310, 280, 31, 21))
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setPointSize(11)
        self.Price_to.setFont(font)
        self.Price_to.setObjectName("Price_to")
        self.Year_to = QtWidgets.QLabel(search_book_widget)
        self.Year_to.setGeometry(QtCore.QRect(310, 200, 31, 21))
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setPointSize(11)
        self.Year_to.setFont(font)
        self.Year_to.setObjectName("Year_to")
        self.Price_from = QtWidgets.QLabel(search_book_widget)
        self.Price_from.setGeometry(QtCore.QRect(150, 280, 51, 21))
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setPointSize(11)
        self.Price_from.setFont(font)
        self.Price_from.setObjectName("Price_from")
        self.title_input = QtWidgets.QTextEdit(search_book_widget)
        self.title_input.setGeometry(QtCore.QRect(200, 120, 241, 31))
        font = QtGui.QFont()
        font.setFamily("Consolas")
        self.title_input.setFont(font)
        self.title_input.setObjectName("title_input")
        self.year_input_to = QtWidgets.QTextEdit(search_book_widget)
        self.year_input_to.setGeometry(QtCore.QRect(350, 200, 91, 31))
        font = QtGui.QFont()
        font.setFamily("Consolas")
        self.year_input_to.setFont(font)
        self.year_input_to.setObjectName("year_input_to")
        self.price_input_from = QtWidgets.QTextEdit(search_book_widget)
        self.price_input_from.setGeometry(QtCore.QRect(200, 280, 91, 31))
        font = QtGui.QFont()
        font.setFamily("Consolas")
        self.price_input_from.setFont(font)
        self.price_input_from.setObjectName("price_input_from")
        self.Price_2 = QtWidgets.QLabel(search_book_widget)
        self.Price_2.setGeometry(QtCore.QRect(60, 320, 91, 21))
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setPointSize(11)
        self.Price_2.setFont(font)
        self.Price_2.setObjectName("Price_2")
        self.order_input = QtWidgets.QComboBox(search_book_widget)
        self.order_input.setGeometry(QtCore.QRect(200, 320, 111, 31))
        font = QtGui.QFont()
        font.setFamily("Consolas")
        self.order_input.setFont(font)
        self.order_input.setObjectName("order_input")
        self.order_input.addItem("")
        self.order_input.addItem("")
        self.order_input.addItem("")
        self.order_input.addItem("")
        self.order_input.addItem("")
        self.order_input.addItem("")
        self.order_input.addItem("")
        self.order_input.addItem("")
        self.order_input.addItem("")
        self.descCheck = QtWidgets.QCheckBox(search_book_widget)
        self.descCheck.setGeometry(QtCore.QRect(330, 320, 111, 31))
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setPointSize(9)
        self.descCheck.setFont(font)
        self.descCheck.setObjectName("descCheck")

        self.retranslateUi(search_book_widget)
        QtCore.QMetaObject.connectSlotsByName(search_book_widget)

    def retranslateUi(self, search_book_widget):
        _translate = QtCore.QCoreApplication.translate
        search_book_widget.setWindowTitle(_translate("search_book_widget", "search_book_widget"))
        self.Press.setText(_translate("search_book_widget", "Press:"))
        self.Category.setText(_translate("search_book_widget", "Category:"))
        self.Author.setText(_translate("search_book_widget", "Author:"))
        self.SearchButton.setText(_translate("search_book_widget", "Search"))
        self.ReturnButton.setText(_translate("search_book_widget", "Return"))
        self.Year.setText(_translate("search_book_widget", "Year:"))
        self.Year_from.setText(_translate("search_book_widget", "from"))
        self.Price.setText(_translate("search_book_widget", "Price:"))
        self.Title.setText(_translate("search_book_widget", "Title:"))
        self.Price_to.setText(_translate("search_book_widget", "to"))
        self.Year_to.setText(_translate("search_book_widget", "to"))
        self.Price_from.setText(_translate("search_book_widget", "from"))
        self.Price_2.setText(_translate("search_book_widget", "Order_by:"))
        self.order_input.setItemText(0, _translate("search_book_widget", "bno"))
        self.order_input.setItemText(1, _translate("search_book_widget", "category"))
        self.order_input.setItemText(2, _translate("search_book_widget", "title"))
        self.order_input.setItemText(3, _translate("search_book_widget", "press"))
        self.order_input.setItemText(4, _translate("search_book_widget", "year"))
        self.order_input.setItemText(5, _translate("search_book_widget", "author"))
        self.order_input.setItemText(6, _translate("search_book_widget", "price"))
        self.order_input.setItemText(7, _translate("search_book_widget", "total"))
        self.order_input.setItemText(8, _translate("search_book_widget", "stock"))
        self.descCheck.setText(_translate("search_book_widget", "是否为降序"))
     