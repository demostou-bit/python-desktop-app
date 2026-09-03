#Tkinterで利用できるフォント一覧を表示する
import tkinter as tk
from tkinter import font

root = tk.Tk()
fonts = font.families()
print(fonts)
print(len(fonts)) #フォントの数を表示