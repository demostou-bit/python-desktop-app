import tkinter as tk

root = tk.Tk()
root.title('Label Test')
root.geometry('250x120')

#Labelウィジェットを生成
label_1 = tk.Label(
  root, #第一引数で親コンテナ(root)を指定
  text='ラベルのテスト') #textオプションでテキストを指定
label_1.pack(expand=True)

root.mainloop()
