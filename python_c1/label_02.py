import tkinter as tk

root = tk.Tk()
root.title('Label Test')
root.geometry('400x50')

#ウィジェットの数
WIDGET_MAX = 6

#reliefオプションに設定できる値のタブ
border_name = ('flat', 'solid', 'groove',
               'raised', 'ridge', 'sunken')

labels = [
  tk.Label(
    root,
    text=border_name[num],
    relief=border_name[num])
  for num in range(WIDGET_MAX)]

#各行の割合を指定
root.rowconfigure(0, weight=1)

#各列の割合を指定し、Labelウィジェットを配置
for num in range(WIDGET_MAX):
  root.columnconfigure(num, weight=1)
  labels[num].grid(column=num, row=0)

root.mainloop()