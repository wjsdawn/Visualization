import time
from datetime import datetime
import pandas
import json
import GH.MapMatching as matcher

pd = pandas.read_csv("./routename.txt", delimiter=' ', encoding='utf-8')
pd['time'] = pandas.to_datetime(pd['time'], unit='s')

low = datetime(2018, 5, 1, 8, 0, 0)
height = datetime(2018, 5, 1, 8, 30, 0)


def deliver(low, heigth):
    target = pd[(pd['time'] >= low) & (pd['time'] <= height)]
    group = target.groupby('id')
    car_route = []
    car_flow = []
    for key, value in group:
        group_route = value.groupby('routename')
        for r_key, r_value in group_route:
            # r_value['speed'] = pandas.to_numeric(r_value['speed'])
            aver_speed = r_value['speed'].mean()
            route_name = r_key
            route = [key, route_name, aver_speed]
            car_route.append(route)
    res_route = pandas.DataFrame(car_route, columns=['id', 'route', 'speed'])

    car_route = []
    group_route = res_route.groupby('route')
    for key, value in group_route:
        if len(value) >= 8:               # 车的数量大于8
            route_speed_aver = value['speed'].mean()  # 计算平均值
            car_route.append([key, route_speed_aver])
        flow = (key, len(value))
        car_flow.append(flow)

    res_route = pandas.DataFrame(car_route, columns=['route', 'speed'])
    res_route = res_route.sort_values(by='speed')
    res_route.to_csv('./route_speed.csv', encoding='utf-8')
    return car_flow




deliver(low, height)
# for key, value in group:
#     group_car = value.groupby('routename')
#     for r_key, r_value in group_car:
#         print(r_value)
#     break