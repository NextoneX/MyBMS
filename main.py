from link import connect
from process import admin
conn = connect.Connect()
db = conn.db
cursor = conn.cursor

administrator = admin.AdminClass(db)
login_no = input("Enter the administrator ID:")
login_password = input("Enter password:")
administrator.login(login_no, login_password)

print("end")