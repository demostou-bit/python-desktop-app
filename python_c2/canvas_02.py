#図形や画像を描画するための関数のテストプログラム
#円、線、四角、円弧、多角形、画像の順に表示する
import tkinter as tk

#グローバル変数
change = 0

#ハンドラ関数
def click_next(event):
  global change

  #Canvasウィジェットを消去
  canvas_1.delete('all')

  if change == 0:
    #円を描く
    canvas_1.create_oval(50, 50,
                         150, 150,
                         width=4)
  elif change == 1:
    #線を描く
    canvas_1.create_line(50, 50,
                         150, 150,
                         width=4)
  elif change == 2:
    #四角形を描く
    canvas_1.create_rectangle(50, 50,
                              150, 150,
                              width=4)
  elif change == 3:
    #円弧を描く
    canvas_1.create_arc(50, 50,
                        150, 150,
                        start=45,
                        extent=135,
                        width=4)
  elif change == 4:
    #多角形を描く
    canvas_1.create_polygon(75, 50,
                            125, 50,
                            150, 75,
                            150, 125,
                            125, 150,
                            75, 150,
                            50, 125,
                            50, 75)
  elif change == 5:
    #画像を描く
    canvas_1.create_image(100, 100,
                          image=img)
  change = change + 1
  if change > 6:
    root.destroy() #プログラムの終了

#トップレベルウィンドウの生成
root = tk.Tk()
root.title('Canvas Test')
root.geometry('300x300')

#画像ファイルの読み込み
img = tk.PhotoImage(file='nsw.png')

#Canvasウィジェットの生成
canvas_1 = tk.Canvas(
  root,
  width=200,
  height=200,
  background='white'
)
canvas_1.bind('<ButtonPress-1>', click_next)
canvas_1.pack(expand=True)

root.mainloop()
