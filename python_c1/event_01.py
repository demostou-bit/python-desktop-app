import tkinter as tk
from tkinter import messagebox

#イベントが発生したときに何らかの処理を行いたい
#場合は、そのイベントに対応する関数を用意しておく
#イベントが発生したら、対応する関数が自動的に実行
#そのような関数はハンドラ関数と呼ばれる
def clicked(): #ハンドラ関数を設定
  messagebox.showinfo('メッセージ', 'こんにちは！')

root = tk.Tk()
root.title('イベントリブン')
root.geometry('250x120')

#Buttonウィジェットの生成と配置
button_1 = tk.Button(
  root,
  text='ボタン1',
  command=clicked) #ハンドラ関数を設定
button_1.pack(expand=True)

#mainloop関数を実行すると、イベントの発生を監視する状態になる
#イベントをハンドラ関数を使ってGUIに関連する処理を行う仕組みが
#イベントリブン(イベント駆動型)
root.mainloop()
