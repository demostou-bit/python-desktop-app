#REPLACE INTO文を使う
import sqlite3

conn = sqlite3.connect('sample.db')
cur = conn.cursor()

#既存のデータの一部を変更
sql = """REPLACE INTO personal
  VALUES (
    '002',
    'Tanaka Hanako',
    163,
    53.1)"""
cur.execute(sql)

#新規に1個のデータを追加
sql = """REPLACE INTO personal
  VALUES (
    '003',
    'Suzuki Saburo',
    180,
    75.8)"""
cur.execute(sql)

conn.commit()

#データの表示
sql = """SELECT * FROM personal
  ORDER BY id"""
for row in cur.execute(sql):
  print(row)

conn.close()

