import concurrent.futures
import xpath_py
import csv
import datetime
baseurl="http://home.klzy.me:8085/xueqing-web/course/index/"


def get_page_url(baseurl,page) :
    print("\n[start] get_page_url: " + str(page))
    url = baseurl + str(page)
    l=xpath_py.get_url(url)
    print("\n[end] get_page_url: " + str(page))
    return l

def get_page_str(url,id):
    print("\n[start] get_page_str: " + str(id))
    r=xpath_py.list_add(url)
    print("\n[end] get_page_str: " + str(id))
    return r



# def fake_job(id, dummy_data):
#     print("[start] job: " + str(id))
#     time.sleep(4)
#     print("[end] job: " + str(id))
#     return str(id) + dummy_data + "aaa"


# 线程数
executor = concurrent.futures.ThreadPoolExecutor(max_workers=10)
futures = []
# for i in range(5):
#     f = executor.submit(fake_job, i, "lalala")
#     futures.append(f)
#
# results = [f.result() for f in futures]


if __name__=="__main__":
    starttime =datetime.datetime.now()
    for page in range(1,41):
        f = executor.submit(get_page_url,baseurl,page)
        futures.append(f)
    results = [f.result() for f in futures]

    # [print(r) for r in results]
    f2 = []
    re_html=[]
    i=0
    for r in results:
        for url in r:
            if "51job" in url:
                i=i+1
                f = executor.submit(get_page_str, url,i)
                f2.append(f)
    re_html = [f.result() for f in f2]

    # [print(r) for r in re_html]

    with open("data.csv", "w+", newline='', encoding='utf-8-sig')as  f:
        w = csv.writer(f)
        for r in re_html:
            sortedValues = xpath_py.getSortedValues(r)
            w.writerow(sortedValues)
    endtime = datetime.datetime.now()
    print(endtime - starttime)