import tkinter as tk

root = tk.Tk()
root.title('Widget Variavle Test')
root.geometry('300x250')

#ウィジェット変数の生成
string_1 = tk.StringVar()
int_1 = tk.IntVar()
double_1 = tk.DoubleVar()
boolean_1 = tk.BooleanVar()

#Labelウィジェットの生成と配置
label_1 = tk.Label(
  root,
  #ウィジェット変数をLabelウィジェットに設定
  textvariable = string_1
)

label_1.pack(expand = True)

#ウィジェット変数に値を設定
string_1.set('ウィジェット変数')

#Scaleウィジェットの生成と配置
scale_1 = tk.Scale(
  root,
  orient = tk.HORIZONTAL,
  length = 100,
  #ウィジェット変数をScaleウィジェットに設定
  variable = int_1,
  command = lambda value:print(value)
)

scale_1.pack(expand = True)

#ウィジェット変数に値を設定
int_1.set(scale_1['length'] / 2)

#Scaleウィジェットの生成と配置
scale_2 = tk.Scale(
  root,
  orient = tk.HORIZONTAL,
  length = 100,
  from_ = 0.0,
  to = 1.0,
  resolution = 0.05,
  #ウィジェット変数をScaleウィジェットに設定
  variable = double_1,
  command = lambda value:print(double_1.get())
)
scale_2.pack(expand = True)
#ウィジェット変数に値を設定
double_1.set(scale_2['to'] / 2)

#Checkbuttonウィジェットの生成と配置
checkbutton_1 = tk.Checkbutton(
  root,
  text = 'チェックボタン',
  #ウィジェット変数をScaleウィジェットに設定
  variable = boolean_1,
  command = lambda:print(boolean_1.get())
)

checkbutton_1.pack(expand = True)

#ウィジェット変数に値を設定
boolean_1.set(True)

root.mainloop()
