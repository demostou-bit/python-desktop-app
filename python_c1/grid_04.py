import tkinter as tk

root = tk.Tk()
root.title('grid関数')
root.geometry('400x200')

#ウィジェットの数
WIDGET_MAX = 8

#Labelウィジェットのリストを生成
labels = [
  tk.Label(
    root,
    text='NO_'+str(num),
    relief=tk.SOLID )
  for num in range(WIDGET_MAX) ]

#各行の割合を指定
root.rowconfigure(0, weight=1)
root.rowconfigure(1, weight=1)

#各列の割合を指定
root.columnconfigure(0, weight=1)
root.columnconfigure(1, weight=1)
root.columnconfigure(2, weight=1)
root.columnconfigure(3, weight=1)

#2行4列のグリッドにLabelウィジェットを配置
#stickyオプションを使う
labels[0].grid(column=0, row=0, sticky='n')
labels[1].grid(column=1, row=0, sticky='s')
labels[2].grid(column=2, row=0, sticky='e')
labels[3].grid(column=3, row=0, sticky='w')
labels[4].grid(column=0, row=1, sticky='ns')
labels[5].grid(column=1, row=1, sticky='se')
labels[6].grid(column=2, row=1, sticky='ew')
labels[7].grid(column=3, row=1, sticky='nsew')

root.mainloop()