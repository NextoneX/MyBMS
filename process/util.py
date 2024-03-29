from PyQt5.QtWidgets import QMessageBox, QTextBrowser


class Util():
    def check_int(str_in: str) -> int:
        try:
            return int(str_in)
        except:
            return -1
        
    def check_float(str_in: str):
        try:
            return float(str_in)
        except:
            return -1

class ScrollableMessageBox(QMessageBox):
    def __init__(self, textContent: str, textScoll: str, parent=None):
        super(ScrollableMessageBox, self).__init__(parent)
        self.setText(textContent)
        text_browser = QTextBrowser()
        text_browser.setPlainText(textScoll)
        text_browser.setMinimumWidth(600)
        self.layout().addWidget(text_browser)

class SearchBook():
    def __init__(self, db) -> None:
        self.__db = db
        self.__cursor = db.cursor()

    def find_book(self, category: str, title: str, press: str, year_from: str, year_to: str, 
            author: str, price_from: str, price_to: str, order: str, descCheck: bool):
        search_book_sql = " select * from book where"
        length = len(search_book_sql)
        if(category != ""): search_book_sql += " category = '%s' and " % category
        if(title != ""): search_book_sql += " title = '%s' and " % title
        if(press != ""): search_book_sql += " press = '%s' and " % press
        if(year_from != ""): 
            temp = Util.check_int(year_from)
            if(temp == -1): return -1, "year_from is not a number!"
            search_book_sql += " year >= %i and " % temp
        if(year_to != ""): 
            temp = Util.check_int(year_to)
            if(temp == -1): return -1, "year_to is not a number!"
            search_book_sql += " year <= %i and " % temp
        if(author != ""): search_book_sql += " author = %s and " % author
        if(price_from != ""): 
            temp = Util.check_int(price_from)
            if(temp == -1): return -1, "price_from is not a number!"
            search_book_sql += " price >= %i and " % temp
        if(price_to != ""): 
            temp = Util.check_int(price_to)
            if(temp == -1): return -1, "price_to is not a number!"
            search_book_sql += " price <= %i and " % temp
        if(len(search_book_sql) == length): return -1, "No input!"
        search_book_sql += " 1 = 1 Order by " + order
        if(descCheck): search_book_sql += " desc "
        try:
            # print(search_book_sql)
            self.__cursor.execute(search_book_sql)
            result = self.__cursor.fetchall()
            # print(result)
            if(len(result) == 0): 
                return -1, "No such book!"
            else: 
                result_str = "\n".join(" ".join(str(i) for i in row) for row in result)
                # print(result_str)
                return 1, result_str
        except Exception as e:
            self.__db.rollback()
            return 0, str(u'Query failed\n') + str(e)