#データ部分を後から追加してSQL文を実行(プレースホルダー)

#入力されたデータを文字列としてSQL文に連結するやり方は
#SQLインジェクションの問題を引き起こす
#そこでプレースホルダーを使い、SQL文を作る

import sqlite3

conn = sqlite3.connect('sample.db')
cur = conn.cursor()

p_data = ('Yamazaki Takashi', 172, 59.3)

#プレースホルダーを使う
#シングルクォーテーションのつけ忘れがあると
#sqlite3.OperationalError: unrecognized token:となる
sql = """INSERT INTO personal
  VALUES(
    '004',
    ?,
    ?,
    ?)"""
cur.execute(sql, p_data)
conn.commit()

sql = """SELECT * FROM personal
  ORDER BY id"""
for row in cur.execute(sql):
  print(row)
print() #改行

id = ('002', )

#プレースホルダーを使う
#idが002のデータだけを表示
sql = """SELECT * FROM personal
  WHERE id = ?"""
cur.execute(sql, id)
print(cur.fetchone())

conn.close()
