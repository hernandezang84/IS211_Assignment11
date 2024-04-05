from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

todo_items = []

@app.route('/')
def home():
    return render_template('todo.html', todos=todo_items)

@app.route('/submit', methods=['POST'])
def submit():
    task = request.form['task']
    email = request.form['email']
    priority = request.form['priority']

    if task and email and (priority in ['Low', 'Medium', 'High']):
        todo_items.append({'task': task, 'email': email, 'priority': priority})
        return redirect(url_for('home'))
    else:
        return redirect(url_for('home'))
    

@app.route('/clear', methods=['POST'])
def clear():
    global todo_items
    todo_items = []
    return redirect(url_for('home'))

if __name__ == '__main__':
    app.run(debug=True)