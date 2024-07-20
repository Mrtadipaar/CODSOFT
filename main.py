import tkinter as tk
from tkinter import messagebox
import math

board = [' ' for _ in range(9)]
def check_winner(board, player):
    win_conditions = [(0, 1, 2), (3, 4, 5), (6, 7, 8),
                      (0, 3, 6), (1, 4, 7), (2, 5, 8),
                      (0, 4, 8), (2, 4, 6)]
    for condition in win_conditions:
        if board[condition[0]] == board[condition[1]] == board[condition[2]] == player:
            return True, condition
    return False, []
def is_board_full(board):
    return ' ' not in board

def minimax(board, depth, is_maximizing):
    if check_winner(board, 'O')[0]:
        return 1
    if check_winner(board, 'X')[0]:
        return -1
    if is_board_full(board):
        return 0

    if is_maximizing:
        best_score = -math.inf
        for i in range(9):
            if board[i] == ' ':
                board[i] = 'O'
                score = minimax(board, depth + 1, False)
                board[i] = ' '
                best_score = max(score, best_score)
        return best_score
    else:
        best_score = math.inf
        for i in range(9):
            if board[i] == ' ':
                board[i] = 'X'
                score = minimax(board, depth + 1, True)
                board[i] = ' '
                best_score = min(score, best_score)
        return best_score
def best_move(board):
    best_score = -math.inf
    move = 0
    for i in range(9):
        if board[i] == ' ':
            board[i] = 'O'
            score = minimax(board, 0, False)
            board[i] = ' '
            if score > best_score:
                best_score = score
                move = i
    return move
def button_click(i):
    if board[i] == ' ':
        board[i] = 'X'
        buttons[i].config(text='X', fg='blue', state=tk.DISABLED)

        won, condition = check_winner(board, 'X')
        if won:
            highlight_winner(condition)
            messagebox.showinfo("Tic-Tac-Toe", "Congratulations! You win!")
            reset_board()
            return

        if is_board_full(board):
            messagebox.showinfo("Tic-Tac-Toe", "It's a tie!")
            reset_board()
            return

        ai_move = best_move(board)
        board[ai_move] = 'O'
        buttons[ai_move].config(text='O', fg='red', state=tk.DISABLED)

        won, condition = check_winner(board, 'O')
        if won:
            highlight_winner(condition)
            messagebox.showinfo("Tic-Tac-Toe", "AI wins! Better luck next time.")
            reset_board()
            return

        if is_board_full(board):
            messagebox.showinfo("Tic-Tac-Toe", "It's a tie!")
            reset_board()
            return

def highlight_winner(condition):
    for index in condition:
        buttons[index].config(bg='lightgreen')

def reset_board():
    global board
    board = [' ' for _ in range(9)]
    for button in buttons.values():
        button.config(text='', fg='black', bg='SystemButtonFace', state=tk.NORMAL)


root = tk.Tk()
root.title("Tic-Tac-Toe")
button_font = ('Helvetica', 24, 'bold')
button_width = 5
button_height = 2

buttons = {}
for i in range(9):
    button = tk.Button(root, text='', font=button_font, width=button_width, height=button_height,
                       command=lambda i=i: button_click(i), relief='raised', bd=3, bg='white',
                       activebackground='lightgrey')
    button.grid(row=i // 3, column=i % 3, padx=5, pady=5)
    buttons[i] = button


reset_button = tk.Button(root, text="Reset", font=button_font, command=reset_board, relief='raised', bd=3,
                         bg='lightgrey', activebackground='grey')
reset_button.grid(row=3, column=0, columnspan=3, pady=20)

root.mainloop()
