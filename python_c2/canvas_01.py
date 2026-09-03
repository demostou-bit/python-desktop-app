#Canvasウィジェットを表示するテストプログラム
import tkinter as tk

root = tk.Tk()
root.title('Canvas Test')
root.geometry('300x300')

#Canvasウィンドウの生成
canvas = tk.Canvas(
  root,
  width=200,
  height=200,
  background='blue'
)
canvas.pack(expand=True)

root.mainloop()
