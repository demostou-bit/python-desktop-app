#Progressbarウィジェットのテストプログラム
import tkinter as tk
from tkinter import ttk #ttkモジュールをインポート

count = 10

def countdown():
  global count
  #ウィジェット変数に値を設定
  val_1.set(count) #val_1(Progressbar)とcountを連動させる
  count = count - 1
  if count < 0:
    return
  else:
    #1000ミリ秒=1秒後にcountdown関数を実行
    root.after(1000, countdown)

#トップレベルウィンドウの生成
root =tk.Tk()
root.title('Progressbar Test')
root.geometry('300x100')

#ウィジェット変数の生成
val_1 = tk.IntVar(value=10)

#Progressbarウィジェットの生成
progressbar_1 = ttk.Progressbar(
  root,
  variable=val_1, #ウィジェット変数を設定
  maximum=10
)
progressbar_1.pack(expand=True)

countdown()

root.mainloop()
