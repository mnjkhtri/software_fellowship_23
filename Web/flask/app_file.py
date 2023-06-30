import json
import time
from flask import Flask, render_template, request, url_for, redirect

app = Flask(__name__)

try:
    with open('./todos.json', 'r') as f:
        todos = json.load(f)
except Exception as e:
    todos = {}
    
def save_to_todos(todos):
    with open('todos.json', 'w') as f:
        json.dump(todos, f, indent=4)
        
@app.route('/', methods = ['GET', 'POST'])
def index():
    if request.method == 'POST':
        content = request.form['content']
        important = 'important' in request.form
        todos[str(int(time.time()))] = {'_id':str(int(time.time())),'content':content, 'important':important}
        save_to_todos(todos)
        return redirect(url_for('index'))
    all_todos = todos.values()
    return render_template('index.html', todos=all_todos)



@app.route('/<id>/delete/', methods = ['POST'])
def delete_todo(id):
    del todos[id]
    save_to_todos(todos)
    return redirect(url_for('index'))

@app.route('/<id>/update/', methods = ['GET', 'POST'])
def update_todo(id):
    if request.method == 'GET':
        to_be_updated_todo = todos[id]
        return render_template('update.html', todo=to_be_updated_todo)
    elif request.method == 'POST':
        content = request.form['content']
        important = 'important' in request.form
        todos[id].update({'content':content, 'important':important})
        save_to_todos(todos)
        return redirect(url_for('index'))
    
    

@app.route('/<id>/complete/', methods=['POST'])
def mark_completed(id):
    todos[id].update({'completed':True})
    save_to_todos(todos)
    return redirect(url_for('index'))

@app.route('/<id>/unmark/', methods=['POST'])
def mark_uncompleted(id):
    todos[id].update({'completed':False})
    save_to_todos(todos)
    return redirect(url_for('index'))