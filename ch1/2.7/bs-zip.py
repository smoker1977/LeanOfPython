# coding=utf-8
from bs4 import BeautifulSoup
# import urllib.request as req
import urllib2

# import urllib

url = "http://api.aoikujira.com/zip/xml/1500042"

# urlopen()でデータを取得 --- (※1)
# res = req.urlopen(url)
res = urllib2.urlopen(url)

# BeautifulSoupで解析 --- (※2)
soup = BeautifulSoup(res, 'html.parser')

# 任意のデータを抽出 --- (※3)
ken = soup.find("ken")
shi = soup.find("shi")
cho = soup.find("cho")
print( ken.string, shi.string, cho.string)
