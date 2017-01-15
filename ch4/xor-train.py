from sklearn import svm

# XORの演算結果 --- (※1)
#   XOR 演算の入力と結果の二次元のリストを定義
#   P,Q     入力データ
#   result  答え
xor_data = [
    #P, Q, result
    [0, 0, 0],
    [0, 1, 1],
    [1, 0, 1],
    [1, 1, 0]
]

# 学習させるためにデータとラベルに分ける --- (※2)
# data  = P,Q
# label = result
# fit()の仕様に合わせるために変更
data = []
label = []
for row in xor_data:
    p = row[0]
    q = row[1]
    r = row[2]
    data.append([p, q])
    label.append(r)

# データの学習 --- (※3)
# SVMアルゴリズムを選択
clf = svm.SVC()

# データの学習
# 第一引数に学習するデータの配列
# 第二引数にラベルの配列
clf.fit(data, label)

# データを予測 --- (※4)
pre = clf.predict(data)
print("入力データ:", data)
print("ラベル:", label)
print("予測結果:", pre)

# 正解と合っているか結果を確認 --- (※5)
ok = 0; total = 0
for idx, answer in enumerate(label):
    p = pre[idx]
    if p == answer: ok += 1
    total += 1
print("正解率:", ok, "/", total, "=", ok/total)


