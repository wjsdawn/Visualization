from flask import Flask
from flask import jsonify
from flask_cors import CORS, cross_origin
import pymongo
import pickle

client = pymongo.MongoClient(host='localhost', port=27017)
db = client.CarRoute
collection = db.get_collection("cars")

app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello World!'


@app.route('/send_data')
def send_data():
    coll = collection.find_one()
    df = pickle.loads(coll["route"])
    arr_point = df.to_json(orient="values")
    data = {
        "id": coll["name"],
        "begin_pos": coll["begin_pos"],
        "end_pos": coll["end_pos"],
        "route": arr_point
    }
    return data


@app.route('/msg', methods=['GET', 'POST'])
@cross_origin()
def getMsg():
    response = {
        'msg': "hello"
    }
    return jsonify(response)


@app.route('/send_test', methods=['GET', 'POST'])
@cross_origin()
def send_test():
    data = {}
    response = {}
    coll = collection.find()
    for item in coll:
        df = pickle.loads(item["route"])
        arr_point = df.to_json(orient="values")
        data['name'] = item['name']
        data['begin_pos'] = item['begin_pos']
        data['end_pos'] = item['end_pos']
        data['route'] = arr_point
        response[item['name']] = data
    return jsonify(response)


if __name__ == '__main__':
    app.run()
