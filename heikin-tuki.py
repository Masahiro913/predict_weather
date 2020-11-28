# -*- coding: utf-8 -*-
import matplotlib.pyplot as plt
import pandas as pd
#CSVを読み込む
df = pd.read_csv("kion10y.csv", encoding = "utf-8")
g = df.groupby(['月'])["気温"]
gg = g.sum() / g.count()
#結果を出力
print(gg)
gg.plot()
plt.savefig("tenki-heikin-tuki.png")
plt.show()

#月ごとによる平均の算出
#月
#1      5.996481
#2      6.598714
#3     10.017009
#4     14.481515
#5     19.607918
#6     22.544848
#7     26.422287
#8     27.887097
#9     24.360303
#10    19.155132
#11    13.484545
#12     8.653079