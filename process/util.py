class SearchBook():
    def __init__(self, db) -> None:
        self.__no = None
        self.__db = db
        self.__cursor = db.cursor()

    def find_book(bno: str, category: str, title: str, press: str, year_from: int, year_to: int, 
            author: str, price_from: int, price_to: int, total: int, stock: int):
        #todo
        state = 0
        result = None
        return state, result