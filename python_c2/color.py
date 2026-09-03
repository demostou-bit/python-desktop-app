import tkinter as tk
from tkinter import colorchooser

#ハンドラ関数
def color_settings():
  #カラー選択ダイアログの表示
  c = colorchooser.askcolor()
  print(c)

root = tk.Tk()
root.title('Color Test')
root.geometry('250x60')

button_1 = tk.Button(
  root,
  text='色の設定',
  command=color_settings
)
button_1.pack(expand=True)

root.mainloop()