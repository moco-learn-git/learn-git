from flask import Flask, render_template

app = Flask(__name__)


@app.route('/home')
def home():
    return render_template('index.html')


@app.route('/step1')
def step1():
    return render_template('step1.html')


@app.route('/step2')
def step2():
    return render_template('step2.html')


if __name__ == '__main__':
    app.run()
