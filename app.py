from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World!'


@app.route('/semantic-release')
def semantic_release():
    return 'Semantic Release'

if __name__ == '__main__':
    app.run(debug=True)
