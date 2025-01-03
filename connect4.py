import tkinter as tk
from tkinter import messagebox
piece = "red"
piece2 = "yellow"
#constants
rows, cols = 6, 7
isRedTurn = True

#making turns and tracking who is playing as well as detterming how to switch
def turn():
    global isRedTurn
    if isRedTurn:
        isRedTurn = False
    else:
        isRedTurn = True
        
def currentPlayer():
    if isRedTurn:
        return "Red"
    else:
        return "Yellow"
    
def winCon():
    for c in range(cols-3):
        for r in range (rows):
            if (
               buttons[r][c].cget("bg") == currentPlayer()
               and buttons[r][c + 1].cget("bg") == currentPlayer()
               and buttons[r][c + 2].cget("bg") == currentPlayer()
               and buttons[r][c + 3].cget("bg") == currentPlayer()
):
                winning_person()

def winCon2():
    for r in range(rows-3):
        for c in range (cols):
            if (
               buttons[r][c].cget("bg") == currentPlayer()
               and buttons[r + 1][c].cget("bg") == currentPlayer()
               and buttons[r + 2][c].cget("bg") == currentPlayer()
               and buttons[r + 3][c].cget("bg") == currentPlayer()
):
                winning_person()
def winCon3():
    for r in range(3, rows):  
        for c in range(cols - 3):  
            if (
                buttons[r][c].cget("bg") == currentPlayer()
                and buttons[r - 1][c + 1].cget("bg") == currentPlayer()
                and buttons[r - 2][c + 2].cget("bg") == currentPlayer()
                and buttons[r - 3][c + 3].cget("bg") == currentPlayer()
            ):
                winning_person()
                return
def winCon4():
    piece = currentPlayer()  
    
    
    for r in range(rows - 3):  
        for c in range(cols - 3):  
            if (
                buttons[r][c].cget("bg") == piece and
                buttons[r + 1][c + 1].cget("bg") == piece and
                buttons[r + 2][c + 2].cget("bg") == piece and
                buttons[r + 3][c + 3].cget("bg") == piece
            ):
                winning_person()  
                return
def button_clicked(r, c):
    global isRedTurn
    for racism in reversed(range(rows)):
     if buttons[racism][c].cget("bg") == "Black":
         buttons[racism][c].configure(bg=currentPlayer())
         winCon()
         winCon2()
         winCon3()
         winCon4()
         turn()  # Switch turn to the other player
         return
    messagebox.showinfo("Invalid Move", "Column is full!")   
    

def winning_person():
    win_window = tk.Toplevel(root)
    win_window.title("Game Finished")
    tk.Label(win_window, text=f"{currentPlayer()} Wins!", font=("Times New Roman", 24)).pack(pady=20)
    tk.Button(win_window, text="OK", command=win_window.destroy).pack(pady=10)
    

def draw_screen():
    tie_window = tk.Toplevel(root)
    tie_window.title("Game Finished")
    tk.Label(tie_window, text="No one wins. Draw.", font=("Times New Roman",24)).pack(pady=20)
    tk.button(tie_window, text="OK",command=tie_window.destroy).pack(pady=10)

def reset_everything():
    for r in range(rows):
        for c in range(cols):
            buttons[r][c].config(bg="Black", state="normal")
            
black = "Black"
root = tk.Tk()
root.title("Connect Four")

buttons = [[None for _ in range(cols)] for _ in range(rows)]
for r in range(rows):
    for c in range(cols):
        # Create a button for each cell in the grid and link it to `my_function`
        button = tk.Button(root, bg = "Black", width=6, height=3, 
                           command=lambda r=r, c=c: button_clicked(r, c))
        button.grid(row=r, column=c, padx=1, pady=1)
        buttons[r][c] = button

reset_button = tk.Button(root, text="Reset", font=("Times New Roman",24), command=reset_everything)
reset_button.grid(row=rows, column=0, columnspan=cols, pady=10)


root.mainloop()