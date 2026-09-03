import tkinter as tk

root = tk.Tk()
root.title('Label Test')
root.geometry('250x100')

WIDGET_MAX = 3

#色名のタブ
color_name = ('red', 'green', 'blue')

#RGB値のタブ
rgb_value = ('#ff0000', '#00ff00', '#0000ff')

labels_1 = [
  tk.Label(
    root,
    text=color_name[num],
    bg=color_name[num]) #背景色の色名を指定
  for num in range(WIDGET_MAX)]

labels_2 = [
  tk.Label(
    root,
    text=rgb_value[num],
    fg=rgb_value[num]) #文字色のRGB値を指定
  for num in range(WIDGET_MAX)]

root.rowconfigure(0, weight=1)
root.rowconfigure(1, weight=1)

for num in range(WIDGET_MAX):
  root.columnconfigure(num, weight=1)
  labels_1[num].grid(column=num, row=0)
for num in range(WIDGET_MAX):
  root.columnconfigure(num, weight=1)
  labels_2[num].grid(column=num, row=1)

root.mainloop()
