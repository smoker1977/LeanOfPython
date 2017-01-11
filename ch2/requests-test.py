# 現在時刻を取得する
import requests
r = requests.get("http://api.aoikujira.com/time/get.php")

# 対象URL
print("対象URL：" + r.url)

# テキスト形式でデータを得る
text = r.text
print("TEXT\n" + text)

# バイナリ形式でデータを得る
bin = r.content
print("BINARY")
print(bin)
