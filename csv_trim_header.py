# -*- coding: utf-8 -*-
in_file = "data.csv"
outfile = "kion10y.csv"

#CSVファイルを一行ずつ読み込み
with open(in_file, "rt", encoding="shift_JIS") as fr:
    lines = fr.readlines()

#ヘッダーを削ぎ落として、新たなヘッダーをつける
lines = ["年,月,日,気温,品質,均質\n"] + lines[5:]
lines = map(lambda v: v.replace('/',','),lines)
result = "".join(lines).strip()
print(result)

#結果をファイルへ出力
with open(outfile, "wt", encoding="utf-8") as fw:
  fw.write(result)
  print("saved")
