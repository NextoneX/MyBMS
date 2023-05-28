
import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QDialog
from PyQt5 import QtCore, QtGui, QtWidgets
#mainwindow.ui Python文件
from frontend.login_window import Ui_login_window
from frontend.admin_window import Ui_admin_window
from frontend.untitled import Ui_Form

class login_window(QMainWindow):
    def __init__(self):
        super(login_window, self).__init__()
        self.ui = Ui_login_window()
        self.ui.setupUi(self)
        self.ui.LoginButton.clicked.connect(self.openNewWindow)

    def openNewWindow(self):
        self.hide()
        new_window = admin_window()
        new_window.exec_()
        self.close()

class admin_window(QDialog):
    def __init__(self):
        super(admin_window, self).__init__()
        self.ui = Ui_Form()
        self.ui.setupUi(self)
    
if __name__ == '__main__':
    app = QApplication(sys.argv)
    main_window = login_window()
    main_window.show()
    sys.exit(app.exec_())