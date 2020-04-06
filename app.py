from flask import Flask, render_template

app = Flask(__name__, static_folder='img')


@app.route('/')
def index():
    return "Hello world"

@app.route('/Day1')
def Day1():
    return render_template('Day1/Day1.html')

@app.route('/Day2')
def Day2():
    return render_template('Day2/index.html')

@app.route('<name>')
def router():
    return render_template('%s' % name)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=True)
