import sqlite3

#コネクションオブジェクトの作成
conn = sqlite3.connect('sample.db')

#カーソルオブジェクトの作成
cur = conn.cursor()

#データの追加
#データを1件追加
sql = """INSERT INTO personal
  VALUES(
    '001',
    'Yamada Taro',
    173,
    62.5)"""
cur.execute(sql)
#データを1件追加
sql = """INSERT INTO personal
  VALUES(
    '002',
    'Tanaka Hanako',
    163,
    53.1)"""
cur.execute(sql)
#データを1件追加
sql = """INSERT INTO personal
  VALUES(
    '003',
    'Suzuki Saburo',
    180,
    75.8)"""
cur.execute(sql)

#コミットを行うことでデータベースに反映させる
conn.commit()

print('personalテーブルにデータを追加しました。')

conn.close()
