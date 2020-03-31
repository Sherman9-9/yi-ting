from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/Day1')
def index():
    return render_template('Day1/Day1.html')

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
