#idやtag属性の名前を使って、特定の図形だけを消去するプログラム
import tkinter as tk

#グローバル変数
id = None

#ハンドラ関数
def oval_drow():
  global id
  if id == None:
    #円を描いて円のオブジェクトidを取得
    id = canvas_1.create_oval(40, 40,
                              160, 160,
                              width=4)
def oval_delete():
  global id
  canvas_1.delete(id) #idで指定した図形のオブジェクトを削除
  id = None

def rectangle_drow():
  #tagオプションで図形の名前を設定
  canvas_1.create_rectangle(50, 50,
                            150, 150,
                            width=4,
                            tag='rectangle')

def rectangle_delete():
  #tag属性の名前で指定した図形のオブジェクトを削除
  canvas_1.delete('rectangle')

def all_delete():
  global id
  canvas_1.delete('all') #Canvasウィジェット全体を消去
  id = None

root =tk.Tk()
root.title('Canvas Test')
root.geometry('300x250')

#ウィジェットの生成
canvas_1 = tk.Canvas(
  root,
  width=200,
  height=200,
  background='white'
)

#5つのボタンを生成
button_1 = tk.Button(
  root,
  text='oval',
  command=oval_drow
)
button_2 = tk.Button(
  root,
  text='o_delete',
  command=oval_delete
)
button_3 = tk.Button(
  root,
  text='rectangle',
  command=rectangle_drow
)
button_4 = tk.Button(
  root,
  text='r-delete',
  command=rectangle_delete
)
button_5 = tk.Button(
  root,
  text='all_delete',
  command=all_delete
)

for i in range(5):
  root.columnconfigure(i, weight=1)

root.rowconfigure(1, weight=1)

canvas_1.grid(column=0, row=0, columnspan=5)
button_1.grid(column=0, row=1)
button_2.grid(column=1, row=1)
button_3.grid(column=2, row=1)
button_4.grid(column=3, row=1)
button_5.grid(column=4, row=1)

root.mainloop()
