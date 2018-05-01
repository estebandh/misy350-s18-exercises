from flask import Flask, render_template
app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/user')
def user():
    return "<h2>This is the page for users<h2>"

@app.route('/users/<string:name>')
def get_user_name(name):
    return render_template('user.html', uname=name)
    #return "Hello %s" % name

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001)
