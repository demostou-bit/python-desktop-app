#ワイルドカードを使って全ての列と行のデータを取得して表示
import sqlite3

conn = sqlite3.connect('sample.db')
cur = conn.cursor()

#ワイルドカードを使う
sql = """SELECT *
  FROM personal"""

for row in cur.execute(sql):
  print(row)

conn.close()
