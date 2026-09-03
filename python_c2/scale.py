#Scaleウィジェットのテストプログラム
import tkinter as tk

root = tk.Tk()
root.title('Scale Test')
root.geometry('250x100')

#ウィジェット変数の生成
var_1 = tk.IntVar()

#Labelウィジェットの生成
label_1 = tk.Label(
  root,
  textvariable=var_1 #ウィジェット変数の設定
)
label_1.pack(expand=True)

#Scaleウィジェットの生成
scale_1 = tk.Scale(
  variable=var_1, #ウィジェット変数の設定
  resolution=5, #分解能を5に
  orient=tk.HORIZONTAL, #水平方向
  from_=0, #左端は0
  to=100 #右端は100
)
scale_1.pack(expand=True)

#初期値を50にする
var_1.set(50)

root.mainloop()
