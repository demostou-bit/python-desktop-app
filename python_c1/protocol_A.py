import tkinter as tk

#ハンドラ関数
def close_button():
  print('プログラムを終了します')
  #destroy関数を実行してプログラムを終了する
  root.destroy()

root = tk.Tk()
root.title('閉じるボタン')
root.geometry('250x120')

#WM_DELETE_WINDOWイベントが発生したら、ハンドラ
#関数のclose_button関数を実行するように設定
root.protocol('WM_DELETE_WINDOW', close_button)

root.mainloop()
