#お絵描きアプリのプログラム
import tkinter as tk
from tkinter import colorchooser

#グローバル変数
sx, sy = 0, 0
color = 'black'

#ハンドラ関数
#2 event.xとevent.yには、左ボタンを押したときのマウスの座標が格納
#2 create_oval関数を使って、点を描画している
#2 第1引数と第3引数に同じsxを、第2引数と第4引数に同じsyを指定している
def on_pressed(event):
  global sx, sy
  sx, sy = event.x, event.y
  canvas_1.create_oval(sx, sy, sx, sy,
                       outline=color,
                       width=scale_1.get())
#3 create_line関数を使って、線を描画している
#3 グローバル変数のsxとsyには、左ボタンが押された時のマウスの座標が格納
#3 event.xとevent.yには、ドラッグされた後のマウスの座標が格納
#3 その後、event.xとevent.yの値をsxとsyに格納
#3 ドラッグ中は<Button1-Motion>イベントが何度も発生するので、
#3 on_dragged関数の実行では、座標(sx, sy)から、値が更新されている座標
#3 (event.x, event.y)に線を描きます。
def on_dragged(event):
  global sx, sy
  canvas_1.create_line(sx, sy, event.x, event.y,
                       fill=color,
                       width=scale_1.get())
  sx, sy = event.x, event.y
#4 change_color関数は、線の色を変更する処理を担当。線の色はグローバル
#4 変数のcolorに保持させています。カラー選択ダイアログで、ユーザーが
#4 キャンセルボタンか右上の×ボタンでダイアログを閉じると、(None, None)
#4 が返ります。Noneは色の情報ではないため、colorやCanvasウィジェットの
#4 background属性に設定できません。そこで、askcolor関数の戻り値をチェックし、
#4 (None, None)が返ってきた場合は、関数を終了するようにしています。
def change_color():
  global color
  c = colorchooser.askcolor()
  if c[1] == None: return
  color = c[1]
  canvas_2['background'] = c[1]
  change_pen(scale_1.get())
#5 ハンドラ関数としてchange_pen関数をcommandオプションで指定
#5 このハンドラ関数は、引数(value)を持ちます。
#5 Scaleウィジェットのつまみを動かすとハンドラ関数が実行されますが、
#5 その際、引数にはつまみの値が文字列で格納されます。change_pen関数では
#5 引数valueからつまみの値を取得し、float型に変換して、線の太さの設定に
#5 利用しています。
def change_pen(value):
  canvas_3.delete('all')
  canvas_3.create_rectangle(0, 0, 20, 20,
                            fill='white')
  size = float(value) / 2
  canvas_3.create_oval(10-size, 10-size,
                       10+size, 10+size,
                       outline=color,
                       fill=color,
                       width=1)
#6 all deleteボタンを生成

#トップレベルウィンドウの生成
root = tk.Tk()
root.title('Drawing App')
root.geometry('300x330')

#Canvasウィジェットの生成
canvas_1 = tk.Canvas(
  root,
  background='white'
)
#1 マウスの左ボタンに関する2つのイベントと、そのハンドラ関数を次のように設定
# Button1-Motionイベントは、マウスのドラッグで発生するイベント
canvas_1.bind('<ButtonPress-1>', on_pressed)
canvas_1.bind('<Button1-Motion>', on_dragged)

canvas_2 = tk.Canvas(
  root,
  width=40,
  height=20,
  background='black'
)

canvas_3 = tk.Canvas(
  root,
  width=20,
  height=20
)

#Buttonウィジェットの生成
button_1 = tk.Button(
  root,
  text='Color Select',
  command=change_color #commandオプションにchange_color関数を設定
)
#Scaleウィジェットの生成
scale_1 = tk.Scale(
  root,
  orient=tk.HORIZONTAL,
  from_=1,
  to=10,
  command=change_pen #commandオプションにchange_pen関数を設定
)

change_pen(5.0) #ペンを初期値に設定

#4列の割合を指定
for i in range(4):
  root.columnconfigure(i, weight=1)

#2行目の割合を指定
#(1行目のCanvasはグリッド側に合わせる)
root.rowconfigure(1, weight=1)

canvas_1.grid(column=0, row=0, columnspan=4)
button_1.grid(column=0, row=1)
canvas_2.grid(column=1, row=1)
scale_1.grid(column=2, row=1)
canvas_3.grid(column=3, row=1)

root.mainloop()
