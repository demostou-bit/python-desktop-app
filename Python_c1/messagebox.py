import tkinter as tk
from tkinter import messagebox

#このコードにおいては、上から順に表示させるだけの処理
#本来であれば、分岐処理に使用する

#メッセージボックス「情報」
r = messagebox.showinfo('showinfo', '情報')
print(r) #戻り値'ok'

#メッセージボックス「警告」
r = messagebox.showwarning('showwarning', '警告')
print(r) #戻り値'ok'

#メッセージボックス「エラー」
r = messagebox.showerror('showerror', 'エラー')
print(r) #戻り値'ok'

#メッセージボックス「はい、いいえ」
r = messagebox.askyesno('askyesno', 'はい、いいえ')
print(r) #戻り値True、False

#メッセージボックス「はい、いいえ」
r = messagebox.askquestion('askquestion', 'はい、いいえ')
print(r) #戻り値'yes'、'no'

#メッセージボックス「OK、キャンセル」
r = messagebox.askokcancel('askokcancel', 'OK、キャンセル')
print(r) #戻り値True、False

#メッセージボックス「再試行、キャンセル」
r = messagebox.askretrycancel('askretrycancel', '再試行、キャンセル')
print(r) #戻り値True、False

#メッセージボックス「はい、いいえ、キャンセル」
r = messagebox.askyesnocancel('askyesnocancel', 'はい、いいえ、キャンセル')
print(r) #戻り値True、False、None
