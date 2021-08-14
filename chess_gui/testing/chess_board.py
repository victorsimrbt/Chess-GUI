import chess
import tkinter as tk
import os
            
class Square():
    def __init__(self,idx,board):
        self.row = idx // 8 
        self.column = idx % 8
        self.idx = idx
        self.square = chess.Square()
        
        if (self.row%2 == self.column%2):
            self.color = '#eeeed2'
        else:
            self.color = '#769656'
        self.get_img(board)
        
    def get_img(self,board):
        self.piece = board.piece_at(self.idx)
        piece = board.piece_at(self.idx)
        if piece:
            piece_symbol = piece.symbol()
            
            filename = ''
            if piece_symbol.isupper():
                filename = '_'
                
            filename += piece_symbol.lower()
            filename += '.png'
            self.image = filename
        else:
            self.image = None
        

root = tk.Tk()

canvas = tk.Canvas(root,height = 656, width = 1000)
canvas.pack()

frame = tk.Frame(canvas,bg = 'white')
frame.place(width = 656,height = 656)

board = chess.Board()
for i in range(64):
    square = Square(i,board)
    if square.image:
        os.chdir(r'C:\Users\v_sim\Desktop\Files\Code\Python\GUI\chess_gui\pieces')
        blank_image = tk.PhotoImage(file = square.image)
    else:
        blank_image= tk.PhotoImage(file = 'q.png')
        
    b = tk.Button(frame, image=blank_image, bg = 'black', borderwidth=0)
    b.config(width=80, height=80)

print(frame.winfo_children())
root.mainloop()
