#階層列を使わないTreeviewウィジェット
import tkinter as tk
from tkinter import ttk

#トップレベルウィンドウの生成
root = tk.Tk()
root.geometry('260x250')
root.title('Treeview Test')
root.resizable(0, 0)

#列の識別名
c_name = ('col_1', 'col_2', 'col_3')

#Treeviewウィジェットの生成
tview_1 = ttk.Treeview(
  root,
  show='headings', #階層列は非表示
  columns=c_name)

#列の設定
for c in c_name:
  tview_1.column(c, anchor='center', width=80)

#列見出し
tview_1.heading(c_name[0], text='カラム_1')
tview_1.heading(c_name[1], text='カラム_2')
tview_1.heading(c_name[2], text='カラム_3')

#最後（この時点での先頭）に追加
tview_1.insert(parent='', index='end',
               values=('ABC', 100, 'あいう'))

#先頭に追加
tview_1.insert(parent='', index='0',
               values=('DEF', 200, 'かきく'))

#最後に追加
tview_1.insert(parent='', index='end',
               values=('GHI', 300, 'さしす'))

tview_1.pack(expand=True)

root.mainloop()
