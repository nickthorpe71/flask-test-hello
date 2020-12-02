# SETUP: https://realpython.com/flask-by-example-part-1-project-setup/

from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def hello():
    return render_template("index.html")

@app.route('/bye')
def bye():
    return "Googbye"

if __name__ == '__main__':
    app.run()
