from flask import Flask, render_template, request, redirect
from file_operations import save_tasks, load_tasks
from task import Task

app = Flask(__name__)

@app.route('/')
def index():
    tasks = load_tasks()
    return render_template('index.html', tasks=tasks)

@app.route('/add', methods=['POST'])
def add_task():
    title = request.form.get('title')
    description = request.form.get('description')
    category = request.form.get('category')
    task = Task(title, description, category)
    tasks = load_tasks()
    tasks.append(task)
    save_tasks(tasks)
    return redirect('/')

@app.route('/complete/<int:index>', methods=['POST'])
def complete_task(index):
    tasks = load_tasks()
    tasks[index].mark_completed()
    save_tasks(tasks)
    return redirect('/')

@app.route('/delete/<int:index>', methods=['POST'])
def delete_task(index):
    tasks = load_tasks()
    del tasks[index]
    save_tasks(tasks)
    return redirect('/')

if __name__ == '__main__':
    app.run(debug=True)
