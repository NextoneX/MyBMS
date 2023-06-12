
import sys
from PyQt5.QtWidgets import QApplication

from frontend.windows_logic import login_window
from link.connect import Connect
    
if __name__ == '__main__':
    conn = Connect()
    app = QApplication(sys.argv)
    main_window = login_window(conn.db)
    main_window.show()
    sys.exit(app.exec_())