# run with: flask --app hello_flask --debug run 
# Link to github: https://github.com/kyle-parker-1500/cst205_wk10c1_lab

from flask import Flask, render_template
from flask_bootstrap import Bootstrap5

app = Flask(__name__)
bootstrap = Bootstrap5(app)

# task 2 at root
@app.route('/')
def hello():
    return "<p>Alex T. : ASAP</p>"

# task 3 at template
@app.route('/kyle')
def t_test():
   return render_template('test_template.html')

# task 4
@app.route('/bootstrap')
def boostrap():
    return render_template('test_bootstrap.html')
