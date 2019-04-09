from lxml import etree
import requests
def remove(s):
    return s.replace("\t","").replace("\n","").replace("\r","")

def get_html(url):
    return requests.get(url).text

html=etree.HTML(get_html("http://home.klzy.me:8085/xueqing-web/51job/98287424.html"))
s="".join(html.xpath("//div[@class='bmsg job_msg inbox']//text()"))
print(remove(s))