import tkinter as tk

#ハンドラ関数
def click_insert1():
  #insert関数。第1引数でテキストの最後に、第2引数に指定した文字列を挿入
  text.insert('end', 'ABCDEFG\n')

def click_insert2():
  #insert関数。第1引数で2行目の0文字目の後に、第2引数に指定した文字列を挿入
  text.insert('2.0', 'あいうえお')

def click_insert3():
  #insert関数。第1引数で3行目の2文字目の後に、第2引数に指定した文字列を挿入
  text.insert('3.2', '■ ■ ■')

#トップレベルウィンドウの生成
root = tk.Tk()
root.geometry('250x220')
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
  text='挿入1',
  command=click_insert1)
button_1.pack(expand=True)

button_2 = tk.Button(
  root,
  text='挿入2',
  command=click_insert2)
button_2.pack(expand=True)

button_3 = tk.Button(
  root,
  text='挿入3',
  command=click_insert3)
button_3.pack(expand=True)

root.mainloop()
