#Comboboxウィジェットのテストプログラム
import tkinter as tk
import tkinter.ttk as ttk
from tkinter import messagebox

#ハンドラ関数
def click_get():
  #選択されている値を取得してメッセージボックスで表示
  messagebox.showinfo('Combobox',  combobox_1.get())

#トップレベルウィンドウの生成
root = tk.Tk()
root.geometry('300x100')
root.title('Combobox Test')

#候補の値をリストで用意しておき、Combobox関数のvaluesオプションに渡す
number = ['1', '2', '3', '4', '5']

#Comboboxウィジェットの生成
combobox_1 = ttk.Combobox(
  root,
  state='normal',
  values=number, #候補のリストを渡す
  width=5
)
#リストの先頭を選択した状態にする
combobox_1.current(0) #current関数
combobox_1.pack(expand=True)

#Buttonウィジェットの生成
button_1 = tk.Button(
  root,
  text='表示',
  command=click_get
)
button_1.pack(expand=True)

root.mainloop()
