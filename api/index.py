from flask import Flask,render_template,redirect,request,url_for
import time
app=Flask(__name__,template_folder="./")

todos_list=[]
@app.route("/")
def home():
    return render_template("todo.html", todos=todos_list)
    
@app.route('/<int:id>/delete', methods=['POST'])
def delete(id):
    #id = int(id)
    for i in range(len(todos_list)):
        if todos_list[i]['id'] == id:
            todos_list.pop(i)
            break
    return redirect(url_for('home'))

@app.route('/add', methods=['POST'])
def add():
    task = request.form['item']
    if len(task) > 0:
        id = int(time.time()*1000)
        todos_list.append({'id': id, 'task': task})
        print(todos_list)
    return redirect(url_for('home'))

