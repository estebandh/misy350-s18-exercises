from flask import Flask
app = Flask(__name__)


@app.route('/')
def index():
    return "<h1>This is an index page<h1> \n this message updates without reloading when debug=1"


@app.route('/user')
def user():
    return "<h2>This is the page for users<h2>"


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001)
