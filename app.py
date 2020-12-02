# SETUP: https://realpython.com/flask-by-example-part-1-project-setup/

from flask import Flask
app = Flask(__name__)


@app.route('/')
def hello():
    return "Hello World!"

if __name__ == '__main__':
    app.run()
