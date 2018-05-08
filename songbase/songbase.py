from flask import Flask, render_template
from flask import request
app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


#@app.route('/user')
#def user():
#    return "<h2>This is the page for users<h2>"

@app.route('/user/<string:name>')
def get_user_name(name):
    return render_template('user.html', uname=name)
    #return "Hello %s" % name

@app.route('/name-form', methods=['GET', 'POST'])
def form():
    if request.method == 'GET':
        first_name = request.args.get('first_name')
        return render_template('form-basics.html', first_name='first_name')
    if request.method == 'POST':
        first_name = request.form['first_name']
        return render_template('form-basics', first_name='first_name')

@app.route('/form-demo')
def form_response():
    first_name = request.args.get('first_name')
    return first_name

@app.route('/email-form', methods=['GET', 'POST'])
def emailForm():
    return render_template('email-form.html')

@app.route('/form')
def formPlaceHolder():
    return "<h1> you have submitted the form <h1>"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001)
