import tkinter as tk
from tkinter import messagebox

#ハンドラ関数。Event型の引数を持つ
def clicked(event):
  messagebox.showinfo('メッセージ', 'こんにちは！')

root = tk.Tk()
root.title('イベントリブン')
root.geometry('250x120')

#Buttonウィジェットの生成と配置
button_1 = tk.Button(
  root,
  text='ボタン1')

#<ButtonRelease-1>イベントのハンドラ関数として
#clicked関数を設定
button_1.bind('<ButtonRelease-1>', clicked) #bind関数
button_1.pack(expand=True)

root.mainloop()
