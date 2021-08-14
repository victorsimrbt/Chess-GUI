from gui_classes import *
import os

os.chdir(r'C:\Users\v_sim\Desktop\Files\Code\Python\GUI\chess_gui\pieces')

root = tk.Tk()
root.title('Chess GUI')
square_size = 80

canvas = tk.Canvas(root,height = 500, width = 700)
canvas.pack()

frame = tk.Frame(canvas,bg = 'white')
frame.place(width = 500,height = 500)

details = tk.Frame(canvas,bg = '#263D42',width = 700,height = 500)
details.place(relx = 500/700, rely = 0)

chessboard = ChessBoard()
chessboard.display_board(frame,details)

fontStyle = Font(family="Trebuchet MS", size=15,weight = 'bold')
title = tk.Label(details,text = "Chess GUI v1.0.0 ",font = fontStyle,bg = '#263D42',fg = 'white')
title.place(relx = 0,rely = 0)
root.mainloop()
