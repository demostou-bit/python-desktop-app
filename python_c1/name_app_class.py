#クラス化する流儀で作るプログラム
import tkinter as tk
from tkinter import messagebox

#Applicationクラスの定義
#Tkクラスを親クラスとする
class Application(tk.Tk):

  #Applicationクラスのコンストラクタ
  def __init__(self):
    #親クラスのコンストラクタを実行
    super().__init__()

    self.geometry('250x250')
    self.title('Name App')

    #Labelウィジェットの生成
    self.label_1 = tk.Label(
      self,
      text = '名前を入力してください'
    )

    #Entryウィジェットの生成
    self.entry_1 = tk.Entry(
      self,
      width = 20
    )

    #Buttonウィジェットの生成
    self.button_1 = tk.Button(
      self,
      text = '表示',
      command = self.clicked
    )

    #各列の割合を指定
    self.columnconfigure(0, weight = 1)

    #各行の割合を指定
    self.rowconfigure(0, weight = 1)
    self.rowconfigure(1, weight = 1)
    self.rowconfigure(2, weight = 1)

    #grid関数で配置
    self.label_1.grid(column = 0, row = 0, sticky = 's')
    self.entry_1.grid(column = 0, row = 1)
    self.button_1.grid(column = 0, row = 2, sticky = 'n')

  def clicked(self):
    messagebox.showinfo('Name App', self.entry_1.get())

#Applicationクラスのインスタンスを生成
app = Application()
app.mainloop()
