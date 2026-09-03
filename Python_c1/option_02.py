#キーでウィジェットの属性にアクセスするプログラム
import tkinter as tk

root = tk.Tk()
root.title('Option Test')
root.geometry('250x120')

#ウィジェットを生成
label_1 = tk.Label(root)

#ウィジェットを配置
label_1.pack(expand = True)

#キーで属性を指定して値を指定する
label_1['text'] = 'ウィジェットの属性'
label_1['relief'] = 'sunken'
label_1['padx'] = 10
label_1['pady'] = 10

root.mainloop()
