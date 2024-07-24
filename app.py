from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World!'

@app.route('/new-one')
def hello_world():
    return 'a whole new world!'


if __name__ == '__main__':
    app.run(debug=True)
