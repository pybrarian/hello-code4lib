from flask import Flask

app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello Code4Lib!'


@app.route('/cool')
def cool():
    return 'Very cool!'


if __name__ == '__main__':
    app.run()
