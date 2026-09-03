import tkinter as tk
import threading as th

count = 10
timer = None

# ハンドラ関数
def start():
    global count
    count = 10
    button_1['state'] = tk.DISABLED  # ボタンを無効
    countdown()

# カウントダウンの関数
def countdown():
    global count
    global timer
    
    # 0未満になったら終了処理をする
    if count < 0:
        if timer is not None:
            timer.cancel()
        button_1['state'] = tk.NORMAL  # ボタンを有効
        return  # 処理を終了して次のタイマーを作らない

    label_1['text'] = str(count)
    count = count - 1
    
    # 次の1秒後のタイマーを設定してスタート
    timer = th.Timer(1, countdown)
    timer.start()

# アクティブなスレッドのオブジェクトを表示（起動時）
for thread in th.enumerate():
    print(thread)
print('\n')

# トップレベルウィンドウの生成
root = tk.Tk()
root.title('スレッド')
root.geometry('250x100')

# Labelウィジェットの生成
label_1 = tk.Label(
    root,
    text='10'  
)
label_1.pack(expand=True)

# Buttonウィジェットの生成
button_1 = tk.Button(
    root,
    text='START',
    command=start
)
button_1.pack(expand=True)

root.mainloop()

# アプリを閉じたときにタイマーが動いていたら強制停止
if timer is not None: 
    timer.cancel()