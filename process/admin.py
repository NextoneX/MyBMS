import datetime

class AdminClass():
    def __init__(self, db) -> None:
        self.__no = None
        self.db = db
        self.__cursor = db.cursor()

    def __del__(self) -> None:
        self.__cursor.close()
        print("Account has been logged out.\n")

    def login(self, login_no: str, login_password: str) -> bool:
        login_sql = " select * from admin where ano = %s and password = %s"
        self.__cursor.execute(login_sql, (login_no, login_password))
        result = len(self.__cursor.fetchall())
        if(result > 0):
            self.__no = login_no
            print("Login success.\n")
            return True
        else:
            return False

    def book_borrow(self, bno: str, cno: str) -> int:
        #do some check
        check_stock_sql = " select stock from book where bno = %s "
        self.__cursor.execute(check_stock_sql,(bno))
        result = self.__cursor.fetchall()
        if(len(result) < 1):
            return 404  #not found
        if(int(result[0]) < 1):
            return -1   #not enough
        
        #borrow
        try:
            borrow_sql = " insert into borrow values (%s,%s,%s,null,%s) "
            borrow_date = datetime.datetime.now().strftime('%Y-%m-%d')
            self.__cursor.execute(borrow_sql,(bno, cno, borrow_date, self.__no))
            #!todo atomic check
            stock_sub_sql = " update book set stock = stock - 1 where bno = %s "
            self.__cursor.execute(stock_sub_sql,(bno))
            self.db.commit()
            return 1
        
        except Exception as e:
            print(u'借书失败\n查询错误...', e)
            self.db.rollback()
        
        return 0

    def book_return(self, bno: str, cno: str) -> int:
        #do some check
        check_return_sql = (" select * from borrow where bno = %s and cno = %s"
                            " and return_date is null ")
        self.__cursor.execute(check_return_sql,(bno, cno))
        result = self.__cursor.fetchall()
        if(len(result) < 1):
            return 404  #not found
        
        #return
        try:
            return_sql = (" update borrow set return_date = %s, ano = %s" 
                          " where bno = %s and cno = %s and return_date is null ")
            return_date = datetime.datetime.now().strftime('%Y-%m-%d')
            self.__cursor.execute(return_sql,(return_date, self.__no, bno, cno))
            self.db.commit()
            stock_add_sql = " update book set stock = stock + 1 where bno = %s "
            self.__cursor.execute(stock_add_sql,(bno))
            self.db.commit()
            return 1
        
        except Exception as e:
            print(u'借书失败\n查询错误...', e)
            self.db.rollback()
        return 0

    def reg_book(self, bno: str, category: str, title: str, press: str, year_str: str, 
                            author: str, price_str: str, num_str: str):
        #region input check
        if(len(bno) != 8):
            return -1, "bno is not 8 digits!"
        if(len(category) != 10):
            return -1, "category is not 10 digits!"
        if(len(title) > 39):
            return -1, "title is too long!"
        if(len(title) == 0):
            return -1, "title is empty!"
        if(len(press) > 29):
            return -1, "press is too long!"
        if(len(press) == 0):
            return -1, "press is empty!"
        year = AdminClass.check_int(year_str)
        if(year < 0 or year > 9999):
            return -1, "year error!"
        if(len(author) > 19):
            return -1, "author is too long!"
        if(len(author) == 0):
            return -1, "author is empty!"
        price = AdminClass.check_float(price_str)
        if(price < 0 or price > 9999):
            return -1, "price error!"
        num = AdminClass.check_int(num_str)
        if(num < 0 or num > 9999):
            return -1, "number error!"
        #endregion

        check_add_book_sql = " select * from book where bno = %s "
        self.__cursor.execute(check_add_book_sql,(bno))
        result = self.__cursor.fetchall()
        if(len(result) > 0):
            return -1, "Already exist!"
        
        try:
            add_book_sql = " insert into book values ('%s','%s','%s','%s',%i,'%s',%.2f,%i,%i) " % (bno, category, title, press, year, author, price, num, num)
            self.__cursor.execute(add_book_sql)
            self.db.commit()
            return 1, None
        
        except Exception as e:
            print(u'Add book failed\nSearching error...', e)
            self.db.rollback()
        return 0, None
    
    def check_card(self, cno: str) -> bool:
        check_card_sql = " select * from card where cno = %s "
        self.__cursor.execute(check_card_sql,(cno))
        result = self.__cursor.fetchall()
        if(len(result) > 0):
            return True
        else:
            return False

    def add_card(self, cno: str, name: str, department: str, type: int) -> int:
        #do some check
        if(self.check_card(cno)):
            return -1  #already exist
        
        try:
            add_card_sql = " insert into card values (%s,%s,%s,%i) "
            self.__cursor.execute(add_card_sql,(cno, name, department, type))
            self.db.commit()
            return 1
        
        except Exception as e:
            print(u'Add card failed\nSearching error...', e)
            self.db.rollback()
        return 0


    def delete_card(self, cno: str) -> int:
        #do some check
        if(not self.check_card(cno)):
            return 404  #not found
        
        try:
            delete_card_sql = " delete from card where cno = %s "
            self.__cursor.execute(delete_card_sql,(cno))
            self.db.commit()
            return 1
        
        except Exception as e:
            print('删卡失败\n查询错误...', e)
            self.db.rollback()
        return 0
        
    def show_borrow_book(self, cno):
        show_borrow_book_sql = " select * from borrow where cno = %s and return_date is null "
        self.__cursor.execute(show_borrow_book_sql, (cno))
        return self.__cursor.fetchall()
    
    def show_all_cards(self):
        show_card_sql = " select * from card "
        self.__cursor.execute(show_card_sql)
        return self.__cursor.fetchall()
    
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
        