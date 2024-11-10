from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/task_summary')
def task_summary():
    return render_template('task_summary.html')

@app.route('/effort_estimation')
def effort_estimation():
    return render_template('effort_estimation.html')

if __name__ == '__main__':
    app.run(debug=True)
