import tkinter as tk

#ハンドラ関数
def click_delete1():
  #すべて削除
  text.delete('1.0', 'end') #delete関数

def click_delete2():
  #3行目を削除。第2引数がendだけだと3行目以降を削除する
  text.delete('3.0', '3.end') #delete関数

#トップレベルウィンドウの生成
root = tk.Tk()
root.geometry('250x200')
root.title('Text Test')

#Textウィジェットの生成
text = tk.Text(
  root,
  width=30,
  height=7)
text.pack(expand=True)

#Buttonウィジェットの生成
button_1 = tk.Button(
  root,
  text='削除1',
  command=click_delete1)
button_1.pack(expand=True)

button_2 = tk.Button(
  root,
  text='削除2',
  command=click_delete2)
button_2.pack(expand=True)

root.mainloop()
