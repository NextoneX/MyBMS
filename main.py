
import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QDialog
from PyQt5 import QtCore, QtGui, QtWidgets
from frontend.login_window import Ui_login_window
from frontend.admin_window import Ui_admin_window
from frontend.book_reg_widget import Ui_book_reg_widget
from frontend.BR_widget import Ui_BR_widget
from frontend.card_manage_widget import Ui_card_manage_widget
from frontend.search_book_widget import Ui_search_book_widget

class login_window(QMainWindow):
    def __init__(self):
        super(login_window, self).__init__()
        self.ui = Ui_login_window()
        self.ui.setupUi(self)
        self.ui.LoginButton.clicked.connect(self.check_login)
        self.ui.Non_admin_login.clicked.connect(self.openSearchBookWindow)

    def check_login(self):
        if(True):
            self.openAdminWindow()

    def openAdminWindow(self):
        self.ui = Ui_admin_window()
        self.ui.setupUi(self)
        self.ui.BookRegButton.clicked.connect(self.openBookRegWindow)
        self.ui.BookOpButton.clicked.connect(self.openBRWindow)
        self.ui.CardManageButton.clicked.connect(self.openCardManageWindow)
        self.ui.BookSearchButton.clicked.connect(self.openSearchBookWindow)
    
    def openSearchBookWindow(self):
        self.hide()
        new_window = search_book_widget()
        new_window.destroyed.connect(self.show)
        new_window.ui.ReturnButton.clicked.connect(self.show)
        new_window.exec_()

    def openBookRegWindow(self):
        self.hide()
        new_window = book_reg_widget()
        new_window.destroyed.connect(self.show)
        new_window.ui.ReturnButton.clicked.connect(self.show)
        new_window.exec_()

    def openBRWindow(self):
        self.hide()
        new_window = BR_widget()
        new_window.destroyed.connect(self.show)
        new_window.ui.ReturnButton_2.clicked.connect(self.show)
        new_window.exec_()
    
    def openCardManageWindow(self):
        self.hide()
        new_window = card_manage_widget()
        new_window.destroyed.connect(self.show)
        new_window.ui.ReturnButton.clicked.connect(self.show)
        new_window.exec_()
    
    def openSearchBookWindow(self):
        self.hide()
        new_window = search_book_widget()
        new_window.destroyed.connect(self.show)
        new_window.ui.ReturnButton.clicked.connect(self.show)
        new_window.exec_()

class search_book_widget(QDialog):
    def __init__(self):
        super(search_book_widget, self).__init__()
        self.ui = Ui_search_book_widget()
        self.ui.setupUi(self)
        self.ui.ReturnButton.clicked.connect(self.close)

class book_reg_widget(QDialog):
    def __init__(self):
        super(book_reg_widget, self).__init__()
        self.ui = Ui_book_reg_widget()
        self.ui.setupUi(self)
        self.ui.ReturnButton.clicked.connect(self.close)

class BR_widget(QDialog):
    def __init__(self):
        super(BR_widget, self).__init__()
        self.ui = Ui_BR_widget()
        self.ui.setupUi(self)
        self.ui.ReturnButton_2.clicked.connect(self.close)

class card_manage_widget(QDialog):
    def __init__(self):
        super(card_manage_widget, self).__init__()
        self.ui = Ui_card_manage_widget()
        self.ui.setupUi(self)
        self.ui.ReturnButton.clicked.connect(self.close)

    
if __name__ == '__main__':
    app = QApplication(sys.argv)
    main_window = login_window()
    main_window.show()
    sys.exit(app.exec_())