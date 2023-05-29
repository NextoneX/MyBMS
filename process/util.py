class SearchBook():
    def __init__(self, db) -> None:
        self.__no = None
        self.__db = db
        self.__cursor = db.cursor()

    def find_book(category: str, title: str, press: str, year_from: int, year_to: int, 
            author: str, price_from: int, price_to: int):
        #todo
        state = 0
        result = None
        search_book_sql = " select * from book where"
        length = len(search_book_sql)
        if(category != ""): search_book_sql += " category = %s and " % category
        if(title != ""): search_book_sql += " title = %s and " % title
        if(press != ""): search_book_sql += " press = %s and " % press
        if(year_from != ""): 
            search_book_sql += " year >= %i and " % year_from
        if(year_to != ""): 
            search_book_sql += " year <= %i and " % year_to
        if(author != ""): search_book_sql += " author = %s and " % author
        if(price_from != ""): 
            search_book_sql += " price >= %d and " % price_from
        if(price_to != ""): 
            search_book_sql += " price <= %d and " % price_to
        if(len(search_book_sql) == length): return -1, None
        search_book_sql += " 1 = 1 "
        result = search_book_sql
        return state, result
    
    def check_int(str_in: str) -> int:
        try:
            return int(str_in)
        except:
            return -1