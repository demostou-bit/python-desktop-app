import tkinter as tk
from tkinter import messagebox
import random
import re

#カードの画像ファイル名
files = ['CardClubs1.png',
         'CardClubs2.png',
         'CardClubs3.png',
         'CardClubs4.png',
         'CardClubs5.png',
         'CardHearts1.png',
         'CardHearts2.png',
         'CardHearts3.png',
         'CardHearts4.png',
         'CardHearts5.png',]
#グローバル変数
#1枚目に選択したカードの数字
first_card = None
#1枚目に選択したカードの番号
first_index = None
card_img = [] #カードの表面の画像
cards = [] #カードを格納
count = 0

#初期化関数
def initialise():
  global first_card
  global first_index
  global count

  first_card = None
  first_index = None
  count = len(files) / 2
  random.shuffle(files) #3カードのシャッフル

  #カードの生成
  card_img.clear()
  cards.clear()
  #4
  for num, img_name in enumerate(files):
    card_img.append(
      tk.PhotoImage(file='Cards\\'+img_name))
    #1カードの表示にCanvasウィジェットを使用
    cards.append([tk.Canvas(
      root,
      width=140,
      height=190),
      None])
    card_set(num, False)

#5
def card_set(num, flag):
  if flag:
    cards[num][0].delete('all')
    cards[num][0].create_image(
      0,
      0,
      anchor='nw',
      image=card_img[num])
  else:
    cards[num][0].delete('all')
    cards[num][0].create_image(
      0,
      0,
      anchor='nw',
      image=card_back_img)
  
  #2
  cards[num][0].bind(
    '<ButtonPress-1>',
    lambda event: click_img(event, num))
  
  r, n = 0, num
  if num > 4:
    r, n = 1, num -5
  cards[num][0].grid(row=r, column=n)
  cards[num][1] = flag

#8 ハンドラ関数
def click_img(event, num):
  global first_card
  global first_index
  global count

  #すでに表面になっている場合は終了
  if cards[num][1]:
    return
  
  #カードを表面(True)にする
  card_set(num, True)
  if first_card != None:
    #6ファイル名から数字を抜き出す
    second_card = re.sub(r'\D', '', files[num])
    #同じ数字なら
    if second_card == first_card:
      count = count - 1
      if count > 0:
        messagebox.showinfo(
          'Memory App',
          '同じです！')
      else:
        messagebox.showinfo(
          'Memory App',
          'すべてそろいました！')
        initialise()
    else:
      messagebox.showinfo(
          'Memory App',
          '違います！')
      card_set(num, False)
      card_set(first_index, False)
    first_card, first_index = None, None
  else:
    first_index = num
    #7ファイル名から数字を抜き出す
    first_card = re.sub(r'\D', '', files[num])

root = tk.Tk()

#カードの裏面の画像ファイルを読み込む
card_back_img = tk.PhotoImage(
  file='Cards\cardBack_bluel.png')

initialise()

#タイトルバーのアイコンを設定
#9
root.iconphoto(False, card_img[0])
root.title('Memory App')

root.mainloop()