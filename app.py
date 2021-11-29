import json
from flask import Flask, request, render_template
from flask import jsonify
from flask_cors import CORS, cross_origin
import pymongo
import pickle
import pandas
from GH import MapMatching as matcher
import pandas as pd
import time as tm

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
        'ak': matcher.read_key("./public/user_key"),
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
    features = []
    # 将时间匹配的数据返回前端
    data = pd.read_table('output.txt', header=None, encoding='gb2312', sep=',')
    for name, time, x, y in zip(data[0], data[1], data[2], data[3]):
        if (tm.localtime(time).tm_hour > request.get_json()['start']) and (
                tm.localtime(time).tm_hour < request.get_json()['end']):
            features.append({'type': 'Feature',
                             'properties': {'id': name, 'time': time},
                             'geometry': {'type': 'Point', 'coordinates': [x, y]}
                             })
    response = {'type': 'FeatureCollection', 'features': features}
    # df = pd.DataFrame(response)
    # df.to_json('test.txt')
    print(len(features))
    return response


if __name__ == '__main__':
    app.run()
