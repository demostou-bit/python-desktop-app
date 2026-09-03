import tkinter as tk
from tkinter import messagebox

#ハンドラ関数。Event型の引数を持つ
def clicked(event):
  print(event.x, event.y) #ボタンが押された時のマウスの座標を表示

root = tk.Tk()
root.title('イベントリブン')
root.geometry('250x120')

root.bind('<ButtonPress>', clicked)

root.mainloop()
