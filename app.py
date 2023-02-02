from flask import Flask, render_template, request, redirect
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
    return redirect("/")


@app.get("/edit/<int:id>")
def edit_task(id):
    cursor.execute("SELECT * FROM todos WHERE id = ('{}')".format(id))
    data = cursor.fetchall()
    return render_template("edit.html", data=data)


@app.post("/update/<int:id>")
def update_task(id):
    todo = request.form["todo"]
    cursor.execute(
        "UPDATE todos SET todo = ('{}') WHERE ID = ('{}')".format(todo, id))
    db.commit()
    return redirect("/")


@app.post("/delete/<int:id>")
def delete_task(id):
    cursor.execute("DELETE FROM todos WHERE id = ('{}')".format(id))
    db.commit()
    return redirect("/")


if __name__ == "__main__":
    app.run()
