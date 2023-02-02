from flask import Flask, render_template, request
from db import db, cursor

app = Flask(__name__)


@app.get("/")
def root():
    cursor.execute("SELECT * FROM todos")
    data = cursor.fetchall()
    return render_template("index.html", data=data)


@app.post("/")
def create_task():
    task = request.form["todo"]
    cursor.execute("INSERT INTO todos (`todo`) VALUES ('{}')".format(task))
    db.commit()
    cursor.execute("SELECT * FROM todos")
    data = cursor.fetchall()
    return render_template("index.html", data=data)


if __name__ == "__main__":
    app.run()
