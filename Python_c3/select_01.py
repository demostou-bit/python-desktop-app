import sqlite3

conn = sqlite3.connect('sample.db')
cur = conn.cursor()

#データの抽出
#変数sqlにSELECT文を使うSQL文を格納
sql = """SELECT id , name
  FROM personal"""

#execute関数でSQL文を実行
data = cur.execute(sql)

list = data.fetchall()
for row in list:
  print(row)

conn.close()
