#割り勘計算機のプログラム
import tkinter as tk
import tkinter.ttk as ttk
from tkinter import messagebox
import math

#ハンドラ関数
def calculation_result(): #(2)
  t = int(total.get()) #金額（円）
  e = int(erai.get()) #偉い人（人数）
  h = int(hira.get()) #平社員（人数）
  s = int(shin.get()) #新人（人数）
  kanj = 2 #幹事（1人）

  #割り勘のルールに従って計算
  #ベースを計算
  base = math.floor(t / (e * 3 + h * 2 + s + kanj))
  #偉い人はベースの約3倍
  erai_pay = 0 if e == 0 else (math.ceil(base * 3 / 100) * 100)
  #平社員はベースの約2倍
  hira_pay = 0 if e == 0 else (math.ceil(base * 2 / 100) * 100)
  #新人はほぼベースの金額
  shin_pay = 0 if e == 0 else (math.ceil(base * 1 / 100) * 100)
  #幹事の金額の計算
  kanji_pay = base *kanj
  total2 = erai_pay * e + hira_pay * h + shin_pay * s + kanji_pay
  kanji_pay = kanji_pay - (total2 - t)

  #計算結果の表示
  c = [['偉い人は　：', str(erai_pay)], ['平社員は　：', str(hira_pay)],
       ['新人は　：', str(shin_pay)], ['幹事は　：', str(kanji_pay)]]
  for i in range(len(out_label)):
    out_label[i][0]['text'] = c[i][0]
    out_label[i][1]['text'] = c[i][1]
  
  #計算結果画面へ切り替え
  out_frame.tkraise()

#トップレベルウィンドウの生成
root = tk.Tk()
root.geometry('300x220')
root.title('Warikan App')

#入力画面の作成(1)
in_frame = tk.Frame(root)
in_frame.grid(row=0, column=0, sticky=tk.NSEW)

#Entryウィジェットの生成(2)
total = tk.Entry(
  in_frame,
  width=10
)
total.insert(0, 0)

#Labelウィジェットの生成
s = ('金　額（ 円 ）',
     '偉い人（ 人数 ）',
     '平社員（ 人数 ）',
     '新　人（ 人数 ）',
     '幹　事（ １人 ）')
in_label = []
for i in range(len(s)):
  in_label.append(tk.Label(
    in_frame,
    text=s[i]
  ))

#Comboboxウィジェットの生成
number = ('0', '1', '2', '3', '4',
          '5', '6', '7', '8', '9')
erai = ttk.Combobox(
  in_frame,
  values=number,
  width=8
)
erai.current(0)
hira = ttk.Combobox(
  in_frame,
  values=number,
  width=8
)
hira.current(0)
shin = ttk.Combobox(
  in_frame,
  values=number,
  width=8
)
shin.current(0)

#Buttonウィジェットの生成
button_1 = tk.Button(
  in_frame,
  text='計算',
  command=calculation_result
)

#列、行の割合を指定
for i in range(2):
  in_frame.columnconfigure(i, weight=1)
for i in range(6):
  in_frame.rowconfigure(i, weight=1)

in_label[0].grid(column=0, row=0)
total.grid(column=1, row=0)
in_label[1].grid(column=0, row=1)
erai.grid(column=1, row=1)
in_label[2].grid(column=0, row=2)
hira.grid(column=1, row=2)
in_label[3].grid(column=0, row=3)
shin.grid(column=1, row=3)
in_label[4].grid(column=0, row=4, rowspan=2)
button_1.grid(column=1, row=5, sticky=tk.N)

#計算結果画面の作成(4)
out_frame = tk.Frame(root)
out_frame.grid(row=0, column=0, sticky=tk.NSEW)

#計算結果画面の割合を指定
out_frame.columnconfigure(0, weight=1)
out_frame.columnconfigure(1, weight=1)
for i in range(5):
  out_frame.rowconfigure(i, weight=1)

#Labelウィジェットの生成
out_label = []
for i in range(4):
  out_label.append([tk.Label(out_frame, padx=20),
                    tk.Label(out_frame, padx=20)])

#Buttonウィジェットの生成
button_2 = tk.Button(
  out_frame,
  text='計算に戻る',
  command=lambda:in_frame.tkraise()
)

for i in range(len(out_label)):
  out_label[i][0].grid(column=0, row=i, sticky='e')
  out_label[i][1].grid(column=1, row=i, sticky='w')
button_2.grid(column=0, row=4, columnspan=2, sticky='n')

#トップレベルウィンドウの生成
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)

#入力画面を前面にする
in_frame.tkraise()

root.mainloop()
