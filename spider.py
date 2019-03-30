from bs4 import BeautifulSoup
import requests,csv
import xpath_py
import datetime

baseurl="http://home.klzy.me:8085/xueqing-web/course/index/"


def gethtml(url):
    r=requests.get(url).text
    return r


def getlist(url):
    soup = BeautifulSoup(gethtml(url), 'html5lib')
    soup = soup.find_all("tr")
    re_list = []
    for s in soup:
        s = s.find_all(['td', "p"])[1:]
        list1 = []
        for l in s:
            l = l.text
            list1.append(l.replace('\t', '').replace('\n', ''))
        re_list.append((list1))
    return re_list
# def getjobinfo(url):


def get_url(url):
    soup = BeautifulSoup(gethtml(url), 'html5lib')
    soup = soup.find_all("a")
    l2=[]
    for l in soup:
        l2.append('http://home.klzy.me:8085'+l["href"])
    return l2


def getSortedValues(row):
    sortedValues=[]#初始化为空list
    keys=row.keys()
    for key in keys:
        sortedValues.append(row[key])
    return sortedValues


if __name__ =="__main__":
    t=[]
    t2=[]
    starttime = datetime.datetime.now()
    # get_url("https://home.klzy.me:8086/xueqing-web/course/index/1")



    for page in range(1,41):
        url=baseurl+str(page)
        t=t+ get_url(url)
    print(t)
    i=0
    for url in t:
        if "51job" in url:
            t2.append(xpath_py.list_add(url))
            i = i + 1
            print(url,i,)

    # t=getlist("https://home.klzy.me:8086/xueqing-web/course/index/1")
    # print(t)
    with open("data.csv","w+",newline='',encoding='utf-8-sig')as  f:
        w=csv.writer(f)
        for row in t2:
            sortedValues = getSortedValues(row)
            w.writerow(sortedValues)

    endtime = datetime.datetime.now()
    print (endtime - starttime)
