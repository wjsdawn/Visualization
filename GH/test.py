import pandas

data = pandas.read_csv('routename.txt', delimiter=' ', encoding="utf-8")#将文件加载到pandas中
data['routename'] = data['routename'].map(lambda x: str(x)[9:])#去掉四川省成都市双流区
route = data['routename']#选取routename列
route = route.to_csv('chinesename.txt',header=None,index=None)
#     fp.write(route)