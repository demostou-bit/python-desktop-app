#sample.db内のpersonalテーブルを削除
import sqlite3

conn = sqlite3.connect('sample.db')
cur = conn.cursor()

#personalテーブルの削除
cur.execute("DROP TABLE personal")

#テーブル削除の処理をデータベースに反映させる
conn.commit()

conn.close()
