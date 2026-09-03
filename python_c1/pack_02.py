import tkinter as tk

root = tk.Tk()
root.title('pack関数')
root.geometry('250x120')

#Labelウィジェットに枠をつけ、幅を8文字分にする
label_top = tk.Label(
  root,
  text = 'TOP',
  relief = tk.SOLID,
  width = 8 )

label_bottom = tk.Label(
  root,
  text = 'BOTTOM',
  relief = tk.SOLID,
  width = 8 )

label_left = tk.Label(
  root,
  text = 'LEFT',
  relief = tk.SOLID,
  width = 8 )

label_right = tk.Label(
  root,
  text = 'RIGHT',
  relief = tk.SOLID,
  width = 8 )

#指定しない場合は、上から下へ
label_top.pack(side=tk.TOP)
label_bottom.pack(side=tk.BOTTOM)
label_left.pack(side=tk.LEFT)
label_right.pack(side=tk.RIGHT)

root.mainloop()