import json

from flask import Flask
from flask import jsonify
from flask_cors import CORS, cross_origin
import pymongo
import pickle
import pandas
from GH import MapMatching as matcher

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
    arr = json.loads(arr_point)

    body = {
        'ak': matcher.read_key(),
        'point_list': matcher.create_point_json(arr),
        'rectify_option': "need_mapmatch:1|transport_mode:driving|denoise_grade:1|vacuate_grade:1",
        'supplement_mode': "driving",
        'coord_type_output': "gcj02"
    }
    url = "https://api.map.baidu.com/rectify/v1/track?"
    res_json = matcher.request_post(url, body)

    data = {
        "id": coll["name"],
        "begin_pos": coll["begin_pos"],
        "end_pos": coll["end_pos"],
        "route": matcher.get_matching_points(res_json)
    }
    return jsonify(data)


@app.route('/test_route', methods=['GET', 'POST'])
@cross_origin()
def test_route():
    data = pandas.read_csv('./public/resFile.txt')
    arr_point = data.to_json(orient='values')
    return jsonify(arr_point)


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
