import time
from datetime import datetime
from datetime import timedelta

import numpy
import pandas
import json
import GH.MapMatching as matcher

# pd = pandas.read_csv("./routename.txt", delimiter=' ', encoding='utf-8')
# # pd['time'] = pandas.to_datetime(pd['time'], unit='s', utc=True).tz_convert('Asia/Shanghai')
#
#
# begin = datetime(2018, 5, 1, 0, 0, 0)
# end = datetime(2018, 5, 1, 1, 0, 0)
#
#
# def deliver(plow, phigh, name):
#     target = pd[(pd['time'] >= plow) & (pd['time'] <= phigh)]
#     group = target.groupby('id')
#     car_route = []
#     car_flow = []
#
#     # 计算每辆车每条路上的平均速度
#     for key, value in group:
#         group_route = value.groupby('routename')
#         for r_key, r_value in group_route:
#             # r_value['speed'] = pandas.to_numeric(r_value['speed'])
#             aver_speed = r_value['speed'].mean()
#             route_name = r_key
#             route = [key, route_name, aver_speed]
#             car_route.append(route)
#     res_route = pandas.DataFrame(car_route, columns=['id', 'route', 'speed'])
#
#     car_route = []
#     group_route = res_route.groupby('route')
#     for key, value in group_route:
#         if len(value) >= 8:               # 车的数量大于8
#             route_speed_aver = value['speed'].mean()  # 计算平均值
#             car_route.append([key, route_speed_aver, len(value)])
#         flow = (key, len(value))
#         car_flow.append(flow)
#
#     res_route = pandas.DataFrame(car_route, columns=['route', 'speed', 'carsnum'])
#     res_route = res_route.sort_values(by='speed')
#     res_route['route'] = res_route['route'].map(lambda x: str(x)[9:]) # 去掉道路中的四川省成都市双流区
#     res_route.to_csv("./30route/"+str(name)+".csv", encoding='utf-8')
#     return car_flow


def merge():
    df = pandas.read_csv("./30route/1.csv", delimiter=",", encoding="utf-8")
    df.rename(columns={'Unnamed: 0':'time_range'}, inplace=True)
    df['time_range'] = 1
    print(df)
    for i in range(2, 25):
        filename = "./30route/"+str(i)+".csv"
        pd = pandas.read_csv(filename, delimiter=",", encoding="utf-8")
        pd.rename(columns={'Unnamed: 0':'time_range'}, inplace=True)
        pd['time_range'] = i
        df = pandas.concat([df, pd])
    df.to_csv('./30route/allroute.txt', index=None)


def sort(filename):
    df = pandas.read_csv(filename, delimiter=",", encoding="utf-8")
    group = df.groupby("route")
    loc_pos = 0
    route_name = []
    all_data = []
    for key, value in group:
        route_name.append(key)
        value['time_range'] = value['time_range']-1
        value['loc_pos'] = loc_pos
        loc_pos = loc_pos+1
        data = value.loc[:, ['time_range', 'loc_pos', 'speed']]
        data["speed"] = data["speed"].astype(int)
        np = numpy.array(data)
        np = np.tolist()
        for i in range(len(np)):
            all_data.append(np[i])
    print(all_data)
    return route_name, all_data


sort("./30route/allroute.txt")
# for i in range(1, 25):
#     first = int(time.mktime(time.strptime(begin.strftime("%Y-%m-%d %H:%M:%S"), "%Y-%m-%d %H:%M:%S")))
#     sec = int(time.mktime(time.strptime(end.strftime("%Y-%m-%d %H:%M:%S"), "%Y-%m-%d %H:%M:%S")))
#     deliver(first, sec, i)
#     begin = begin+timedelta(hours=1)
#     end = end+timedelta(hours=1)

