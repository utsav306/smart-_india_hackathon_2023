from sqlite3 import *

db = connect("./gyaanConnect.db")

cursor = db.cursor()


cursor.execute('''SELECT name FROM sqlite_master WHERE type="table";''')

print("db created")


data = cursor.fetchall()

print(data)