import tkinter as tk
from tkinter import ttk
import threading as th
from tkinter import messagebox

#グローバル変数
count = 0
timer = None

#ハンドラ関数
def start():
  global count
  global timer
  button_1['state'] = tk.DISABLED
  button_2['state'] = tk.NORMAL
  m = var_minutes.get() #ウィジェット変数の値を取得
  s = var_seconds.get() #ウィジェット変数の値を取得
  count = m * 60 + s
  progressbar_1['maximum'] = count #バーの最大値を設定
  #Timer関数の実行
  timer = th.Timer(1, countdown)
  timer.start() #スレッドを開始

def stop():
  timer.cancel()
  button_1['state'] = tk.NORMAL
  button_2['state'] = tk.DISABLED

def countdown():
  global count
  global timer
  count = count - 1
  if count > 0:
    progressbar_1['value'] = count
    m, s = divmod(count, 60)
    var_minutes.set(m) #ウィジェット変数に値を設定
    var_seconds.set(s) #ウィジェット変数に値を設定
    #Timer関数の実行
    timer = th.Timer(1, countdown)
    timer.start() #スレッドを開始
  else:
    progressbar_1['value'] = count
    var_minutes.set(0) #ウィジェット変数に値を設定
    var_seconds.set(0) #ウィジェット変数に値を設定
    messagebox.showinfo('Timer App', 'お時間です！')
    button_1['state'] = tk.NORMAL
    button_2['state'] = tk.DISABLED
    timer.cancel()

#トップレベルウィンドウの生成
root =tk.Tk()
root.title('Timer App')
root.geometry('250x100')

#Labelウィジェットの生成
label_1 = tk.Label(
  root,
  text='分'
)

label_2 = tk.Label(
  root,
  text='秒'
)

#分と秒のウィジェット変数
var_minutes = tk.IntVar(value=0)
var_seconds = tk.IntVar(value=0)

#Spinboxウィジェットの生成
spinbox_1 = tk.Spinbox(
  root,
  width=2,
  from_=0,
  to=59,
  increment=1,
  textvariable=var_minutes #分を管理する同じウィジェット変数を設定
)

spinbox_2 = tk.Spinbox(
  root,
  width=2,
  from_=0,
  to=59,
  increment=1,
  textvariable=var_seconds #秒を管理する同じウィジェット変数を設定
)

#Scaleウィジェットの生成
scale_1 = tk.Scale(
  root,
  variable=var_minutes, #分を管理する同じウィジェット変数を設定
  orient=tk.HORIZONTAL,
  from_=0,
  to=59,
  showvalue=0
)

scale_2 = tk.Scale(
  root,
  variable=var_seconds, #秒を管理する同じウィジェット変数を設定
  orient=tk.HORIZONTAL,
  from_=0,
  to=59,
  showvalue=0
)

#Progressbarウィジェットの生成
progressbar_1 = ttk.Progressbar(
  root,
  variable=0,
  maximum=0
)

#Buttonウィジェットの生成
button_1 = tk.Button(
  root,
  text='START',
  state=tk.NORMAL,
  command=start
)

button_2 = tk.Button(
  root,
  text='STOP',
  state=tk.DISABLED,
  command=stop
)

#各列の割合を指定
for i in range(4):
  root.columnconfigure(i, weight=1)

#各行の割合を指定
for i in range(3):
  root.rowconfigure(i, weight=1)

#ウィジェットをgrid関数で配置
spinbox_1.grid(column=0, row=0, sticky='e')
label_1.grid(column=1, row=0, sticky='w')
spinbox_2.grid(column=2, row=0, sticky='e')
label_2.grid(column=3, row=0, sticky='w')
scale_1.grid(column=0, row=1, columnspan=2, sticky='n')
scale_2.grid(column=2, row=1, columnspan=2, sticky='n')
progressbar_1.grid(column=2, row=2, sticky='n')
button_1.grid(column=2, row=2, sticky='n')
button_2.grid(column=3, row=2, sticky='n')

root.mainloop()

if timer != None: timer.cancel()
