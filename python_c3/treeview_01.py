import tkinter as tk
from tkinter import ttk #ttkをインポートする

#insert関数の実行
def insert_test(str):
  id = tview_1.insert(parent='',
                      index='end', text=str)
  tview_1.insert(parent=id, index='end',
                 values=('ABC', 100, 'あいう'))
  tview_1.insert(parent=id, index='end',
                 values=('DEF', 200, 'かきく'))
  tview_1.insert(parent=id, index='end',
                 values=('GHI', 300, 'さしす'))

#トップレベルウィンドウの生成
root = tk.Tk()
root.geometry('350x260')
root.title('Treeview Test')
root.resizable(0, 0)

#別の識別名
c_name = ('col_1', 'col_2', 'col_3') #1

#Treeviewウィジェットの生成
tview_1 = ttk.Treeview( #Terrview関数
  root,
  columns=c_name)

#列の設定
#column関数
tview_1.column('#0', anchor='w', width=80) #階層列
#2
for c in c_name:
  tview_1.column(c, anchor='center', width=80)

#列見出し
#3
tview_1.heading('#0',
                text='ツリーカラム') #階層列
tview_1.heading(c_name[0], text='カラム_1')
tview_1.heading(c_name[1], text='カラム_2')
tview_1.heading(c_name[2], text='カラム_3')

insert_test('1行目')
insert_test('2行目')
insert_test('3行目')

tview_1.pack(expand=True)

root.mainloop()
