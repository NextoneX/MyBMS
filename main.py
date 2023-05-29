
import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QDialog, QMessageBox
from PyQt5 import QtCore, QtGui, QtWidgets
from frontend.windows_ui import *
from link.connect import Connect
from process.admin import AdminClass
from process.util import SearchBook
#region mainwindow
class login_window(QMainWindow):
    def __init__(self, db):
        self.admin = AdminClass(db)
        super(login_window, self).__init__()
        self.ui = Ui_login_window()
        self.ui.setupUi(self)
        self.ui.statusbar.setStyleSheet("QStatusBar{color: red;}")
        self.ui.LoginButton.clicked.connect(self.check_login)
        self.ui.Non_admin_login.clicked.connect(self.openSearchBookWindow)

    def check_login(self):
        if(self.admin.login(self.ui.ano_input.toPlainText(), self.ui.password_input.toPlainText())):
            self.openAdminWindow()
            QMessageBox.information(self, "Login success", "Login success!")
        else:
            QMessageBox.critical(self, "Login failed", "ID or password error!")
            self.ui.statusbar.showMessage("ID or password error!", 0)

    def openAdminWindow(self):
        self.ui = Ui_admin_window()
        self.ui.setupUi(self)
        self.ui.BookRegButton.clicked.connect(self.openBookRegWindow)
        self.ui.BookOpButton.clicked.connect(self.openBRWindow)
        self.ui.CardManageButton.clicked.connect(self.openCardManageWindow)
        self.ui.BookSearchButton.clicked.connect(self.openSearchBookWindow)

    def opensubwindow(self, window_type):
        self.hide()
        new_window = window_type(self.admin)
        new_window.destroyed.connect(self.show)
        new_window.ui.ReturnButton.clicked.connect(self.show)
        new_window.exec_()

    def openSearchBookWindow(self):
        self.opensubwindow(search_book_widget)

    def openBookRegWindow(self):
        self.opensubwindow(book_reg_widget)

    def openBRWindow(self):
        self.opensubwindow(BR_widget)
    
    def openCardManageWindow(self):
        self.opensubwindow(card_manage_widget)
#endregion

#region widgets
class search_book_widget(QDialog):
    def __init__(self, admin):
        self.search = SearchBook(admin.db)
        super(search_book_widget, self).__init__()
        self.ui = Ui_search_book_widget()
        self.ui.setupUi(self)
        self.ui.ReturnButton.clicked.connect(self.close)
        self.ui.SearchButton.clicked.connect(self.search_book)
    
    def search_book(self):
        category = self.ui.category_input.toPlainText()
        title = self.ui.title_input.toPlainText()
        press = self.ui.press_input.toPlainText()
        year_from = self.ui.year_input_from.toPlainText()
        year_to = self.ui.year_input_to.toPlainText()
        author = self.ui.author_input.toPlainText()
        price_from = self.ui.price_input_from.toPlainText()
        price_to = self.ui.price_input_to.toPlainText()
        state, result = self.search.find_book(category, title, press, year_from, 
                            year_to, author, price_from, price_to)
        if(state == 1):
            QMessageBox.information(self, "Search success", result)
        elif(state == 0):
            QMessageBox.critical(self, "Search failed", "No input!")
        elif(state == -1):
            QMessageBox.critical(self, "Search failed", result)
        elif(state == 404):
            QMessageBox.critical(self, "Search failed", "No such book!")
        else:
            QMessageBox.critical(self, "Search failed", "Unknown error!")

class book_reg_widget(QDialog):
    def __init__(self, admin):
        self.admin = admin
        super(book_reg_widget, self).__init__()
        self.ui = Ui_book_reg_widget()
        self.ui.setupUi(self)
        self.ui.ReturnButton.clicked.connect(self.close)
        self.ui.RegButton.clicked.connect(self.reg_book)

    def reg_book(self):
        #todo check input
        #todo show result
        #todo show error
        bno = self.ui.bno_input.toPlainText()
        category = self.ui.category_input.toPlainText()
        title = self.ui.title_input.toPlainText()
        press = self.ui.press_input.toPlainText()
        year = self.ui.year_input.toPlainText()
        author = self.ui.author_input.toPlainText()
        price = self.ui.price_input.toPlainText()
        total = self.ui.total_input.toPlainText()
        stock = self.ui.stock_input.toPlainText()
        state = self.admin.add_newbook(bno, category, title, press, year, author, price, total, stock)
        if(state == 1):
            QMessageBox.information(self, "Reg success", "Reg success!")
        elif(state == 404):
            QMessageBox.critical(self, "Reg failed", "No result!")
        else:
            QMessageBox.critical(self, "Reg failed", "Unknown error!")

class BR_widget(QDialog):
    def __init__(self, admin):
        self.admin = admin
        super(BR_widget, self).__init__()
        self.ui = Ui_BR_widget()
        self.ui.setupUi(self)
        self.ui.ReturnButton_2.clicked.connect(self.close)
        self.ui.CardInputButton.clicked.connect(self.card_input)
        self.ui.BorrowButton.setEnabled = False
        self.ui.BorrowButton.clicked.connect(self.borrow_book)
        self.ui.ReturnButton.setEnabled = False
        self.ui.ReturnButton.clicked.connect(self.return_book)
        self.cno: str = None

    def card_input(self):
        self.cno = self.ui.cno_input.toPlainText()
        state = self.admin.check_card(self.cno)
        if(state):
            QMessageBox.information(self, "Card check success", "Card check success!")
            self.ui.borrowed_output.setText(self.admin.show_borrow_book(self.cno))
            self.ui.BorrowButton.setEnabled = True
            self.ui.ReturnButton.setEnabled = True
        else:
            QMessageBox.critical(self, "Card check failed", "Card check failed!")
            self.ui.BorrowButton.setEnabled = False
            self.ui.ReturnButton.setEnabled = False

    def borrow_book(self):
        #todo more output
        bno = self.ui.bno_input.toPlainText()
        state = self.admin.book_borrow(bno, self.cno)
        if(state == 1):
            QMessageBox.information(self, "Borrow success", "Borrow success!")
        elif(state == -1):
            QMessageBox.critical(self, "Borrow failed", "Not enough!")
        elif(state == 404):
            QMessageBox.critical(self, "Borrow failed", "No result!")
        else:
            QMessageBox.critical(self, "Borrow failed", "Unknown error!")

    def return_book(self):
        #todo more output
        bno = self.ui.bno_input.toPlainText()
        state = self.admin.book_return(bno, self.cno)
        # state, message = self.admin.book_return(bno, self.cno)
        if(state == 1):
            QMessageBox.information(self, "Return success", "Return success!")
        elif(state == 404):
            QMessageBox.critical(self, "Return failed", "No result!")
        else:
            QMessageBox.critical(self, "Return failed", "Unknown error!")

class card_manage_widget(QDialog):
    def __init__(self, admin):
        self.admin = admin
        super(card_manage_widget, self).__init__()
        self.ui = Ui_card_manage_widget()
        self.ui.setupUi(self)
        self.ui.ReturnButton.clicked.connect(self.close)
        self.ui.AddButton.clicked.connect(self.add_card)
        self.ui.DeleteButton.clicked.connect(self.delete_card)
    
    def add_card(self):
        #todo check input
        #todo show result
        #todo show error
        cno = self.ui.cno_input.toPlainText()
        name = self.ui.name_input.toPlainText()
        department = self.ui.department_input.toPlainText()
        type = self.ui.type_input.value()
        state = self.admin.add_card(cno, name, department, type)
        if(state == 1):
            QMessageBox.information(self, "Add success", "Add success!")
        elif(state == -1):
            QMessageBox.critical(self, "Add failed", "Already exist!")
        else:
            QMessageBox.critical(self, "Add failed", "Unknown error!")
    
    def delete_card(self):
        #todo check input
        #todo show result
        #todo show error
        cno = self.ui.cno_input.toPlainText()
        state = self.admin.delete_card(cno)
        if(state == 1):
            QMessageBox.information(self, "Delete success", "Delete success!")
        elif(state == 404):
            QMessageBox.critical(self, "Delete failed", "No such card!")
        else:
            QMessageBox.critical(self, "Delete failed", "Unknown error!")
#endregion
    
if __name__ == '__main__':
    conn = Connect()
    # admin = AdminClass(conn.db)
    app = QApplication(sys.argv)
    main_window = login_window(conn.db)
    main_window.show()
    sys.exit(app.exec_())