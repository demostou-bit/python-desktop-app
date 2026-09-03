#ラムダ式(無名関数または匿名関数)を使って
#event_02.pyを実現
import tkinter as tk
from tkinter import messagebox

#ラムダ式を使って、commandオプションに渡すための記述
def clicked(s):
  messagebox.showinfo('メッセージ', s)

root = tk.Tk()
root.title('イベントリブン')
root.geometry('250x120')

#Buttonウィジェットの生成と配置
button_1 = tk.Button(
  root,
  text='ボタン1',
  command=lambda:clicked('こんにちは！')) #ラムダ式を利用
button_1.pack(expand=True)

button_2 = tk.Button(
  root,
  text='ボタン2',
  command=lambda:clicked('Kiai Ga Tarinai')) #ラムダ式を利用
button_2.pack(expand=True)

root.mainloop()