import tkinter as tk
from tkinter import messagebox
import random
import re
import os #追加その1

# カードの画像ファイル名
files = ['cardClubs1.png',
         'cardClubs2.png', 
         'cardClubs3.png', 
         'cardClubs4.png', 
         'cardClubs5.png',
         'cardHearts1.png', 
         'cardHearts2.png', 
         'cardHearts3.png', 
         'cardHearts4.png', 
         'cardHearts5.png'] 

# グローバル変数
# 1枚目に選択したカードの数字
first_card = None    
# 1枚目に選択したカードの番号
first_index = None   
card_img = []   # カードの表面の画像
cards = []      # カードを格納
count = 0

# 追加その2 現在のスクリプトファイルの場所を取得
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# 初期化関数
def initialise():
  global first_card, first_index, count #修正その1

  first_card = None
  first_index = None
  count = len(files) / 2
  random.shuffle(files)   # カードのシャッフル

  # カードの生成
  card_img.clear()
  cards.clear()
  for num, img_name in enumerate(files):
    # 追加その3 os.path.joinを使って正しいパスを組み立てる
    img_path = os.path.join(BASE_DIR, 'Cards', img_name)
    card_img.append(
      # 修正前のコード1 tk.PhotoImage(file='Cards\\'+img_name))
      tk.PhotoImage(file=img_path)) #修正その1
    # カードの表示にCanvasウィジェットを使用
    cards.append([tk.Canvas(
      root, 
      width=140, 
      height=190), 
      None])
    card_set(num, False)

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

  cards[num][0].bind(
    '<ButtonPress-1>', 
    lambda event: click_img(event, num))
    
  r, n = 0, num
  if num > 4:
    r, n = 1, num - 5
  cards[num][0].grid(row=r, column=n)
  cards[num][1] = flag

# ハンドラ関数
def click_img(event, num):  
  global first_card
  global first_index
  global count

  # すでに表面になっている場合は終了
  if cards[num][1]:
    return

  # カードを表面（True）にする
  card_set(num, True)
  if first_card != None:
    # ファイル名から数字を抜き出す
    second_card = re.sub(r'\D', '', files[num])
    # 同じ数字なら
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
    # ファイル名から数字を抜き出す
    first_card = re.sub(r'\D', '', files[num])

root = tk.Tk()

# 修正前コード2 トランプの裏面の画像ファイルを読み込む
# card_back_img = tk.PhotoImage(
#   file=r'Cards\cardBack_blue1.png')  

# 修正その2 裏面の画像読み込みも絶対パスに必要
back_img_path = os.path.join(BASE_DIR, 'Cards', 'cardBack_blue1.png')
card_back_img = tk.PhotoImage(file=back_img_path)

initialise()

# タイトルバーのアイコンを設定
# iconphoto は initialise の後に移動させる
if card_img: # 追加その4 リストが空でないことを確認する安全装置
  # 読み込みに失敗してリストが空のままだった場合、card_img[0]にアクセス
  # しようとするとエラーが発生してプログラムが止まってしまう
  root.iconphoto(False, card_img[0])
root.title('Memory App')

root.mainloop()