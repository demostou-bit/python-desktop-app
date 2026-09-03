import tkinter as tk

root = tk.Tk()
root.title('place関数')
root.geometry('250x120')

label_1 = tk.Label(
  root,
  text='x=100, y=50',
  relief=tk.SOLID)

#Labelウィジェットを親コンテナの
#座標(100, 50)に配置
label_1.place(x=100, y=50)

root.mainloop()