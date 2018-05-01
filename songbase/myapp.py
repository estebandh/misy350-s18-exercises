import random
from flask import Flask
myapp = Flask(__name__)

@myapp.route('/')
def index():
    return "<h1>Hello Esteban Delgado<h1>"

@myapp.route('/hello')
def hello():
    greeting_list = ['Ciao', 'Hei', 'Salut', 'Hola', 'Nihao']
    return random.choice(greeting_list)
