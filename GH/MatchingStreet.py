import json
import urllib.request
import math

import numpy


def z_turn(x, y):
    # gcj02坐标转百度坐标
    z = math.sqrt(x * x + y * y) + 0.00002 * math.sin(y * math.pi)
    theta = math.atan2(y, x) + 0.000003 * math.cos(x * math.pi)
    bd09_Lng = z * math.cos(theta) + 0.0065
    bd09_Lat = z * math.sin(theta) + 0.006
    lat = str(bd09_Lng)
    lng = str(bd09_Lat)
    return lat, lng


def Format(lat, lng):
    # 导入百度地图API,AK
    url = "http://api.map.baidu.com/geocoder/v2/?location=" + lat + "," + lng + "&iDU5Gn9U217Lf8O5FcyRZMtOFml2RWvU"
    req = urllib.request.urlopen(url)  # json格式的返回数据
    res = req.read().decode("utf-8")  # 将其他编码的字符串解码成unicode
    m = json.loads(res)
    jsonResult = m.get('result')
    address = jsonResult.get('addressComponent')
    # 省
    province = address.get('province')
    # 城市
    city = address.get('city')
    # 县区
    district = address.get('district')
    # 街道
    street = address.get('street')
    # 街道编号
    street_n = address.get('streetNumber')
    print("省（直辖市）：{0}，市：{1}，县（区）：{2}，街道：{3}，街道编码：{4}".format(province, city, district, street, street_n))


if __name__ == '__main__':
    # x = float(input())
    # y = float(input())
    #
    # '''
    # 测试数据
    # x = 39.90733345
    # y = 116.391244079988
    # '''
    # lat, lng = z_turn(x, y)
    # Format(lat, lng)
    np = numpy.loadtxt(r'../public/resFile.txt', delimiter=',')
    for arr in np:
        lat, lng = z_turn(arr[1], arr[0])
        Format(lat, lng)
