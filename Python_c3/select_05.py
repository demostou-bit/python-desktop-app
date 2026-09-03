#WHERE句を使う
import sqlite3

conn = sqlite3.connect('sample.db')
cur = conn.cursor()

print("idが '002' と等しい行")
sql = """SELECT *
  FROM personal
  WHERE id = '002' """ #WHERE句を使う
for row in cur.execute(sql):
  print(row)
print() #改行

print("heightが 173 以上の行")
sql = """SELECT *
  FROM personal
  WHERE height >= 173 """ #WHERE句を使う
for row in cur.execute(sql):
  print(row)
print() #改行

print("weightが 75.8 以外の行")
sql = """SELECT *
  FROM personal
  WHERE weight != 75.8 """ #WHERE句を使う
for row in cur.execute(sql):
  print(row)
print() #改行

print("idが '001' と等しい以外の行")
sql = """SELECT *
  FROM personal
  WHERE NOT id = '001' """ #WHERE句を使う
for row in cur.execute(sql):
  print(row)
print() #改行

print("""heightが 173 以上で、かつ、
weightが 75.8 と等しい行""")
sql = """SELECT *
  FROM personal
  WHERE height >= 173 AND weight = 75.8""" #WHERE句を使う
for row in cur.execute(sql):
  print(row)
print() #改行

print("""heightが 163 と等しいか、もしくは
173 と等しい行""")
sql = """SELECT *
  FROM personal
  WHERE height = 163 OR height = 173""" #WHERE句を使う
for row in cur.execute(sql):
  print(row)
print() #改行

print("""heightが 170 から 180
の範囲に含まれている行""")
sql = """SELECT *
  FROM personal
  WHERE height BETWEEN 170 AND 180""" #WHERE句を使う
for row in cur.execute(sql):
  print(row)
print() #改行

print("""heightが 160、170、180 の
どれかと等しい行""")
sql = """SELECT *
  FROM personal
  WHERE height IN(160, 170, 180)""" #WHERE句を使う
for row in cur.execute(sql):
  print(row)
print() #改行

print("""heightが 160、170、180 の
どれとも等しくない行""")
sql = """SELECT *
  FROM personal
  WHERE height NOT IN(160, 170, 180)""" #WHERE句を使う
for row in cur.execute(sql):
  print(row)
print() #改行