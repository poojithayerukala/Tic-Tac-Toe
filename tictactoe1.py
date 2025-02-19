import tkinter as tk
from tkinter import messagebox

def check_win(board,player):
    for i in range(3):
        if all([board[i][j]==player for j in range(3)]):
            return True
        if all([board[j][i]==player for j in range(3)]):
            return True
    if all([board[i][i]==player for i in range(3)]):
        return True
    if all([board[i][2-i]==player for i in range(3)]):
        return True
    return False


def is_full(board):
    return all(cell!=" " for row in board for cell in row)


def on_button_click(row, col):
    global current_player
    if board[row][col]==" ":
        buttons[row][col].config(text=current_player)
        board[row][col]=current_player

        if check_win(board,current_player):
            messagebox.showinfo("Game Over",f"Player {current_player} wins!")
            reset_game()
        elif is_full(board):
            messagebox.showinfo("Game Over", "It's a draw!")
            reset_game()
        else:
            current_player="O" if current_player=="X" else "X"


def reset_game():
    global board,current_player
    board = [[" " for _ in range(3)] for _ in range(3)]
    for row in range(3):
        for col in range(3):
            buttons[row][col].config(text=" ")
    current_player = "X"


root = tk.Tk()
root.title("Tic-Tac-Toe")

board = [[" " for _ in range(3)] for _ in range(3)]
current_player = "X"

buttons = [[None for _ in range(3)] for _ in range(3)]
for i in range(3):
    for j in range(3):
        buttons[i][j] = tk.Button(root, text=" ", width=10, height=3, font=("Arial", 24),
                                  command=lambda row=i, col=j: on_button_click(row, col))
        buttons[i][j].grid(row=i, column=j)

root.mainloop()
