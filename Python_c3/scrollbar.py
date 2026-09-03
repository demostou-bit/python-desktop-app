import tkinter as tk

#表示テキストの生成
sample = ''
for i in range(20):
  hira = [chr(j) for j in range(ord('あ'),
                                ord('ん') + 1)]
  hira = ''.join(hira)
  sample = sample + hira + '\n'

#トップレベルウィンドウの生成
root = tk.Tk()
root.geometry('250x150')
root.title('Scrollbar Text')

#Textウィジェットの生成と配置
text = tk.Text(
  root,
  wrap=tk.NONE)
#テキストを挿入
text.insert('1.0', sample)
text.place(x=10, y=10, width=220, height=120)

#垂直方向のScrollbarウィジェットの生成
scroll_v = tk.Scrollbar(
  root,
  orient=tk.VERTICAL, #垂直方向を指定
  command=text.yview) #Textウィジェットを設定
#Textウィジェットを設定
text['yscrollcommand'] = scroll_v.set
scroll_v.place(x=230, y=10, height=120)

#水平方向のScrollbarウィジェットの生成
scroll_h = tk.Scrollbar(
  root,
  orient=tk.HORIZONTAL, #水平方向を指定
  command=text.xview) #Textウィジェットを設定
#Textウィジェットを設定
text['xscrollcommand'] = scroll_h.set
scroll_h.place(x=230, y=10, height=120)

root.mainloop()
