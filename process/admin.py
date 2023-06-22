import datetime
from process.util import Util

class AdminClass():
    def __init__(self, db) -> None:
        self.__no = None
        self.db = db
        self.__cursor = db.cursor()

    def __del__(self) -> None:
        self.__cursor.close()
        if(self.__no):
            print("Account has been logged out.\n")

    def login(self, login_no: str, login_password: str) -> bool:
        login_sql = " select * from admin where ano = %s and password = %s"
        try:
            self.__cursor.execute(login_sql, (login_no, login_password))
            result = len(self.__cursor.fetchall())
        except:
            return False
        
        if(result > 0):
            self.__no = login_no
            print("Login success.\n")
            return True
        else:
            return False

    def book_borrow(self, bno: str, cno: str):
        #do some check
        if(len(bno) != 8):
            return -1, "bno is not 8 digits!"
        if(len(cno) != 7):
            return -1, "cno is not 7 digits!"
        check_stock_sql = " select stock from book where bno = %s "
        self.__cursor.execute(check_stock_sql,(bno))
        result = self.__cursor.fetchall()
        if(len(result) < 1):
            return -1, "No such book!"  #not found
        # print(result)
        if(int(result[0][0]) < 1):
            find_book_sql = " select borrow_date from borrow where bno = %s and return_date is null ORDER BY borrow_date "
            self.__cursor.execute(find_book_sql,(bno))
            result = self.__cursor.fetchall()
            return -1, "No stock!\n" + "The earliest books on loan are in " + result[0]   #not enough
        search_type_sql = " select type from card where cno = %s "
        self.__cursor.execute(search_type_sql,(cno))
        type = int(self.__cursor.fetchall()[0][0])
        # print(type)
        check_borrow_sql = " select * from borrow where bno = %s and cno = %s and return_date is null "
        self.__cursor.execute(check_borrow_sql,(bno, cno))
        result = self.__cursor.fetchall()
        if(len(result) >= type):
            return -1, "The number of books borrowed has reached your limit."  #borrow limit
        
        #borrow
        try:
            borrow_sql = " insert into borrow values (%s,%s,%s,null,%s) "
            borrow_date = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            self.__cursor.execute(borrow_sql,(bno, cno, borrow_date, self.__no))
            stock_sub_sql = " update book set stock = stock - 1 where bno = %s "
            self.__cursor.execute(stock_sub_sql,(bno))
            self.db.commit()
            return 1, None
        
        except Exception as e:
            self.db.rollback()
            return 0, str(u'Borrow book failed\n') + str(e)

    def book_return(self, bno: str, cno: str):
        #do some check
        if(len(bno) != 8):
            return -1, "bno is not 8 digits!"
        if(len(cno) != 7):
            return -1, "cno is not 7 digits!"
        check_return_sql = (" select * from borrow where bno = %s and cno = %s"
                            " and return_date is null ")
        self.__cursor.execute(check_return_sql,(bno, cno))
        result = self.__cursor.fetchall()
        if(len(result) < 1):
            return -1, "No record!"  #not found
        
        #return
        try:
            return_sql = (" update borrow set return_date = %s, ano = %s" 
                          " where bno = %s and cno = %s and return_date is null order by borrow_date limit 1")
            return_date = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            self.__cursor.execute(return_sql,(return_date, self.__no, bno, cno))
            stock_add_sql = " update book set stock = stock + 1 where bno = %s "
            self.__cursor.execute(stock_add_sql,(bno))
            self.db.commit()
            return 1, None
        
        except Exception as e:
            self.db.rollback()
            return 0, str(u'Return book failed\n') + str(e)

    def reg_book(self, bno: str, category: str, title: str, press: str, year_str: str, 
                            author: str, price_str: str, num_str: str):
        #region input check
        if(len(bno) != 8):
            return -1, "bno is not 8 digits!"
        if(len(category) > 19):
            return -1, "category is too long!"
        if(len(title) > 39):
            return -1, "title is too long!"
        if(len(title) == 0):
            return -1, "title is empty!"
        if(len(press) > 29):
            return -1, "press is too long!"
        if(len(press) == 0):
            return -1, "press is empty!"
        year = Util.check_int(year_str)
        if(year < 0 or year > 9999):
            return -1, "year error!"
        if(len(author) > 19):
            return -1, "author is too long!"
        if(len(author) == 0):
            return -1, "author is empty!"
        price = Util.check_float(price_str)
        if(price < 0 or price > 9999):
            return -1, "price error!"
        num = Util.check_int(num_str)
        if(num < 0 or num > 9999):
            return -1, "number error!"
        #endregion

        check_reg_book_sql = " select * from book where bno = %s "
        self.__cursor.execute(check_reg_book_sql,(bno))
        result = self.__cursor.fetchall()
        if(len(result) > 0):
            return -1, "Already exist!"
        
        try:
            reg_book_sql = " insert into book values ('%s','%s','%s','%s',%i,'%s',%.2f,%i,%i) " % (bno,
                                                 category, title, press, year, author, price, num, num)
            self.__cursor.execute(reg_book_sql)
            self.db.commit()
            return 1, None
        
        except Exception as e:
            self.db.rollback()
            return 0, str(u'Reg book failed\n') + str(e)
    
    def add_book(self, bno: str, num_str: str):
        if(len(bno) != 8):
            return -1, "bno is not 8 digits!"
        num = Util.check_int(num_str)
        if(num < 0 or num > 9999):
            return -1, "number error!"
        check_add_book_sql = " select * from book where bno = %s "
        self.__cursor.execute(check_add_book_sql,(bno))
        result = self.__cursor.fetchall()
        if(len(result) < 1):
            return -1, "Don't exist!"
        
        try:
            add_book_sql = " update book set total = total + %i, stock = stock + %i where bno = '%s' " % (num, num, bno)
            self.__cursor.execute(add_book_sql)
            self.db.commit()
            return 1, None
        
        except Exception as e:
            self.db.rollback()
            return 0, str(u'Add book failed\n') + str(e)
    
    def check_card(self, cno: str) -> bool:
        check_card_sql = " select * from card where cno = %s "
        self.__cursor.execute(check_card_sql,(cno))
        result = self.__cursor.fetchall()
        if(len(result) > 0):
            return True
        else:
            return False

    def add_card(self, cno: str, name: str, department: str, type: int):
        #do some check
        if(len(cno) != 7):
            return -1, "cno is not 7 digits!"
        if(len(name) > 19):
            return -1, "name is too long!"
        if(len(department) > 39):
            return -1, "department is too long!"
        if(self.check_card(cno)):
            return -1, "Already exist!"  #already exist
        
        try:
            add_card_sql = " insert into card values ('%s', '%s', '%s', %i) " % (cno, name, department, type)
            self.__cursor.execute(add_card_sql)
            self.db.commit()
            return 1, None
        
        except Exception as e:
            self.db.rollback()
            return 0, str(u'Add card failed\n') + str(e)


    def delete_card(self, cno: str):
        #do some check
        if(len(cno) != 7):
            return -1, "cno is not 7 digits!"
        if(not self.check_card(cno)):
            return -1, "Don't have this card!"  #not found
        state, _ = self.show_borrow_book(cno, False)
        if(state != -1):
            return -1, "There are still books not returned"
        
        try:
            delete_card_sql = " delete from card where cno = %s "
            self.__cursor.execute(delete_card_sql,(cno))
            self.db.commit()
            return 1, None
        
        except Exception as e:
            self.db.rollback()
            return 0, str(u'delete card failed\n') + str(e)
        
    def show_borrow_book(self, cno, show_result = True):
        show_borrow_sql = " select * from borrow where cno = %s and return_date is null "
        self.__cursor.execute(show_borrow_sql, (cno))
        borrow_result = self.__cursor.fetchall()
        if(len(borrow_result) == 0):
            return -1, "No book borrowed!"
        elif(show_result):
            result = []
            show_borrow_book_sql = " select * from book where bno = %s "
            for i in range(len(borrow_result)):
                # print(borrow_result[i][0])
                self.__cursor.execute(show_borrow_book_sql, (borrow_result[i][0]))
                result.append(self.__cursor.fetchall()[0])
            result_str = "\n".join(" ".join(str(i) for i in row) for row in result)
            return 0, result_str
        
        return 0, None
    
        