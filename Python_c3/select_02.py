#for文でexecute関数を実行
import sqlite3

conn = sqlite3.connect('sample.db')
cur = conn.cursor()

#データの抽出
sql = """SELECT id, name
  FROM personal"""

#for文でexecute関数を実行
for row in cur.execute(sql):
  print(row)

conn.close()
