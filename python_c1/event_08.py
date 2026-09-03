import tkinter as tk

#ハンドラ関数
def clicked(event):
  event.widget['text'] = 'クリックしましたね'

root = tk.Tk()
root.title('イベントリブン')
root.geometry('250x120')

#全てのLabelウィジェットにハンドラ関数を設定
root.bind_class('Label',
                '<ButtonRelease-1>',
                clicked)

label_1 = tk.Label(
  root,
  text='ココをクリック')
label_1.pack(expand=True)

label_2 = tk.Label(
  root,
  text='ココをクリック')
label_2.pack(expand=True)

root.mainloop()