'''
def sum(a, b, c):
    return a + b + c

def printBoard(xState, zState):
    zero = 'X' if xState[0] == 1 else ('O' if zState[0] == 1 else 0)
    one = 'X' if xState[1] == 1 else ('O' if zState[1] == 1 else 1)
    two = 'X' if xState[2] == 1 else ('O' if zState[2] == 1 else 2)
    three = 'X' if xState[3] == 1 else ('O' if zState[3] == 1 else 3)
    four = 'X' if xState[4] == 1 else ('O' if zState[4] == 1 else 4)
    five = 'X' if xState[5] == 1 else ('O' if zState[5] == 1 else 5)
    six = 'X' if xState[6] == 1 else ('O' if zState[6] == 1 else 6)
    seven = 'X' if xState[7] == 1 else ('O' if zState[7] == 1 else 7)
    eight = 'X' if xState[8] == 1 else ('O' if zState[8] == 1 else 8)
    
    print(f"{zero} | {one} | {two}")
    print(f"{three} | {four} | {five}")
    print(f"{six} | {seven} | {eight}")
    
def checkWin(xState, zState):
    win = [[0,1,2], [3,4,5], [6,7,8], [0,3,6], [1,4,7], [2,5,8], [0,4,8], [2,4,6]]
    for win in win:
        if(sum(xState[win[0]], xState[win[1]], xState[win[2]]) == 3):
            print("X won the match!")
            return 1
        if(sum(zState[win[0]], zState[win[1]], zState[win[2]]) == 3):
            print("O won the match!")
            return 0
    
    return -1

if __name__ == '__main__':
    xState = [0, 0, 0, 0, 0, 0, 0, 0, 0]
    zState = [0, 0, 0, 0, 0, 0, 0, 0, 0]
    turn = 1
    
    print("[INSTRUCTIONS]   X will make the first move!")
    while True:
        
        printBoard(xState, zState)
        value = int(input("Select a position: "))
        if turn == 1:
            xState[value] = 1
        else:
            zState[value] = 1
        
        checkWin(xState, zState)
        if(checkWin(xState, zState) != -1):
            print("MATCH OVER")
            break
        turn = 1 - turn
'''
import tkinter as tk
from tkinter import messagebox

def sum(a, b, c):
    return a + b + c

def print_board():
    zero = 'X' if x_state[0] == 1 else ('O' if z_state[0] == 1 else 0)
    one = 'X' if x_state[1] == 1 else ('O' if z_state[1] == 1 else 1)
    two = 'X' if x_state[2] == 1 else ('O' if z_state[2] == 1 else 2)
    three = 'X' if x_state[3] == 1 else ('O' if z_state[3] == 1 else 3)
    four = 'X' if x_state[4] == 1 else ('O' if z_state[4] == 1 else 4)
    five = 'X' if x_state[5] == 1 else ('O' if z_state[5] == 1 else 5)
    six = 'X' if x_state[6] == 1 else ('O' if z_state[6] == 1 else 6)
    seven = 'X' if x_state[7] == 1 else ('O' if z_state[7] == 1 else 7)
    eight = 'X' if x_state[8] == 1 else ('O' if z_state[8] == 1 else 8)
    
    button_0.config(text=f"{zero}")
    button_1.config(text=f"{one}")
    button_2.config(text=f"{two}")
    button_3.config(text=f"{three}")
    button_4.config(text=f"{four}")
    button_5.config(text=f"{five}")
    button_6.config(text=f"{six}")
    button_7.config(text=f"{seven}")
    button_8.config(text=f"{eight}")

def check_win():
    win = [[0,1,2], [3,4,5], [6,7,8], [0,3,6], [1,4,7], [2,5,8], [0,4,8], [2,4,6]]
    for win_combination in win:
        if sum(x_state[win_combination[0]], x_state[win_combination[1]], x_state[win_combination[2]]) == 3:
            messagebox.showinfo("Winner", "X won the match!")
            return True
        if sum(z_state[win_combination[0]], z_state[win_combination[1]], z_state[win_combination[2]]) == 3:
            messagebox.showinfo("Winner", "O won the match!")
            return True
    
    return False

def make_move(position):
    global turn
    if x_state[position] == 0 and z_state[position] == 0:
        if turn == 1:
            x_state[position] = 1
        else:
            z_state[position] = 1
        if check_win():
            messagebox.showinfo("Match Over", "Match Over")
            root.quit()
        turn = 1 - turn
        print_board()

root = tk.Tk()
root.title("Tic Tac Toe")

x_state = [0, 0, 0, 0, 0, 0, 0, 0, 0]
z_state = [0, 0, 0, 0, 0, 0, 0, 0, 0]
turn = 1

button_0 = tk.Button(root, text="", font=("Arial", 20), width=5, height=2, command=lambda: make_move(0))
button_0.grid(row=0, column=0)
button_1 = tk.Button(root, text="", font=("Arial", 20), width=5, height=2, command=lambda: make_move(1))
button_1.grid(row=0, column=1)
button_2 = tk.Button(root, text="", font=("Arial", 20), width=5, height=2, command=lambda: make_move(2))
button_2.grid(row=0, column=2)
button_3 = tk.Button(root, text="", font=("Arial", 20), width=5, height=2, command=lambda: make_move(3))
button_3.grid(row=1, column=0)
button_4 = tk.Button(root, text="", font=("Arial", 20), width=5, height=2, command=lambda: make_move(4))
button_4.grid(row=1, column=1)
button_5 = tk.Button(root, text="", font=("Arial", 20), width=5, height=2, command=lambda: make_move(5))
button_5.grid(row=1, column=2)
button_6 = tk.Button(root, text="", font=("Arial", 20), width=5, height=2, command=lambda: make_move(6))
button_6.grid(row=2, column=0)
button_7 = tk.Button(root, text="", font=("Arial", 20), width=5, height=2, command=lambda: make_move(7))
button_7.grid(row=2, column=1)
button_8 = tk.Button(root, text="", font=("Arial", 20), width=5, height=2, command=lambda: make_move(8))
button_8.grid(row=2, column=2)

root.mainloop()
