import test
from modle import db,Job
# test=db.session.query(Job).filter(Job.company.like("%云计算%")).all()
# print(test)

# from sqlalchemy import or_
#
# words = ['%开发%', '%架构%',"%销售%"]
#
# # print(*[Job.jobName.like(w) for w in words])
# rule = or_(*[Job.jobName.like(w) for w in words])
# # print(rule)
# t2=Job.query.filter(rule)
# print(len(t2.all()))

# print(db.session.query(Job).params(company="深圳市腾讯计算机系统有限公司").all())

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


def make_list_data(list_Jobname):
    re_list=[]
    for l in list_Jobname:
        re_list.append({"jobname": l})
    return re_list


def make_list_series(name,list_series_data:list):
    list_series = [{"name": name, "type": "line", "stack": "总量", "data": list_series_data}]
    return list_series


def make_json(name:str,data:list,date:list,series:list):
    dict_json={"name":name,"data":data,"date":date,"series":series}
    j = json.dumps(dict_json)
    return j


def make_dict(name:str,data:list,date:list,series:list):
    dict_json={"name":name,"data":data,"date":date,"series":series}
    return dict_json


def test_make():
    list_jobname=[]
    r= db.session.query(Job).all()
    for l in r:
        list_jobname.append(l.jobName)
    list_jobname=list(set(list_jobname))
    dict_job_num={}
    for l in list_jobname:
        r=db.session.query(Job).filter(Job.jobName==l).all()
        dict_job_num[l]=len(r)
    # print(dict_job_num)
    series_list=[]
    for key,value in dict_job_num.items():
        series_list.append(make_list_series(key,value))
    # j=make_json("岗位变化曲线",make_list_data(dict_job_num.keys()),["3-11"],series_list)
    j= make_dict("岗位变化曲线", make_list_data(dict_job_num.keys()), ["3-11"], series_list)
    return j


