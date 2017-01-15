#
# アヤメの品種分類
#
# Author        :t.kurahara@gmail.com
# Create DATE   :2017/01/15
# Update DATE   :2017/01/15
from sklearn import svm, metrics
import random, re

# 定数
filename = "iris.csv"
splitWords = ','
fileOpenMode = "r"
EnCode = "utf-8"


# アヤメのCSVデータを読み込む --- (※1)
csv = []
with open(filename, fileOpenMode,  encoding=EnCode) as fp:
    # 一行ずつ読む
    for line in fp:
        line = line.strip()    # 改行を削除
        cols = line.split(splitWords) # カンマで区切る
        # 文字列データを数値に変換
        fn = lambda n : float(n) if re.match(r'^[0-9\.]+$', n) else n
        print("fn:", fn)
        print("cols:", cols)
        cols = list(map(fn, cols))
        print("new cols", cols)
        csv.append(cols)

# 先頭のヘッダ行を削除
del csv[0]

# データをシャッフル --- (※2)
random.shuffle(csv)

# 学習用とテスト用に分割する(2:1の比率) --- (※3)
# 全件数：150件
# 学習データ：100件
# 試験データ： 50件
total_len = len(csv)
print("total_len:", total_len)
train_len = int(total_len * 2 / 3)
print("train_len:", train_len)
train_data = []
train_label = []
test_data = []
test_label = []
for i in range(total_len):
    data  = csv[i][0:4]
    label = csv[i][4]
    if i < train_len:
        train_data.append(data)
        train_label.append(label)
    else:
        test_data.append(data)
        test_label.append(label)

# データを学習し、予測する --- (※4)
clf = svm.SVC()
clf.fit(train_data, train_label)
pre = clf.predict(test_data)

# 正解率を求める --- (※5)
ac_score = metrics.accuracy_score(test_label, pre)
print("正解率=", ac_score)
