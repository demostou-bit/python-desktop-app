import tkinter as tk

#トップレベルウィンドウの生成
root = tk.Tk()
root.geometry('250x100')
root.title('画面の切り替え')

#画面1の作成
#Frameウィジェットの生成
frame_1 = tk.Frame(root)
frame_1.grid(row=0, column=0, sticky=tk.NSEW)
#Labelウィジェットの生成
label_1 = tk.Label(
  frame_1,
  text='画面1です。'
)
label_1.pack(pady=10)
#Buttonウィジェットの生成
button_1 = tk.Button(
  frame_1,
  text='次の画面',
  command=lambda:frame_2.tkraise() #tkraise関数を実行するラムダ式
)
button_1.pack(pady=10)

#画面2の作成
#Frameウィジェットの生成
frame_2 = tk.Frame(root)
frame_2.grid(row=0, column=0, sticky=tk.NSEW)
#Labelウィジェットの生成
label_2 = tk.Label(
  frame_2,
  text='画面2です。'
)
label_2.pack(pady=10)
#Buttonウィジェットの生成
button_2 = tk.Button(
  frame_2,
  text='戻る',
  command=lambda:frame_1.tkraise() #tkraise関数を実行するラムダ式
)
button_2.pack(pady=10)

root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)

#画面1を前面にする
frame_1.tkraise()

root.mainloop()
