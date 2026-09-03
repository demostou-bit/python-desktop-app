#personalテーブルidが002行のname列を変更
import sqlite3

conn = sqlite3.connect('sample.db')
cur = conn.cursor()

print("id が '002' の 変更前")
#データの表示
sql = """SELECT * 
  FROM personal
  WHERE id = '002'"""
cur.execute(sql)
print(cur.fetchone())
print() #改行

#idが002のname列をSasaki Jiroに変更
sql = """UPDATE personal
  SET name = 'Sasaki Jiro'
  WHERE id = '002'""" #WHEREで指定しないと全てのデータが更新対象となる
cur.execute(sql)
conn.commit()

print("id が '002' の 変更後")
#データの表示
sql = """SELECT * 
  FROM personal
  WHERE id = '002'"""
cur.execute(sql)
print(cur.fetchone())
print() #改行

conn.close()
