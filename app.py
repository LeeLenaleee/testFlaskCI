#!flask/bin/python
from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return "Hello, World! Pep heeft corona keer twee met tico"

if __name__ == '__main__':
    app.run(debug=True)