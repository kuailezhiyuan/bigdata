from lxml import etree
import requests
from bs4 import BeautifulSoup
import re

def gethtml(url):
    r=requests.get(url).text
    return r

def re_get(url,s_re):
    try:
        s = re.findall(s_re, gethtml(url))[0]
        s.replace('\t', '').replace('\n', '').replace('\r', '').replace('\xa0', '').replace('|', '').strip()
    except:
        return ""
    return s


def get_text(url,xpath):
    try:
        html=etree.HTML(gethtml(url))
        html_data=html.xpath(xpath)[0]
    except:
        return ""
    return html_data.replace('\t', '').replace('\n', '').replace('\r', '').replace('\xa0', '').replace('|', '').strip()
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