import json
from task import Task

def save_tasks(tasks):
    with open('tasks.json', 'w') as f:
        json.dump([task.__dict__ for task in tasks], f)

def load_tasks():
    try:
        with open('tasks.json', 'r') as f:
            return [Task(**data) for data in json.load(f)]
    except FileNotFoundError:
        return []
