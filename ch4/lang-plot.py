#
# 言語判別の機械学習
# データごとの分布をグラフにする
#
# Author        :t.kurahara@gmail.com
# Create DATE   :2017/01/17
#
import matplotlib.pyplot as plt
import pandas as pd
import json

# アルファベットの出現頻度データを読み込む --- (※1)
with open("./lang/freq.json", "r", encoding="utf-8") as fp:
    freq = json.load(fp)

# 言語ごとに集計する --- (※2)
lang_dic = {}
for i, lbl in enumerate(freq[0]["labels"]):
    fq = freq[0]["freqs"][i]
    if not (lbl in lang_dic):
        lang_dic[lbl] = fq
        continue
    for idx, v in enumerate(fq):
        lang_dic[lbl][idx] = (lang_dic[lbl][idx] + v) / 2

# PandasのDataFrameにデータを入れる --- (※3)
asclist = [[chr(n) for n in range(97,97+26)]]
df = pd.DataFrame(lang_dic, index=asclist)

# プロット --- (※4)
plt.style.use('ggplot')
# df.plot(kind="bar", subplots=True, ylim=(0,0.15)) # 棒グラフ
df.plot(kind = "line") # 折れ線グラフ
plt.savefig("lang-plot.png")

