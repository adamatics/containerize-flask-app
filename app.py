# 1. Import Flask
from flask import Flask, render_template, url_for

from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField

# 2. Define Flask App
app = Flask(__name__)

# 3. Secret Key
app.config['SECRET_KEY'] = 'my-secret-key'

# Class for Tasks app
class Task:

    def __init__(self, name, status):
        self.name = name
        self.status = status


my_tasks = [Task("Start learning Flask!", True)]

# Define Flask Form for New Task
class NewTask(FlaskForm):
    name = StringField(label="New Task")
    add = SubmitField(label="Add Task")

# 4. Entry Point of your Website
@app.route('/')
def index():
    return render_template('index.html')

# 6. 2nd Page - Tasks
@app.route('/tasks', methods=['GET', 'POST'])
def tasks():
    # Form
    form = NewTask()
    # Form Step 1: Method call Validate Submig
    if form.validate_on_submit():
        # Form Step 2: Check whether `Add` button was clicked or not
        if form.add.data:
            # Form Step 3: Get the details of new Task
            new_task_name = form.name.data
            # Form Step 4: Add new task to our Task list.
            my_tasks.append(Task(name=new_task_name, status=False))
            # Clear HTML Text Input field
            form.name.data = ""
    
    return render_template('tasks.html', my_tasks = my_tasks, form=form)

if __name__ == "__main__":
    app.run(host="0.0.0.0/apps/to-dos-app", port=5000)

