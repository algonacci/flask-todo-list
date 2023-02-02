import mysql.connector

db = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="",
    database="todo-list-php"
)

cursor = db.cursor()
