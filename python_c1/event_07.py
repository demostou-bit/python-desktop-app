import tkinter as tk
from tkinter import messagebox

#ハンドラ関数その1
def clicked_1(event):
  print('clicked_1')

#ハンドラ関数その2
def clicked_2(event):
  print('clicked_2')

#ハンドラ関数その3
def clicked_3(event):
  print('clicked_3')

root = tk.Tk()
root.title('イベントリブン')
root.geometry('250x120')

label_1 = tk.Label(
  root,
  text='ココをクリック')

#bind関数のaddオプションに'+'を与えると、ハンドラ関数を
#追加で設定できるようになります。
label_1.bind('<ButtonPress-1>', clicked_1)
label_1.bind('<ButtonPress-1>', clicked_2, add='+')
label_1.bind('<ButtonPress-1>', clicked_3, add='+')
label_1.pack(expand=True)

root.mainloop()
