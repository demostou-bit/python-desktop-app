import sqlite3

conn = sqlite3.connect('sample.db')
cur = conn.cursor()

#データの抽出
sql = """SELECT id name
  FROM personal"""

data = cur.execute(sql)

#無限ループ
while True:
  #fetchone関数でSELECT文が抽出したデータを1個ずつ取り出す
  d = data.fetchone()
  if d == None: break #Noneが返った後にbreakでループ終了
  print(d)

conn.close()
