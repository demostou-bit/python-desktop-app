#config関数を使うプログラム
import tkinter as tk

root = tk.Tk()
root.title('Option Test')
root.geometry('250x120')

#ウィジェットを生成
label_1 = tk.Label(root)

#ウィジェットを配置
label_1.pack(expand = True)

#config関数で属性に値を設定
label_1.config(text = 'ウィジェットの属性',
               relief = 'sunken',
               padx = 10,
               pady = 10
)

root.mainloop()
