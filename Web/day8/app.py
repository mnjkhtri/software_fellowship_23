from flask import Flask,render_template,request,redirect,url_for
from pymongo import MongoClient
import time
from bson.objectid import ObjectId

app = Flask(__name__)

client = MongoClient('mongodb://mongo:yEmfwMJ7AZDQWsToN07r@containers-us-west-120.railway.app:5736')

db = client.flask_db
todos = db.todos

@app.route('/',methods=['GET','POST'])
def home():
    if request.method == "POST":
        print('i am here in home- post')
        content = request.form['content']
        todos.insert_one({'content':content})
        return redirect(url_for('home'))
    all_todos = todos.find()
    return render_template('todos.html',todos=all_todos)
    
@app.route('/delete',methods=['POST'])
def delete():
    if request.method == "POST":
        print('i am here')
        todo_id = request.form['todo_id']
        print(todo_id)
        todos.delete_one({"_id":ObjectId(todo_id)})
        return redirect(url_for('home'))
