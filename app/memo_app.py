import tkinter as tk
import datetime
import calendar
from tkinter import messagebox
import sqlite3

#日付を引数にしてメモを取得する関数
def get_memo(day):
  conn = sqlite3.connect('memo.db')
  cur = conn.cursor()
  today_memo = ''
  #dailyテーブルからメモのデータを抽出するSQL文
  sql = 'SELECT * FROM daily WHERE date = ?'
  for row in cur.execute(sql, (day,)):
    today_memo = row[1]
  conn.close()
  return today_memo

#日付のクリック時に実行する関数
def click(event):
  global click_day
  click_day = event.widget['text']
  n = str(yer[0]) + '_' + str(mon[0]) + \
      '_' + str(click_day)
  title['text'] = make_text_1(yer[0], mon[0], \
                  click_day) + 'のメモ'
  text.delete('1.0', 'end')
  text.insert('1.0', get_memo(n))

#保存ボタンのクリック時に実行する関数
def save(t_day):
  conn = sqlite3.connect('memo.db')
  cur = conn.cursor()
  #データの追加または更新を行うSQL文
  #REPLACE INTOであるはずが、REPLACE INFOになっていたため、保存できなかった
  sql = 'REPLACE INTO daily VALUES(?, ?)'
  cur.execute(sql, (t_day, \
              text.get('1.0', 'end-1c')))
  conn.commit()
  conn.close()
  messagebox.showinfo('メッセージ', \
                      'データを保存しました。')
  disp(0)

#引数の日付にメモがあればTrue、なければFalseを返す関数
def check(y, m, d):
  day = str(y) + '_' + str(m) + '_' + str(d)
  if get_memo(day) != '':
    return True
  return False

#日付文字列を作る関数
def make_text_1(y, m, d):
  return str(y) + '年' + str(m) + \
         '月' + str(d) + '日'

def make_text_2(y, m, d):
  return str(y) + '_' + str(m) + '_' + str(d)

#表示するカレンダーの生成
WEEK = ['日', '月', '火', '水', '木', '金', '土']
WEEK_COLOR = ['red', 'black', 'black', 'black',
              'black', 'black', 'blue']

def disp(arg):
  global yer
  global mon
  mon[0] += arg

  if mon[0] < 1:
    mon[0], yer[0] = 12, yer[0] - 1
  elif mon[0] > 12:
    mon[0], yer[0] = 1, yer[0] + 1
  label['text'] = str(yer[0]) + '年' \
                  + str(mon[0]) + '月'
  
  cal = calendar.Calendar(firstweekday=6)
  cal = cal.monthdayscalendar(yer[0], mon[0])

  for widght in frame.winfo_children():
    widght.destroy()
  
  r = 0
  for i,x in enumerate(WEEK):
    label_day = tk.Label(
      frame,
      text=x,
      font=('', 10),
      width=3,
      fg=WEEK_COLOR[i])
    label_day.grid(row=r, column=i, pady=1)
  r = 1
  for week in cal:
    for i,day in enumerate(week):
      day = ' ' if day == 0 else day
      label_day = tk.Label(
        frame,
        text=day,
        font=('', 10),
        fg=WEEK_COLOR[i],
        borderwidth=1)
      if (yer[0], mon[0], today) == \
         (yer[1], mon[1], day):
        label_day['background'] = 'yellow'
      label_day.bind('<ButtonRelease-1>', click)
      label_day.grid(row=r, column=i, \
                     padx=2, pady=1)
    r = r + 1

#トップレベルウィンドウの生成(リサイズ不可)
root = tk.Tk()
root.title('メモアプリ')
root.geometry('480x280')
root.resizable(0, 0)

#カレンダー用のフレーム
c_frame = tk.Frame(root)
frame = tk.Frame(c_frame)

for n in range(3):
  c_frame.grid_columnconfigure(n, weight=1)

yer = [datetime.date.today().year] * 2
mon = [datetime.date.today().month] * 2
today = datetime.date.today().day
click_day = today

label = tk.Label(c_frame, font=('', 10))
label.grid(row=0, column=1)

button_1 = tk.Button(
  c_frame,
  text='<',
  font=('', 10),
  command=lambda:disp(-1))
button_1.grid(row=0, column=0, pady=10)

button_2 = tk.Button(
  c_frame,
  text='>',
  font=('', 10),
  command=lambda:disp(1))
#gridの引数column=0にしていたため、レイアウト崩れがあった
button_2.grid(row=0, column=2)
frame.grid(row=1, column=0, columnspan=3)

disp(0)

#ここからメモ用のフレーム
d_frame = tk.Frame(root)

#タイトルと保存ボタン
t_frame = tk.Frame(d_frame)
title = tk.Label(
  t_frame,
  text=make_text_1(yer[0], mon[0], today) + \
                   'のメモ',
  font=('', 12))
title.grid(row=0, column=0, padx=20)

button = tk.Button(
  t_frame,
  text='保存',
  command=lambda:save(make_text_2(yer[0], \
                      mon[0], click_day)))
button.grid(row=0, column=1)
t_frame.grid(row=0, column=0, pady=10)

#メモ用のTextウィジェット
text = tk.Text(
  d_frame,
  width=30,
  height=14)
text.grid(row=4, column=0)

scroll_v = tk.Scrollbar(d_frame,
                        orient=tk.VERTICAL,
                        command=text.yview)
scroll_v.grid(row=4, column=1,
              sticky=tk.N+tk.S)
text["yscrollcommand"] = scroll_v.set
text.insert('1.0', \
            get_memo(make_text_2(yer[0], \
                                 mon[0],today)))

c_frame.grid(row=0, column=0, padx=10)
d_frame.grid(row=0, column=1)

root.mainloop()
