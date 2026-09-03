import tkinter as tk

root = tk.Tk()
root.title('Label Test')
root.geometry('250x150')

WIDGET_MAX = 3

#justifyオプションを利用してテキストを寄せる
labels = [
  tk.Label(
    root,
    text = 'テキスト1行目\n2行目',
    relief = 'solid' #中央寄せ
  ),
  tk.Label(
    root,
    text = 'テキスト1行目\n2行目',
    relief = 'solid',
    justify = 'left' #左寄せ
  ),
  tk.Label(
    root,
    text = 'テキスト1行目\n2行目',
    relief = 'solid',
    justify = 'right' #右寄せ
  )
]

root.columnconfigure(0, weight=1)

for num in range(WIDGET_MAX):
  root.rowconfigure(num, weight=1)
  labels[num].grid(column=0, row=num)

root.mainloop()