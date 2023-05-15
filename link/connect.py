import pymysql

class Connect():
    def __init__(self) -> None:
        self.db = pymysql.connect(host='127.0.0.1', user='root', password="175763971", database='mybms', port=3306)
        self.cursor = self.db.cursor()
        print("Link success.\n")

    def __del__(self):
        self.cursor.close()
        self.db.close()
        print("Link has ended.\n")