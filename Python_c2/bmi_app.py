import tkinter as tk

#BMIの計算(べき乗)
def calc(weight, height):
  return weight / (height**2)

#判定はcheck関数で行う。if～elif～else文を使って以下のように定義
def check(bmi):
  if bmi < 18.5: return '低体重'
  elif bmi < 25.0: return '普通体重'
  elif bmi < 30.0: return '肥満度1'
  elif bmi < 35.0: return '肥満度2'
  elif bmi < 40.0: return '肥満度3'
  else: return '肥満度4'

#ハンドラ関数はjudgement関数を使用
#Entryウィジェットのweightとheightから入力された値を
#get関数で取得し、「float関数」でfloat型に変換したら、
#calc関数を使ってBMIの計算を行う。
def judgement():
  w = float(weight.get())
  h = float(height.get()) / 100
  label_5['text'] = check(calc(w, h))

#トップレベルウィンドウの生成
root = tk.Tk()
#resizable関数を使い、ウィンドウのサイズ変更を不可に
root.resizable(width=False, height=False)
root.title('BMI App')
root.geometry('250x150')

#Labelウィジェットを5個生成
label_1 = tk.Label(root, text='体重')
label_2 = tk.Label(root, text='kg')
label_3 = tk.Label(root, text='身長')
label_4 = tk.Label(root, text='cm')
label_5 = tk.Label(
  root,
  text='体重と身長を入力してください。'
)

#Entryウィジェットを2個生成
weight = tk.Entry(width=5)
height = tk.Entry(width=5)

#Buttonウィジェットを1個生成
button = tk.Button(
  root,
  text='BMI判定',
  command=judgement
)

#各列の割合を指定
root.columnconfigure(0, weight=1)
root.columnconfigure(1, weight=1)
root.columnconfigure(2, weight=1)

#各行の割合を指定
root.rowconfigure(0, weight=1)
root.rowconfigure(1, weight=1)
root.rowconfigure(2, weight=1)
root.rowconfigure(3, weight=1)

#grid関数でウィジェットを配置
label_1.grid(column=0, row=0, sticky=tk.E)
weight.grid(column=1, row=0)
label_2.grid(column=2, row=0, sticky=tk.W)
label_3.grid(column=0, row=1, sticky=tk.E)
height.grid(column=1,row=1)
label_4.grid(column=2, row=1, sticky=tk.W)
button.grid(column=0, row=2, columnspan=3)
label_5.grid(column=0, row=3, columnspan=3)

root.mainloop()
