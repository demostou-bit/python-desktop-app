#Menuウィジェットを使うプログラム
import tkinter as tk
from tkinter import messagebox

#トップレベルウィンドウの生成
root = tk.Tk()
root.geometry('320x220')
root.title('Menu Test')

#Menuウィジェットを生成
men = tk.Menu(
  root,
  tearoff=False)

#menをウィンドウのメニューバーに設定
root.config(menu=men)

#menuウィジェットを生成
menu_command = tk.Menu(
  root,
  tearoff=False)

#menu_commandをメニューバーに
#操作メニューとして追加
men.add_cascade(label='操作', menu=menu_command)

#操作メニューに保存メニューを追加
menu_command.add_command(
  label='保存',
  command=lambda:messagebox.showinfo('Menu Test', '保存'))

#区切り線を追加
menu_command.add_separator()

#操作メニューに削除メニューを追加
menu_command.add_command(
  label='削除',
  command=lambda:messagebox.showinfo('Menu Test', '削除'))

#区切り線を追加
menu_command.add_separator()

#操作メニューに検索メニューを追加
menu_command.add_command(
  label='検索',
  command=lambda:messagebox.showinfo('Menu Test', '検索'))

root.mainloop()

