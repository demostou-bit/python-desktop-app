import tkinter as tk
from tkinter import messagebox

#ハンドラ関数。
#entry_1.get()で入力されたテキストを取得
def clicked():
  messagebox.showinfo('Name App', entry_1.get())

#トップレベルウィンドウの生成
root = tk.Tk()
root.geometry('250x120')
root.title('Name App')

#Labelウィジェットの生成
label_1 = tk.Label(
  root,
  text = '名前を入力してください'
)

#entryウィジェットの生成
entry_1 = tk.Entry(
  root,
  width = 20
)

#Buttonウィジェットの生成
button_1 = tk.Button(
  root,
  text = '表示',
  command = clicked
)

#各列の割合を指定
root.columnconfigure(0, weight = 1)

#各行の割合を指定
root.rowconfigure(0, weight = 1)
root.rowconfigure(1, weight = 1)
root.rowconfigure(2, weight = 1)

#grid関数で配置
label_1.grid(column = 0, row = 0, sticky = 's')
entry_1.grid(column = 0, row = 1)
button_1.grid(column = 0, row = 2, sticky = 'n')

#トップレベルウィンドウの表示
root.mainloop()
