import pandas
import math
def getDistanceFromLatLonInKm(lat1,lon1,lat2,lon2) : #lon>lat
    R = 6371
    lat1 = deg2rad(lat1);
    lon1 = deg2rad(lon1);
    lat2 = deg2rad(lat2);
    lon2 = deg2rad(lon2);
    dLat = abs(lat2-lat1)
    dLon = abs(lon2-lon1);
    a = math.sin(dLat/2) * math.sin(dLat/2) + math.cos(lat1) * math.cos(lat2) * math.sin(dLon/2) * math.sin(dLon/2)
    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1-a))
    d = R * c
    return d


def deg2rad(deg) :
  return deg * (math.pi/180)


def time_hour(time1,time2):
    time_span = time2 - time1
    return float(time_span/3600)


df = pandas.read_csv('./chinesename.txt', delimiter=" ")
group_id = df.groupby('id')
for key,value in group_id:
    group_route = value.groupby('routename')
    for rkey,rvalue in group_route:
        k = value.loc[:,["time", "lon", "lat"]].values.tolist()
        speedcount = 0
        for i in range(len(k)-1):
            speed = 0
            km = getDistanceFromLatLonInKm(k[i][2], k[i][1], k[i+1][2], k[i+1][1])
            time = time_hour(k[i][0],k[i+1][0])
            if time != 0:
                speed = km/time
            speedcount += speed
        if len(k) <= 1:
            continue
        res = speedcount/(len(k)-1)
        print(rkey+":"+str(res))


