import tkinter as tk
import datetime
import calendar
from tkinter import messagebox

#1「本日」の年月日を取得
yer = [datetime.date.today().year] * 2
mon = [datetime.date.today().month] * 2
today = [datetime.date.today().day]

WEEK = ['日', '月', '火', '水', '木', '金', '土']
WEEK_COLOR = ['red', 'black', 'black', 'black',
              'black', 'black', 'blue']

#カレンダーの日付がクリックされた時の処理
def click(event):
  t = event.widget['text']
  messagebox.showinfo('メッセージ', str(t) + '日です。')

#表示するカレンダーの生成
def disp(arg):
  global yer
  global mon
  #インデントをdefブロックに合わせる。そうでないとエラーになる
  mon[0] += arg

  #年をまたぐ処理と年月の表示
  if mon[0] < 1:
    mon[0], yer[0] = 12, yer[0] - 1
  elif mon[0] > 12:
    mon[0], yer[0] = 1, yer[0] + 1
  label['text'] = str(yer[0]) + '年' + \
                      str(mon[0]) + '月'

  #2カレンダーの情報の取得
  cal = calendar.Calendar(firstweekday=6)
  cal = cal.monthdayscalendar(yer[0], mon[0])

  #Frame上のウィジェットを削除
  for widget in frame.winfo_children():
    widget.destroy()

  #1行目に曜日を表示
  r = 0
  for i, x in enumerate(WEEK):
    label_day = tk.Label(
      frame,
      text=x,
      font=('', 10),
      width=3,
      fg=WEEK_COLOR[i])
    label_day.grid(row=r, column=i, pady=1)

  #2行目以降日付を表示
  #forの入れ子が複雑化している。インデント位置がずれると日付が表示されない
  r = 1
  #forブロック1
  for week in cal:
    #forブロック2
    for i, day in enumerate(week):
      day = ' ' if day == 0 else day
      label_day = tk.Label(
        frame,
        text=day,
        font=('', 10),
        fg=WEEK_COLOR[i],
        borderwidth=1)
      #ifブロック
      if (yer[0], mon[0], today) == \
         (yer[1], mon[1], day):
        #インデントはifブロックに合わせる
        label_day['relief'] = 'solid'
      #インデントはforブロック2に合わせる
      label_day.bind('<ButtonRelease-1>', click)
      label_day.grid(row=r, column=i,
                     padx=2, pady=1)
    r = r + 1

#ウィンドウの生成
root = tk.Tk()
root.title('Calender')
root.geometry('220x200')
root.resizable(0, 0)

#ウィンドウの幅に合わせて列を均等に3分割
for n in range(3):
  root.grid_columnconfigure(n, weight=1)

#年月ボタンの表示
label = tk.Label(root, font=('', 10))
label.grid(row=0, column=1)

button_1 = tk.Button(
  root,
  text='<',
  font=('', 10),
  command=lambda:disp(-1))
button_1.grid(row=0, column=0, pady=10)

button_2 = tk.Button(
  root,
  text='>',
  font=('', 10),
  command=lambda:disp(1))
button_2.grid(row=0, column=2)

#カレンダーの日付を表示
frame = tk.Frame(root)
frame.grid(row=1, column=0, columnspan=3)

disp(0)

root.mainloop()