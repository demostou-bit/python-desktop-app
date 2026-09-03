import tkinter as tk

#ハンドラ関数
#1クリックされたウィジェットが
#1textキーを持つかどうかチェック
#2クリックされたウィジェットがtk.Tkクラスの
#2インスタンスであるかどうかをチェック
def clicked(event):
  if "text" in event.widget.keys(): #1
    event.widget['text'] = 'クリックしましたね'
  if isinstance(event.widght, tk.Tk): #2
    print('ウインドウをクリックしました')

root = tk.Tk()
root.title('イベントリブン')
root.geometry('250x120')

#すべてのウィジェットにハンドラ関数を設定
#3イベントの種類はButtonReleaseで、詳細は-1
root.bind_all('<ButtonRelease-1>', clicked)

label_1 = tk.Label(
  root,
  text='ココをクリック')
label_1.pack(expand=True)

button_1 = tk.Button(
  root,
  text='ココをクリック')
button_1.pack(expand=True)

root.mainloop()
