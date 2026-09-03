import tkinter as tk
from tkinter import messagebox
import csv

#グローバル変数
quiz_count = 0 #クイズの番号
data = [] #クイズのデータ

#quiz.csvからデータを読み込む
with open('quiz.csv', encoding='utf-8', newline='') as csvfile:
  reader_quiz = csv.reader(csvfile)
  data = [row for row in reader_quiz]

#ハンドラ関数
def change_quiz():
  global quiz_count
  var.set(0) #選択肢の初期値は設定しない
  quiz_count = quiz_count + 1
  if quiz_count < len(data):
    #クイズのテキストを設定
    question['text'] = data[quiz_count][0]
    #選択肢のテキストを設定
    for i in range(len(radio)):
      radio[i]['text'] = data[quiz_count][i + 1]
  else:
    messagebox.showinfo('Quiz App', 'クイズはもうありません！')

def judgement(): #回答を判定する関数
  if data[quiz_count][5] == str(var.get()):
    messagebox.showinfo('Quiz App', '正解です。')
  elif var.get() == 0:
    messagebox.showinfo('Quiz App', '選択肢を選んでください！')
  else:
    messagebox.showinfo('Quiz App', '残念！不正解です！')

#トップレベルウィンドウの生成
root =tk.Tk()
root.geometry('300x250')
root.title('Quiz App')

#Labelウィジェットの生成
question = tk.Label(
  root,
  #最初のクイズのテキストを設定
  text=data[quiz_count][0]
)
question.grid(row=0, column=0, columnspan=2)

#ウィジェット変数の生成
var = tk.IntVar()

#Radiobuttonウィジェットの生成
radio = []
for i in range(4):
  radio.append(tk.Radiobutton(
    root,
    #最初のクイズの選択肢を設定
    text=data[quiz_count][i + 1],
    variable=var, #ウィジェット変数の設定
    value=i+1 #値を設定
  ))
  radio[i].grid(row=i+1, column=0, columnspan=2)

#Buttonウィジェットの生成
answer = tk.Button(
  root,
  text='回答',
  command=judgement
)
answer.grid(row=5, column=0, sticky='n')

next_quiz = tk.Button(
  root,
  text='次のクイズ',
  command=change_quiz
)
next_quiz.grid(row=5, column=1, sticky='n')

#2列、6行の割合を指定
for i in range(2):
  root.columnconfigure(i, weight=1)
for i in range(6):
  root.rowconfigure(i, weight=1)

#トップレベルウィンドウの表示
root.mainloop()
