import json


def test():
    list_data=[]
    for i in range(5):
        list_data.append({"jobname": "java开发工程师"+str(i)})
    list_date=[]
    for _ in range(5):
        list_date.append({"faburiqi":"03-21"})
    list_series_data=[2,1,34,324]
    list_series=[{"name":"java开发工程师","type":"line","stack":"总量","data":list_series_data}]
    dict_json={}
    dict_json["name"]="游戏开发"
    dict_json["data"]=list_data
    dict_json["date"]=list_date
    dict_json["series"]=list_series
    j=json.dumps(dict_json)
    return j


def make_json(name,data:list,date,series):
    dict_json={"name":name,"data":data,"date":date,"series":series}
    j = json.dumps(dict_json)
    return j

