# run with: flask --app hello_flask --debug run 

from flask import Flask, render_template
from flask_bootstrap import Bootstrap5

app = Flask(__name__)

# task 2 at root
@app.route('/')
def hello():
    return "<p>Alex T. : ASAP</p>"

# task 3 at template
@app.route('/kyle')
def t_test():
   return render_template('test_template.html')


