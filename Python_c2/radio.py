import tkinter as tk
from tkinter import messagebox

#ハンドラ関数
def click_1():
  messagebox.showinfo('Radio Test', var_1.get())

def click_2():
  messagebox.showinfo('Radio Test', var_2.get())

#トップレベルウィンドウの生成
root = tk.Tk()
root.geometry('250x300')
root.title('Radio Test')

action_1 = ['選択肢1', '選択肢2', '選択肢3', '選択肢4']
action_2 = ['選択肢1', '選択肢2']

#ウィジェット変数を生成
#初期値は'選択肢1'にする
var_1 = tk.StringVar(value='選択肢1')
var_2 = tk.StringVar(value='選択肢1')

#4個のRediobuttonウィンドウを生成
for action in action_1:
  radio = tk.Radiobutton(
    root,
    text=action, #テキストを設定
    variable=var_1, #ウィジェット変数を設定
    width=10,
    value=action #値を設定
  )
  radio.pack(pady=5)

#Buttonウィジェットの生成
button_1 = tk.Button(
  root,
  text='表示',
  command=click_1
)
button_1.pack(pady=5)

#2個のRadiobuttonウィジェットを生成
for action in action_2:
  radio = tk.Radiobutton(
    root,
    text=action, #テキストを設定
    variable=var_2, #ウィジェット変数を設定
    width=10,
    value=action #値を設定
  )
  radio.pack(pady=5)

#Buttonウィジェットの生成
button_2 = tk.Button(
  root,
  text='表示',
  command=click_2
)
button_2.pack(pady=5)

root.mainloop()
