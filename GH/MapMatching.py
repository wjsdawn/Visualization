import json
import math
import pickle

import pandas
import requests
from requests import RequestException
import Database


x_pi = 3.14159265358979324 * 3000.0 / 180.0
pi = 3.1415926535897932384626  # π
a = 6378245.0  # 长半轴
ee = 0.00669342162296594323  # 偏心率平方


def _transformlng(lng, lat):
    ret = 300.0 + lng + 2.0 * lat + 0.1 * lng * lng + \
          0.1 * lng * lat + 0.1 * math.sqrt(math.fabs(lng))
    ret += (20.0 * math.sin(6.0 * lng * pi) + 20.0 *
            math.sin(2.0 * lng * pi)) * 2.0 / 3.0
    ret += (20.0 * math.sin(lng * pi) + 40.0 *
            math.sin(lng / 3.0 * pi)) * 2.0 / 3.0
    ret += (150.0 * math.sin(lng / 12.0 * pi) + 300.0 *
            math.sin(lng / 30.0 * pi)) * 2.0 / 3.0
    return ret


def _transformlat(lng, lat):
    ret = -100.0 + 2.0 * lng + 3.0 * lat + 0.2 * lat * lat + \
          0.1 * lng * lat + 0.2 * math.sqrt(math.fabs(lng))
    ret += (20.0 * math.sin(6.0 * lng * pi) + 20.0 *
            math.sin(2.0 * lng * pi)) * 2.0 / 3.0
    ret += (20.0 * math.sin(lat * pi) + 40.0 *
            math.sin(lat / 3.0 * pi)) * 2.0 / 3.0
    ret += (160.0 * math.sin(lat / 12.0 * pi) + 320 *
            math.sin(lat * pi / 30.0)) * 2.0 / 3.0
    return ret


def out_of_china(lng, lat):
    """
    判断是否在国内，不在国内不做偏移
    :param lng:
    :param lat:
    :return:
    """
    return not (lng > 73.66 and lng < 135.05 and lat > 3.86 and lat < 53.55)


# 坐标转化
def gcj02_to_wgs84(lng, lat):
    """
    GCJ02(火星坐标系)转GPS84
    :param lng:火星坐标系的经度
    :param lat:火星坐标系纬度
    :return:
    """
    if out_of_china(lng, lat):
        return [lng, lat]
    dlat = _transformlat(lng - 105.0, lat - 35.0)
    dlng = _transformlng(lng - 105.0, lat - 35.0)
    radlat = lat / 180.0 * pi
    magic = math.sin(radlat)
    magic = 1 - ee * magic * magic
    sqrtmagic = math.sqrt(magic)
    dlat = (dlat * 180.0) / ((a * (1 - ee)) / (magic * sqrtmagic) * pi)
    dlng = (dlng * 180.0) / (a / sqrtmagic * math.cos(radlat) * pi)
    mglat = lat + dlat
    mglng = lng + dlng
    return [lng * 2 - mglng, lat * 2 - mglat]


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


def get_matching_time_points(points):
    print(points)
    try:
        res = points['points']
        df = pandas.DataFrame(res)
        try:
            route = df.loc[:, ['loc_time', 'longitude', 'latitude']]
            arr_points = route.to_json(orient="values")
            return json.loads(arr_points)
        except KeyError:
            return None
    except KeyError:
        return False


def get_matching_points(points):
    res = points['points']
    df = pandas.DataFrame(res)
    route = df.loc[:, ['longitude', 'latitude']]
    arr_points = route.to_json(orient="values")
    return json.loads(arr_points)


def get_car_msg(points):
    try:
        res = points['points']
        df = pandas.DataFrame(res)
        try:
            route = df.loc[:, ['loc_time', 'longitude', 'latitude', 'speed', 'direction']]
            arr_points = route.to_json(orient="values")
            return json.loads(arr_points)
        except KeyError:
            try:
                route = df.loc[:, ['loc_time', 'longitude', 'latitude']]
                arr_points = route.to_json(orient="values")
                return json.loads(arr_points)
            except KeyError:
                return None
    except KeyError:
        return False


def matching_street_name(arr_points,ak):
    url = "https://api.map.baidu.com/reverse_geocoding/v3/?"
    for point in arr_points:
        data = {'ak': ak, 'output': 'json', 'coordtype': 'gcj02ll', 'extensions_road': True,
                'location': str(point[3]) + "," + str(point[2])}
        response = requests.get(url, params=data)
        try:
            res_json = response.json()
            point.append(res_json['result']['formatted_address'])
        except KeyError:
            return False
    return True


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
#     get_matching_time_points(res_json)
#     print(res_json)
#
#
# test()
