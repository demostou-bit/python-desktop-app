import tkinter as tk

root = tk.Tk()
root.geometry('250x100')
root.title('Entry Test')

#Entryウィジェットの生成と配置
#widthの後ろに「, show='文字列'」を入れると
#入力したものが指定した文字列が置き換わる
entry_1 = tk.Entry(root, width = 20)
entry_1.pack(expand = True)

root.mainloop()