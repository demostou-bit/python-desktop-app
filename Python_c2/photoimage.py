#PNGファイルを読み込んでCanvasウィジェットに表示する
#PhotoImageクラスはjpeg形式には対応していない
import tkinter as tk

root = tk.Tk()
root.title('PhotoImage')
root.geometry('250x220')

#同じディレクトリのCardsフォルダのcardBack_blue1.pngを読み込む
card_back_img = tk.PhotoImage(
  file='Cards\cardBack_blue1.png'
)
canvas_1 = tk.Canvas(
  root,
  width=240,
  height=200
)
canvas_1.pack()

canvas_1.create_image(120, 100,
  image=card_back_img, #読み込んだ画像を扱う変数を指定
  anchor='center')

root.mainloop()
