import tkinter as tk

root = tk.Tk()
root.title('Label Test')
root.geometry('400x250')

WIDGET_MAX = 3

#サイズと文字位置を指定して
#Labelウィジェットを生成
labels = [
  tk.Label(
    root,
    text='width=25, height=2',
    relief='solid',
    width=25,
    height=2),

  tk.Label(
    root,
    text='anchor=\'n',
    relief='solid',
    anchor='n',
    width=25,
    height=4),
  
  tk.Label(
    root,
    text='padx=100, pady=20',
    relief='solid',
    padx=100,
    pady=20)]

root.columnconfigure(0, weight=1)

for num in range(WIDGET_MAX):
  root.columnconfigure(num, weight=1)
  labels[num].grid(column=0, row=num)

root.mainloop()