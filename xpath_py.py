from lxml import etree
import datetime
import requests
from bs4 import BeautifulSoup
import re

def get_url(url):
    soup = BeautifulSoup(gethtml(url), 'html5lib')
    soup = soup.find_all("a")
    l2=[]
    for l in soup:
        l2.append('http://10.255.46.97:8085'+l["href"])
        # l2.append('http://home.klzy.me:8085' + l["href"])
    return l2

def getSortedValues(row):
    sortedValues=[]#初始化为空list
    keys=row.keys()
    for key in keys:
        sortedValues.append(row[key])
    return sortedValues


def gethtml(url):
    headers = {
        'Connection': 'close',
    }
    s = requests.Session()
    tiantian_data = None
    with requests.Session() as s:
        result_data = s.get(url, headers=headers)
    return result_data.text


def re_get(url,s_re):
    try:
        s = re.findall(s_re, gethtml(url))[0]
    except:
        return ""
    return remove_char(s)

def remove_char(str):
    return str.replace('\t', '').replace('\n', '').replace('\r', '').replace('\xa0', '').replace(' ', '')


def get_text(url,xpath):
    html = etree.HTML(gethtml(url))
    try:
        html_data=html.xpath(xpath)[0]
    except:
        return ""
    return remove_char(html_data)

def list_add(url):
    dict={}
    dict["jobname"]=get_text(url,"//div[@class='cn']/h1/text()")
    dict["date"]=re_get(url,"<em class=\"i4\"></em>([^<]+)</span>")
    dict["companymess"]=get_text(url,"//p[@class='msg ltype']/text()")
    dict["salary"]=get_text(url,"//div[@class='cn']/strong/text()")
    dict["location"]=get_text(url,"//span[@class='lname']/text()")
    dict["company"]=get_text(url,"//p[@class='cname']/a/text()")
    dict["experience"]=re_get(url,"<em class=\"i1\"></em>([^<]+)</span>")
    dict["education"]=re_get(url,"<em class=\"i2\"></em>([^<]+)</span>")
    dict["amount"]=re_get(url,"<em class=\"i3\"></em>([^<]+)</span>")
    dict["description"]=get_text(url,"//div[@class='bmsg job_msg inbox']/text()")
    dict["category"]=get_text(url,"//span[@class='el']/text()")
    return dict

# url="https://home.klzy.me:8086/xueqing-web/51job/72396849.html"
# print(list_add(url))

if __name__=="__main__":
    l=list_add("http://home.klzy.me:8085/xueqing-web/51job/97244043.html")
    print(l)