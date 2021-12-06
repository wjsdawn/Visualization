import json
import pickle
import time
import pandas
import Database
import GH.MapMatching as matcher

timer = 0
err_count = 0
key_pos = 0
ss = True


def encapsulate_daidu():
    global timer
    global err_count
    global key_pos
    coll = Database.get_coll()
    data = coll.find()
    count = coll.count_documents(filter={})
    ak = "iDU5Gn9U217Lf8O5FcyRZMtOFml2RWvU"
    while timer <= count:
        print(str(timer) + ":" + data[timer]["name"])
        df = pickle.loads(data[timer]["route"])
        arr_point = df.to_json(orient="values")
        arr = json.loads(arr_point)
        body = {
            'ak': ak,
            'point_list': matcher.create_point_json(arr),
            'rectify_option': "need_mapmatch:1|transport_mode:driving|denoise_grade:1|vacuate_grade:1",
            'supplement_mode': "driving",
            'coord_type_output': "gcj02"
        }

        url = "https://api.map.baidu.com/rectify/v1/track?"
        res_json = matcher.request_post(url, body)
        try:
            time_points = matcher.get_matching_time_points(res_json)
            detail_points = matcher.get_car_msg(res_json)
            if time_points is None or detail_points is None:
                timer = timer + 1
                time.sleep(1)
                continue
            if time_points == False or detail_points == False:
                time.sleep(10)
                continue
            with open('./detail.txt', 'a', encoding='utf-8') as dp:
                for point in detail_points:
                    if len(point) > 3:
                        line = data[timer]["name"] + " " + str(point[0]) + " " + str(point[1]) + " " + str(
                            point[2]) + " " + str(point[3]) + " " + str(point[4]) + '\n'
                        dp.write(line)
                    else:
                        line = data[timer]["name"] + " " + str(point[0]) + " " + str(point[1]) + " " + str(
                            point[2]) + " " + str(0) + " " + str(0) + '\n'
                        dp.write(line)
            with open('./output.txt', 'a', encoding='utf-8') as fp:
                for point in time_points:
                    line = data[timer]["name"] + " " + str(point[0]) + " " + str(point[1]) + " " + str(point[2]) + '\n'
                    fp.write(line)
            time.sleep(0.7)
            fp.close()
            dp.close()
            timer = timer + 1
        except TypeError:
            print("出错了")
            time.sleep(60)
            continue
        except KeyError:
            print("出错了")
            time.sleep(60)
            continue


def append_route_name():
    global ss
    global timer
    res = pandas.read_csv("./detail.txt", delimiter=" ")
    group = res.groupby('id')
    for key,value in group:
        if timer < 18574:
            timer = timer+1
            continue
        if timer > 20999:
            break
        print(str(timer) + ":   " + key)
        str_points = value.to_json(orient="values")
        arr_points = json.loads(str_points)
        back = matcher.matching_street_name(arr_points, "iDU5Gn9U217Lf8O5FcyRZMtOFml2RWvU")
        if not back:
            break
        with open("./routename.txt", 'a', encoding="utf-8") as fp:
            for point in arr_points:
                line = str(point[0])+" "+str(point[1])+" "+str(point[2])+" "+str(point[3])+" "+str(
                    point[4])+" "+str(point[5])+" "+str(point[6])+"\n"
                fp.write(line)
        fp.close()
        timer = timer + 1


append_route_name()

# pd = pandas.read_csv("./output.txt", delimiter=" ")
# group = pd.groupby('id')
# for key, value in group:
#
#     data = value.loc[:, ['lon', 'lat']].to_json(orient="values")
#     arr = json.loads(data)
#     print(arr)
#     for point in arr:
#         point[0] = matcher.gcj02_to_wgs84(point[0], point[1])[0]
#         point[1] = matcher.gcj02_to_wgs84(point[0], point[1])[1]
#     route = json.dumps(arr)
#     print(route)
#     break
