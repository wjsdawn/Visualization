import json
import pickle

import pandas
import requests
from requests import RequestException
import Database


# 获取百度地图的key
def read_key(filename):
    with open(filename, 'r', encoding='utf-8') as f:
        key = f.read()
        return key


# 处理get请
def request_url_get(url):
    """ get请求 """
    try:
        r = requests.get(url=url, timeout=30)
        if r.status_code == 200:
            return r.text
        return None
    except RequestException:
        print("请求url返回异常")
        return None


# arr坐标点数组
def request_post(url, data):
    response = requests.post(url, data=data)
    if response.status_code == 200:
        return response.json()
    else:
        print("请求失败："+response.status_code)
        return None


def request_get(url, data):
    response = requests.get(url, data=data)
    if response.status_code == 200:
        return response.json()
    else:
        print("请求失败："+response.status_code)
        return None


def create_point_json(points):
    points_json = []
    for point in points:
        point_json = {'longitude': point[1], 'latitude': point[2], 'coord_type_input': 'gcj02', 'loc_time': point[0]}
        points_json.append(point_json)
    points_json = json.dumps(points_json)
    return points_json


def get_matching_points(points):
    res = points['points']
    df = pandas.DataFrame(res)
    print(df)
    route = df.loc[:, ['longitude','latitude']]
    arr_points = route.to_json(orient="values")
    return arr_points


def get_car_msg(points):
    res = points['points']
    df = pandas.DataFrame(res)
    route = df.loc[:, ['loc_time', 'longitude', 'latitude', 'speed', 'direction']]
    arr_points = route.to_json(orient="values")
    return json.loads(arr_points)


def matching_street(arr_points):
    url = "https://api.map.baidu.com/reverse_geocoding/v3/?"
    for point in arr_points:
        data = {'ak': read_key("../public/user_key"), 'output': 'json', 'coordtype': 'gcj02ll',
                'location': str(point[2]) + "," + str(point[1])}
        response = requests.get(url, params=data)
        res_json = response.json()
        point.append(res_json['result']['formatted_address'])
    return arr_points
#
#
# def test():
#     coll = Database.get_coll()
#     data = coll.find_one()
#     df = pickle.loads(data["route"])
#     arr_point = df.to_json(orient="values")
#     arr = json.loads(arr_point)
#
#     body = {
#         'ak': read_key("../public/user_key"),
#         'point_list': create_point_json(arr),
#         'rectify_option': "need_mapmatch:1|transport_mode:driving|denoise_grade:1|vacuate_grade:1",
#         'supplement_mode': "driving",
#         'coord_type_output': "gcj02"
#     }
#
#     url = "https://api.map.baidu.com/rectify/v1/track?"
#     res_json = request_post(url, body)
#     print(matching_street(get_car_msg(res_json)))
#
#
#
# test()
