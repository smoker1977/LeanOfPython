import urllib.request as req
from urllib.parse import urljoin
from bs4 import BeautifulSoup

url = "http://www.aozora.gr.jp/index_pages/person148.html"
base = url
res = req.urlopen(url)
soup = BeautifulSoup(res, "html.parser")

li_list = soup.select("ol > li")
for li in li_list:
    a = li.a
    if a is not None:
        name = a.string
        href = a.attrs["href"]
        print(name, ">", urljoin(base, href))

