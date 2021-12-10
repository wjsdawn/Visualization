import time
from datetime import datetime
from datetime import timedelta
import pandas
import json
import GH.MapMatching as matcher

pd = pandas.read_csv("./routename.txt", delimiter=' ', encoding='utf-8')
pd = pd.sort_values(by='time')
print(pd['time'])
print(time.localtime(1525104122))
pd['time'] = pandas.to_datetime(pd['time'], unit='s')



low = datetime(2018, 4, 30, 16, 0, 0)
high = datetime(2018, 4, 30, 16, 30, 0)


def deliver(plow, phigh, name):
    target = pd[(pd['time'] >= plow) & (pd['time'] <= phigh)]
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
    res_route['route'] = res_route['route'].map(lambda x: str(x)[9:]) # 去掉道路中的四川省成都市双流区
    res_route.to_csv("./30route/"+str(name)+".csv", encoding='utf-8')
    return car_flow


# for i in range(1, 49):
#     print(low)
#     print(high)
#     deliver(low, high, i)
#     low = low+timedelta(minutes=30)
#     high = high+timedelta(minutes=30)

