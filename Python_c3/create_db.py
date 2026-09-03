import sqlite3

#データベースに接続（存在しない場合は作成）
db_name = 'sample.db'
conn = sqlite3.connect(db_name)

#接続の切断
conn.close()