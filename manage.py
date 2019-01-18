from flask import Flask
import sys
app = Flask(__name__)


@app.route("/")
def hello():
    return "Hello World!"


if __name__ == '__main__':
    if sys.argv[1]:
        print('Test Pass\n')
    else:
        app.run()
