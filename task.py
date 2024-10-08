# task.py
class Task:
    def __init__(self, title, description, category, completed=False):
        self.title = title
        self.description = description
        self.category = category
        self.completed = completed  # Default to False if not provided

    def mark_completed(self):
        self.completed = True
