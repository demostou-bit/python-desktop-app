import tkinter as tk
from tkinter import font

root = tk.Tk()
root.title('Font Test')
root.geometry('250x250')

WIDGET_MAX = 3

#fontクラスのオブジェクトを生成
fonts = [
  font.Font(
    size = 18
  ),
  font.Font(
    family = 'System'
  ),
  font.Font(
    family = 'ＭＳ Ｐ明朝',
    weight = 'bold',
    size = 20,
    slant = 'italic',
    underline = True,
    overstrike = True
  )
]

labels = [
  tk.Label(
    root,
    text = 'フォントテスト\nABCD',
    font = fonts[num]
  )
  for num in range(WIDGET_MAX)
]

root.columnconfigure(0, weight = 1)

for num in range(WIDGET_MAX):
  root.rowconfigure(num, weight = 1)
  labels[num].grid(column = 0, row = num)

root.mainloop()
