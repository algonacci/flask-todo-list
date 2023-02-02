from flask import Flask
from db import db, cursor

app = Flask(__name__)


@app.get("/")
def root():
    cursor.execute("SELECT * FROM todos")
    data = cursor.fetchall()
    print(data)
    return "Hello World!"


if __name__ == "__main__":
    app.run()
