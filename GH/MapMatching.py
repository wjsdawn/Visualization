import json
import pickle

import pandas
import requests
from requests import RequestException
import Database

def read_key(filename):
    with open(filename, 'r', encoding='utf-8') as f:
        key = f.read()
        return key


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


def parse_json(content_json):
    """  解析json函数 """
    result_json = json.loads(content_json)
    return result_json


# arr坐标点数组
def request_post(url, data):
    response = requests.post(url, data=data)
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
    route = df.loc[:, 'loc_time':'latitude']
    arr_points = route.to_json(orient="values")
    return arr_points

# def test():
#     coll = Database.get_coll()
#     data = coll.find_one()
#     df = pickle.loads(data["route"])
#     arr_point = df.to_json(orient="values")
#     arr = json.loads(arr_point)
#
#     body = {
#         'ak': read_key(),
#         'point_list': create_point_json(arr),
#         'rectify_option': "need_mapmatch:1|transport_mode:driving|denoise_grade:1|vacuate_grade:1",
#         'supplement_mode': "driving",
#         'coord_type_output': "gcj02"
#     }
#     url = "https://api.map.baidu.com/rectify/v1/track?"
#     res_json = request_post(url, body)
#     get_matching_points(res_json)
#
#
# test()
