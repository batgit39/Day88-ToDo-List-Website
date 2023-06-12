from flask import Flask, render_template, request, redirect

app = Flask(__name__)
tasks = []

@app.route('/')
def index():
    return render_template('index.html', tasks=tasks)

@app.route('/add', methods=['POST'])
def add():
    task = request.form.get('task')
    tasks.append(task)
    return redirect('/')

@app.route('/delete/<int:index>', methods=['POST'])
def delete(index):
    if index < len(tasks):
        del tasks[index]
    return redirect('/')

if __name__ == '__main__':
    app.run(debug=True)

