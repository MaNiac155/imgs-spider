import urllib.request as ul
from bs4 import BeautifulSoup as bf

error_pages=[]


def check_page(str):
    new_url="http://www.cse.zju.edu.cn"+str
    try:
        nhtml = ul.urlopen(new_url)
    except:
        return 0
    soup = bf(nhtml.read(), 'html.parser')
    imgs=soup.find_all('img')
    imgs.pop(-1)
    for img in imgs:
        src_str=img['src']
        if "/_upload"!=src_str[:8]:
            if new_url not in error_pages:
                error_pages.append(new_url)
                print("error in "+new_url)
    print("page check!")



for i in range(98,99):

    url = "http://www.cse.zju.edu.cn/39283/list" + str(i) + ".htm"
    html = ul.urlopen(url)
    obj = bf(html.read(), 'html.parser')
    n = obj.body.section
    list_a = n.find_all("a")

    for link in list_a[2:-10]:
        check_page(link['href'])

for item in error_pages:
    print(item)