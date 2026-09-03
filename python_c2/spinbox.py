#Spinboxウィジェットのテストプログラム
import tkinter as tk

#トップレベルウィンドウの生成
root = tk.Tk()
root.title('Spinbox Test')
root.geometry('250x100')

#ウィジェット変数の生成
var_spin_1 = tk.IntVar(value=0)

#Labelウィジェットの生成
label_1 = tk.Label(
  root,
  #ウィジェット変数の生成
  textvariable=var_spin_1 #2つのウィジェットを連動
)
label_1.pack(expand=True)

#Spinboxウィジェットの生成
spinbox_1 = tk.Spinbox(
  root,
  width=3,
  from_=0, #最小値
  to=100, #最大値
  increment=5, #増減幅
  #ウィジェット変数を設定
  textvariable=var_spin_1 #2つのウィジェットを連動
)
spinbox_1.pack(expand=True)

#初期値を設定
var_spin_1.set(50)

root.mainloop()
