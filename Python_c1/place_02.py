import tkinter as tk

root = tk.Tk()
root.title('place関数')
root.geometry('250x120')

label_1 = tk.Label(
  root,
  text='relx=0.5, rely=0.5',
  relief=tk.SOLID)

#LabelウィジェットのX座標を
#親コンテナの幅の0.5(50%)の位置に、
#LabelウィジェットのY座標を
#親コンテナの高さの0.5(50%)の位置にする
label_1.place(relx=0.5, rely=0.5)

root.mainloop()