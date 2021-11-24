from ast import literal_eval

from flask import Flask, request, render_template
from flask import jsonify
from flask_cors import CORS, cross_origin
import pymongo
import pickle
import pandas as pd

client = pymongo.MongoClient(host='localhost', port=27017)
db = client.CarRoute
collection = db.get_collection("cars")

app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello World!'


@app.route('/send_data', methods=['GET', 'POST'])
@cross_origin()
def send_data():
    coll = collection.find_one()
    df = pickle.loads(coll["route"])
    route = df.loc[:, 2:3]
    arr_point = route.to_json(orient="values")
    data = {
        "id": coll["name"],
        "begin_pos": coll["begin_pos"],
        "end_pos": coll["end_pos"],
        "route": arr_point
    }
    return jsonify(data)


@app.route('/msg', methods=['GET', 'POST'])
@cross_origin()
def getMsg():
    response = {
        'msg': "hello"
    }
    return response


@app.route('/send_test', methods=['GET', 'POST'])
@cross_origin()
def send_test():
    response = {}
    features = []
    data = pd.read_table('output.txt', header=None, encoding='gb2312', sep=',')
    for name, time, x, y in zip(data[0], data[1], data[2], data[3]):
        features.append({'type': 'Feature',
                         'properties': {'id': name, 'time': time},
                         'geometry': {'type': 'Point', 'coordinates': [x, y]}
                         })
    response = {'type': 'FeatureCollection', 'features': features}
    # df = pd.DataFrame(response)
    # df.to_json('test.txt')
    rd = {'type': 'FeatureCollection', 'features': [features[1]]}
    return rd


@app.route('/send_point', methods=['GET', 'POST'])
@cross_origin()
def sendGoeJson():
    print(request.get_json())
    return jsonify({})

if __name__ == '__main__':
    app.run()
