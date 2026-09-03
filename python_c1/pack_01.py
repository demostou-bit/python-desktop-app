#tkinterを利用するためにインポートする
import tkinter as tk

#Tkオブジェクトの生成
root = tk.Tk()

#ウインドウのタイトルを指定
root.title('pack関数')

#ウインドウの内部のサイズを設定
root.geometry('250x120')

#Labelウィジェットの生成
label_1 = tk.Label(
  root, #親コンテナを指定
  text = '画面の中央' )

#Labelウィジェットをウインドウの中央に配置
label_1.pack(expand=True)

#トップレベルウインドウが表示され、イベントの発生を監視する
root.mainloop()