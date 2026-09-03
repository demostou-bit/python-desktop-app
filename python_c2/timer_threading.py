import tkinter as tk
import threading as th #threadingモジュールをインポート

count = 10
timer = None

#ハンドラ関数
def start():
  global count
  count = 10
  button_1['state'] = tk.DISABLED #ボタンを無効
  countdown()

#カウントダウンの関数
def countdown():
  global count
  global timer
  label_1['text'] = str(count)
  count = count - 1
  timer = th.Timer(1, countdown) #Timer関数を実行
  timer.start() #スレッドの開始

  #アクティブなスレッドのオブジェクトを表示
  for thread in th.enumerate():
    print(thread)
  print('\n')

  if count < 0:
    timer.cancel() #スレッドの停止
    button_1['state'] = tk.NORMAL #ボタンを有効

#トップレベルウィンドウの生成
root = tk.Tk()
root.title('スレッド')
root.geometry('250x100')

#Labelウィジェットの生成
label_1 = tk.Label(
  root,
  text='10'  
)
label_1.pack(expand=True)

#Buttonウィジェットの生成
button_1 = tk.Button(
  root,
  text='START',
  command=start
)
button_1.pack(expand=True)

root.mainloop()

if timer != None: timer.cancel()
