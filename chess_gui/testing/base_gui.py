import tkinter as tk
from tkinter.font import *
from tkinter import *
import os
import chess
import random

root = tk.Tk()
square_size = 80

canvas = tk.Canvas(root,height = 656, width = 1000)
canvas.pack()

frame = tk.Frame(canvas,bg = 'white')
frame.place(width = 656,height = 656)

details = tk.Frame(canvas,bg = '#263D42',width = 344,height = 656)
details.place(relx = 656/1000, rely = 0)

fontStyle = Font(family="Trebuchet MS", size=20,weight = 'bold')
title = tk.Label(details,text = "《KASTANET v2.1》",font = fontStyle,bg = '#263D42',fg = 'white')
title.place(relx = 0.15,rely = 0)
root.mainloop()