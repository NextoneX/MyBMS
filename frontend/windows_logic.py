from PyQt5.QtWidgets import QMainWindow, QDialog, QMessageBox
from frontend.windows_ui import *
from process.admin import AdminClass
from process.util import *

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

    def openSubWindow(self, window_type):
        self.hide()
        new_window = window_type(self.admin)
        new_window.destroyed.connect(self.show)
        new_window.ui.ReturnButton.clicked.connect(self.show)
        new_window.exec_()

    def openSearchBookWindow(self):
        self.openSubWindow(search_book_widget)

    def openBookRegWindow(self):
        self.openSubWindow(book_reg_widget)

    def openBRWindow(self):
        self.openSubWindow(BR_widget)
    
    def openCardManageWindow(self):
        self.openSubWindow(card_manage_widget)

#region widgets
class search_book_widget(QDialog):
    def __init__(self, admin: AdminClass):
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
        order = self.ui.order_input.currentText()
        descCheck = self.ui.descCheck.isChecked()
        # print(order)
        state, result = self.search.find_book(category, title, press, year_from, 
                            year_to, author, price_from, price_to, order, descCheck)
        if(state == 1):
            message_box = ScrollableMessageBox("(bno,category,name,press,year,author,price,total,stock):"
                                                , result, self)
            message_box.setWindowTitle("Search success")
            message_box.exec_()
        else:
            QMessageBox.critical(self, "Search failed", result)

class book_reg_widget(QDialog):
    def __init__(self, admin: AdminClass):
        self.admin = admin
        super(book_reg_widget, self).__init__()
        self.ui = Ui_book_reg_widget()
        self.ui.setupUi(self)
        self.ui.ReturnButton.clicked.connect(self.close)
        self.ui.RegButton.clicked.connect(self.reg_book)
        self.ui.AddButton.clicked.connect(self.add_book)

    def reg_book(self):
        bno = self.ui.bno_input.toPlainText()
        category = self.ui.category_input.toPlainText()
        title = self.ui.title_input.toPlainText()
        press = self.ui.press_input.toPlainText()
        year = self.ui.year_input.toPlainText()
        author = self.ui.author_input.toPlainText()
        price = self.ui.price_input.toPlainText()
        num = self.ui.num_input.toPlainText()
        state, result = self.admin.reg_book(bno, category, title, press, year, author, price, num)
        if(state == 1):
            QMessageBox.information(self, "Reg success", "Reg success!")
        else:
            QMessageBox.critical(self, "Reg failed", result)
    
    def add_book(self):
        bno = self.ui.bno_input.toPlainText()
        num = self.ui.num_input.toPlainText()
        state, result = self.admin.add_book(bno, num)
        if(state == 1):
            QMessageBox.information(self, "Add success", "Add success!")
        else:
            QMessageBox.critical(self, "Add failed", result)

class BR_widget(QDialog):
    def __init__(self, admin: AdminClass):
        self.admin = admin
        super(BR_widget, self).__init__()
        self.ui = Ui_BR_widget()
        self.ui.setupUi(self)
        self.ui.ReturnButton.clicked.connect(self.close)
        self.ui.CardInputButton.clicked.connect(self.card_input)
        self.ui.BorrowButton.setEnabled(False)
        self.ui.BorrowButton.clicked.connect(self.borrow_book)
        self.ui.ReturnBookButton.setEnabled(False)
        self.ui.ReturnBookButton.clicked.connect(self.return_book)
        self.cno: str = None

    def card_input(self):
        self.cno = self.ui.cno_input.toPlainText()
        if(self.admin.check_card(self.cno)):
            QMessageBox.information(self, "Card check success", "Card check success!")
            _, result = self.admin.show_borrow_book(self.cno)
            self.ui.borrowed_output.setText(result)
            self.ui.BorrowButton.setEnabled(True)
            self.ui.ReturnBookButton.setEnabled(True)
        else:
            QMessageBox.critical(self, "Card check failed", "Card check failed!")

    def borrow_book(self):
        bno = self.ui.bno_input.toPlainText()
        state, result = self.admin.book_borrow(bno, self.cno)
        if(state == 1):
            self.ui.BorrowButton.setEnabled(False)
            self.ui.ReturnBookButton.setEnabled(False)
            QMessageBox.information(self, "Borrow success", "Borrow success!")
        else:
            QMessageBox.critical(self, "Borrow failed", result)

    def return_book(self):
        bno = self.ui.bno_input.toPlainText()
        state, result = self.admin.book_return(bno, self.cno)
        if(state == 1):
            self.ui.BorrowButton.setEnabled(False)
            self.ui.ReturnBookButton.setEnabled(False)
            QMessageBox.information(self, "Return success", "Return success!")
        else:
            QMessageBox.critical(self, "Return failed", result)

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
        cno = self.ui.cno_input.toPlainText()
        name = self.ui.name_input.toPlainText()
        department = self.ui.department_input.toPlainText()
        type = self.ui.type_input.value()
        state, result = self.admin.add_card(cno, name, department, type)
        if(state == 1):
            QMessageBox.information(self, "Add success", "Add success!")
        else:
            QMessageBox.critical(self, "Add failed", result)
    
    def delete_card(self):
        cno = self.ui.cno_input.toPlainText()
        state, result = self.admin.delete_card(cno)
        if(state == 1):
            QMessageBox.information(self, "Delete success", "Delete success!")
        else:
            QMessageBox.critical(self, "Delete failed", result)
#endregion