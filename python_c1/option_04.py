#config関数のcnfオプションを使うプログラム
import tkinter as tk

root = tk.Tk()
root.title('Option Test')
root.geometry('250x120')

#属性とその値を辞書にまとめる
option = {
  'text': 'ウィジェットの属性',
  'relief': 'sunken',
  'padx': 10,
  'pady': 10
}

label_1 = tk.Label(root)
label_1.pack(expand = True)

#config関数で属性に値を設定
label_1.config(cnf = option)

root.mainloop()
