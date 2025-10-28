# run with: flask --app hello_flask --debug run 

from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
    return 'Hello world from Flask!'

@app.route('/welcome')
def wc():
    s1 = 'Welcome to my page! '
    s2 = 'Have a nice day!'
    return s1 + s2
