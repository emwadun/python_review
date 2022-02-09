from distutils.log import debug
from flask import Flask

app = Flask(__name__)

def index():
    return "hello world"

if __name__ == "__main__":
 app.run(debug = True)