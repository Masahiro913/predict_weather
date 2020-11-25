# -*- coding: utf-8 -*-
import pandas as pd

#pandasでcsvファイルを読み込む
df = pd.read_csv("kion10y.csv", encoding="utf-8")

#日付ごとに気温をリストにまとめる
md = {}
for i, row in df.iterrows():
  m, d, v = (int(row['月']), int(row['日']), float(row['気温']))
  key = str(m) + "/" + str(d)
  if not(key in md): md[key] = []
  md[key] += [v]

#日付ごとに平均を求める
avs = {}
for key in md:
  v = avs[key] = sum(md[key]) / len(md[key])
  print("{0} : {1}".format(key, v))

