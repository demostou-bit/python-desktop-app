#cnfオプションを使って属性を設定するプログラム
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

#ウィジェットを生成
label_1 = tk.Label(
  root,
  cnf = option #辞書をcnfオプションに渡す
)

label_1.pack(expand = True)

root.mainloop()
