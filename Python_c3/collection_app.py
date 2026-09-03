#蔵書管理アプリのプログラム
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import sqlite3

#書籍の情報をデータベースから取得する関数
def get_books():
  conn = sqlite3.connect('collection.db')
  cur = conn.cursor()
  sql = 'SELECT * FROM books' #SQLのSELECT文
  cur.execute(sql)
  books_list = cur.fetchall()
  conn.close()
  return books_list

#蔵書一覧の行が選択されたときに実行する関数
#（詳細情報の更新を行う）
def view_select(event):
  global img
  global d_frame
  slct_items = list_view.selection()
  s = ('ISBN/ASIN', 'タイトル', '著者',
       '出版社', '発売日', '価格（円）')
  for i in range(len(s)):
    item_view.item(i,
      values=(s[i],
        books_list[int(slct_items[0])][i+1]))
  img = tk.PhotoImage(
    file=books_list[int(slct_items[0])][7])
  panel.create_image(0, 0, anchor='nw', image=img)

#「登録」ボタンのハンドラ関数
in_entry = []
def new_registration():
  global sub_win
  global in_entry
  conn = sqlite3.connect('collection.db')
  cur = conn.cursor()
  #SQLのINSERT INTO文
  sql = """INSERT INTO
           books (isbn,
                  title,
                  author,
                  publisher,
                  release,
                  price,
                  image)
           VALUES(?, ?, ?, ?, ?, ?, ?)"""
  ele = []
  for i in range(len(in_entry)):
    ele.append(in_entry[i].get())
  cur.execute(sql, ele)
  conn.commit()
  conn.close()
  messagebox.showinfo('蔵書管理アプリ',
                      '新規登録しました。')
  sub_win.destroy()
  disp()

#「操作」→「新規登録」のハンドラ関数
sub_win = None
s = ('ISBN/ASIN', 'タイトル', '著者', '出版社',
     '発売日', '価格（円）', '画像ファイル')
def save():
  global sub_win
  global in_entry
  #書籍情報入力用ウィンドウの生成
  #Tk関数ではなく、Toplevel関数でウィンドウを生成すると、
  #メインウィンドウ(root)に連動するサブウィンドウになる
  sub_win = tk.Toplevel()
  sub_win.geometry('250x250')
  in_label = []
  in_entry.clear()
  for i in range(len(s)):
    in_label.append(tk.Label(
      sub_win,
      text=s[i]))
    in_entry.append(tk.Entry(
      sub_win,
      width=20))
  register = tk.Button(
    sub_win,
    text='登録',
    command=new_registration)
  for i in range(3):
    sub_win.columnconfigure(i, weight=1)
  for i in range(9):
    sub_win.rowconfigure(i, weight=1)
  for i in range(7):
    in_label[i].grid(column=0, row=i)
    in_entry[i].grid(column=1, row=i,
                     columnspan=2)
  register.grid(column=1, row=8, rowspan=2,
                sticky='n')

#「操作」→「削除」のハンドラ関数
def delete():
  conn = sqlite3.connect('collection.db')
  cur = conn.cursor()
  #SQLのDELETE文
  sql = 'DELETE FROM books WHERE id = ?'
  slct_items = list_view.selection()
  cur.execute(sql, (books_list[int(slct_items[0])][0],))
  conn.commit()
  conn.close()
  messagebox.showinfo('蔵書管理アプリ',
                      'データを削除しました。')
  disp()

#トップレベルウィンドウの生成
root = tk.Tk()
root.geometry('400x300')
root.title('蔵書管理アプリ')
root.resizable(0, 0)
root.grid_rowconfigure(0, weight=1)
root.grid_rowconfigure(1, weight=1)
root.grid_columnconfigure(0, weight=1)

#メニューバーを生成
men = tk.Menu(root)
root.config(menu=men)

#「操作」メニューを生成
menu_command = tk.Menu(
  root,
  tearoff=False)
men.add_cascade(label='操作', menu=menu_command)

#「操作」メニューに「新規登録」と「削除」を追加
menu_command.add_command(label='新規登録',
                         command=save)
menu_command.add_separator()
menu_command.add_command(label='削除', command=delete)

#蔵書一覧用のフレーム
c_frame = tk.Frame(root)

#蔵書一覧用のTreeviewウィジェットの生成
list_view = ttk.Treeview(
  c_frame,
  show='headings',
  columns=('t', 'a', 'p'),
  selectmode='browse',
  height = 5)
list_view.bind('<<TreeviewSelect>>', view_select)

#列見出し
list_view.heading('t', text='タイトル', anchor='center')
list_view.heading('a', text='著者', anchor='center')
list_view.heading('p', text='出版社', anchor='center')

#列の設定
list_view.column('t', anchor='w', width=200)
list_view.column('a', anchor='w', width=80)
list_view.column('p', anchor='w', width=80)

#Scrollbarウィジェットの生成
yber = tk.Scrollbar(
  c_frame,
  orient=tk.VERTICAL,
  width=16,
  command=list_view.yview)
list_view.configure(yscrollcommand=yber.set)
yber.grid(row=0, column=1, sticky='nsew')

#蔵書一覧にデータを追加
books_list = []
def disp():
  #初期化
  list_view.delete(*list_view.get_children())
  global books_list
  books_list = get_books()
  for i in range(len(books_list)):
    list_view.insert(parent='', index='end', iid=i,
      values=(books_list[i][2],
              books_list[i][3],
              books_list[i][4]))
    list_view.grid(row=0, column=0, sticky='nsew')
    #最後の行を選択
    list_view.selection_set(i)
    #最後の行に移動（自動スクロール）
    list_view.see(i)

#蔵書一覧を作成
disp()

#詳細情報部分の生成
d_frame = tk.Frame(root)
d_frame.grid_columnconfigure(0, weight=1)
d_frame.grid_columnconfigure(1, weight=1)

#書籍の詳細情報用のTreeviewウィジェットを生成
item_view = ttk.Treeview(
  d_frame,
  show='tree',
  columns=('i', 'c'),
  selectmode='none',
  height=6)
#階層列はwidth=0にして見えなくする
item_view.column('#0', width=0, stretch=False)
item_view.column('i', anchor='w', width=80)
item_view.column('c', anchor='w', width=200)

#詳細情報の表示
slct_items = list_view.selection()
for i in range(len(s)):
  item_view.insert(parent='', index='end', iid=i,
    values=(s[i],
            books_list[int(slct_items[0])][i+1]))
item_view.grid(row=0, column=0)

#表紙画像の生成
img = tk.PhotoImage(
  file=books_list[int(slct_items[0])][7])
panel = tk.Canvas(
  d_frame,
  width=70,
  height=100)
panel.create_image(0, 0, anchor='nw', image=img)
panel.grid(row=0, column=1, pady=15, sticky='nsew')

#下記の部分を記述を忘れると、一覧表示されない
c_frame.grid(row=0, column=0)
d_frame.grid(row=1, column=0, sticky='nsew')

root.mainloop()

