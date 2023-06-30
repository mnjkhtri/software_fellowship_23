from flask import Flask, render_template, request, url_for, redirect
from pymongo import MongoClient
from bson.objectid import ObjectId

app = Flask(__name__)
# connecting to Mongodb server
client = MongoClient("mongodb://mongo:irxi1GrdztU7pHfU4lFp@containers-us-west-23.railway.app:6674")

# accessing the "flask_db"
db = client.flask_db

# accessing the collection "todos" in "flask_db"
todos = db.todos

@app.route('/', methods = ['GET', 'POST'])
def index():
    if request.method == 'POST':
        content = request.form['content']
        important = 'important' in request.form
        todos.insert_one({'content':content, 'important':important})
        return redirect(url_for('index'))
    all_todos = todos.find()
    return render_template('index.html', todos=all_todos)



@app.route('/<id>/delete/', methods = ['POST'])
def delete_todo(id):
    todos.delete_one({"_id":ObjectId(id)})
    return redirect(url_for('index'))

@app.route('/<id>/update/', methods = ['GET','POST'])
def update_todo(id):
    if request.method == 'GET':
        to_be_updated_todo = todos.find_one({'_id':ObjectId(id)})
        return render_template('update.html', todo=to_be_updated_todo)
    else:
        content = request.form['content']
        important = 'important' in request.form
        todos.find_one_and_update({'_id':ObjectId(id)},{'$set':{'content':content,'important':important}})
        return redirect(url_for('index'))

@app.route('/<id>/complete/', methods=['POST'])
def mark_completed(id):
    todos.find_one_and_update({'_id':ObjectId(id)},{'$set':{'completed':True}})
    return redirect(url_for('index'))

@app.route('/<id>/unmark/', methods=['POST'])
def mark_uncompleted(id):
    todos.find_one_and_update({'_id':ObjectId(id)},{'$set':{'completed':False}})
    return redirect(url_for('index'))