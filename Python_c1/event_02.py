#ハンドラ関数を2つ用意
import tkinter as tk
from tkinter import messagebox

#ボタン1のハンドラ関数
def button_1_clicked():
  messagebox.showinfo('メッセージ', 'こんにちは！')

#ボタン2のハンドラ関数
def button_2_clicked():
  messagebox.showinfo('メッセージ', 'Kiai Ga Tarinai')

root = tk.Tk()
root.title('イベントリブン')
root.geometry('250x120')

#Buttonウィジェットの生成と配置
button_1 = tk.Button(
  root,
  text='ボタン1',
  command=button_1_clicked)
button_1.pack(expand=True)

button_2 = tk.Button(
  root,
  text='ボタン2',
  command=button_2_clicked)
button_2.pack(expand=True)

root.mainloop()