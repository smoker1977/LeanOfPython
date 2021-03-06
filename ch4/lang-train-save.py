#
# 言語判別の機械学習
# 学習済みのパラメータを保存するプログラム
#
# Author        :t.kurahara@gmail.com
# Create DATE   :2017/01/21
#
from sklearn import svm
from sklearn.externals import joblib
import json

# 各言語の頻出データ(JSON)を読み込む
with open("./lang/freq.json", "r", encoding="utf-8") as fp:
    d = json.load(fp)
    data = d[0]

# データを学習する
clf = svm.SVC()
clf.fit(data["freqs"], data["labels"])

# 学習データを保存する
joblib.dump(clf, "./cgi-bin/freq.pkl")
print("ok")

