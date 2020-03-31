from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/Day1')
def Day1():
    return render_template('Day1.html')

if __name__ == "__main__":
    app.run()
