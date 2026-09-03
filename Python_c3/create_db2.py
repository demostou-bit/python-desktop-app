import sqlite3

#データベースを作成
conn = sqlite3.connect('collection.db')
cur = conn.cursor()

#booksテーブルを作成するSQL文を文字列で定義
sql = """CREATE TABLE books (
         id INTEGER PRIMARY KEY AUTOINCREMENT,
         isbn TEXT NOT NULL,
         title TEXT NOT NULL,
         author TEXT NOT NULL,
         publisher TEXT NOT NULL,
         release TEXT NOT NULL,
         price INTEGER NOT NULL,
         image TEXT NOT NULL)"""

#SQL文を実行してbooksテーブルを作成
cur.execute(sql)

#テスト用のデータ5件
books = [
  [ '9784296102136',
    'ビジネスPython超入門',
    '中島　省吾',
    '日経BP',
    '2019年6月10日',
    2640,
    'img_001.png'],
  [ 'B07HMN68L9',
    '5日間で学ぶPython　AIプログラミング編',
    '中島　省吾',
    '日経BP',
    '2018年9月25日',
    880,
    'img_002.png'],
  [ 'B00N2NRK0K',
    'VisualC#　やりたいこと逆引き事典',
    '中島　省吾',
    '日経BP',
    '2014年8月28日',
    550,
    'img_003.png'],
  [ 'B00JQ1A9F0',
    '読むプログラミング用語辞典',
    '中島　省吾',
    '日経BP',
    '2014年4月18日',
    550,
    'img_004.png'],
  [ 'B000IN7NG4',
    'Windowsアプリを5日で作れる本',
    '中島　省吾',
    '日経BP',
    '2014年10月16日',
    550,
    'img_005.png']]

sql = """INSERT INTO books(isbn,
                           title,
                           author,
                           publisher,
                           release,
                           price,
                           image)
         VALUES (?, ?, ?, ?, ?, ?, ?)"""

for i in range(len(books)):
  cur.execute(sql, books[i])
conn.commit()

#SELECT文でテスト用のデータを確認
for row in cur.execute("SELECT * FROM books"):
  print(row)

#接続の切断
conn.close()
