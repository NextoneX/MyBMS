
import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QDialog
from PyQt5 import QtCore, QtGui, QtWidgets
from frontend.windows_ui import *
from link.connect import Connect
from process.admin import AdminClass

#region mainwindow
class login_window(QMainWindow):
    def __init__(self, admin):
        self.admin = admin
        super(login_window, self).__init__()
        self.ui = Ui_login_window()
        self.ui.setupUi(self)
        self.ui.statusbar.setStyleSheet("QStatusBar{color: red;}")
        self.ui.LoginButton.clicked.connect(self.check_login)
        self.ui.Non_admin_login.clicked.connect(self.openSearchBookWindow)

    def check_login(self):
        if(admin.login(self.ui.ano_input.toPlainText(), self.ui.password_input.toPlainText())):
            self.openAdminWindow()
        else:
            self.ui.statusbar.showMessage("ID or password error!", 0)

    def openAdminWindow(self):
        self.ui = Ui_admin_window()
        self.ui.setupUi(self)
        self.ui.BookRegButton.clicked.connect(self.openBookRegWindow)
        self.ui.BookOpButton.clicked.connect(self.openBRWindow)
        self.ui.CardManageButton.clicked.connect(self.openCardManageWindow)
        self.ui.BookSearchButton.clicked.connect(self.openSearchBookWindow)
    
    def openSearchBookWindow(self):
        self.hide()
        #todo
        new_window = search_book_widget()
        new_window.destroyed.connect(self.show)
        new_window.ui.ReturnButton.clicked.connect(self.show)
        new_window.exec_()

    def openBookRegWindow(self):
        self.hide()
        #todo
        new_window = book_reg_widget()
        new_window.destroyed.connect(self.show)
        new_window.ui.ReturnButton.clicked.connect(self.show)
        new_window.exec_()

    def openBRWindow(self):
        self.hide()
        #todo
        new_window = BR_widget()
        new_window.destroyed.connect(self.show)
        new_window.ui.ReturnButton_2.clicked.connect(self.show)
        new_window.exec_()
    
    def openCardManageWindow(self):
        self.hide()
        #todo
        new_window = card_manage_widget()
        new_window.destroyed.connect(self.show)
        new_window.ui.ReturnButton.clicked.connect(self.show)
        new_window.exec_()
    
    def openSearchBookWindow(self):
        self.hide()
        #todo
        new_window = search_book_widget()
        new_window.destroyed.connect(self.show)
        new_window.ui.ReturnButton.clicked.connect(self.show)
        new_window.exec_()
#endregion

#region widgets
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
#endregion
    
if __name__ == '__main__':
    conn = Connect()
    admin = AdminClass(conn.db)
    app = QApplication(sys.argv)
    main_window = login_window(admin)
    main_window.show()
    sys.exit(app.exec_())