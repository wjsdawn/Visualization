from flask import Flask
from flask import jsonify
from flask_cors import CORS, cross_origin

app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello World!'


@app.route('/msg', methods=['GET', 'POST'])
@cross_origin()
def getMsg():
    response = {
        'msg': "hello"
    }
    return jsonify(response)


if __name__ == '__main__':
    app.run()
