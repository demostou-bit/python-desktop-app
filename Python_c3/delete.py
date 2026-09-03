#idが003のデータを削除する
import sqlite3

conn = sqlite3.connect('sample.db')
cur = conn.cursor()

#データの削除
sql = """DELETE FROM personal
  WHERE id = '003'""" #WHEREで指定しないと全てのデータが削除される
cur.execute(sql)

conn.commit()

#データの表示
sql = """SELECT *
  FROM personal"""
for row in cur.execute(sql):
  print(row)

conn.close()
