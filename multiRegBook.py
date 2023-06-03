import sys
from link.connect import Connect
from process.admin import AdminClass

if __name__ == '__main__':
    conn = Connect()
    admin = AdminClass(conn.db)
    file_path = input("Please input the file path(using '/' instead of '\\'):(e.g. D:/test.txt)\n")
    file = open(file_path, 'r', encoding='utf-8')
    # sample file:( book_no1, Computer Science, Computer Architecture, xxx, 2004, xxx, 90.00, 2 ),
    #             ( book_no2, Computer Science, Computer Architecture, xxx, 2004, xxx, 90.00, 2 ),
    #             
    for line in file.readlines():
        # admin.add_book(bno, categoty, title, press, year, author, price, num)
        line = line.strip()
        line = line[2:-3]
        line = line.split(', ')
        bno = line[0].strip()
        category = line[1].strip()
        title = line[2].strip()
        press = line[3].strip()
        year = line[4].strip()
        author = line[5].strip()
        price = line[6].strip()
        num = line[7].strip()
        print(line)
        state, result = admin.reg_book(bno, category, title, press, year, author, price, num)
        if(state == 1):
            print("Reg success!")
        else:
            print("Reg failed! " + result)
    file.close()
