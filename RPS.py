import random
import tkinter as tk

p1_rock = 0
p1_paper = 0 
p1_scissors = 0 

def play():
    user = input("What is your choice?\n'r' for rock, 'p' for paper, 's' for scissors\n")
    computer = random.choice(['r', 'p', 's'])

    if user == computer:
        return 'tie'
    
    # r > s, s > p, p > r
    if is_win(user, computer):
        return 'You won!'
    
    return 'You lost!'

def is_win(player, opponent):
    # return true if player wins 
    # r > s, s > p, p > r
    if(player == 'r' and opponent == 's') or (player == 's' and opponent == 'p') or (player == 'p' and opponent == 'r'):
        return True
    
# if button is clicked, the selected "choice" is displayed on the text field. 
# Define function to get the information about the Button
def press_button(t):
    if t == 1:
        print("You selected Rock")
    elif t == 2:
        print("You selected Paper")
    elif t == 3:
        print("You selected Scissors")

#def update_p1(tk.Text, string):
#   tk.Text.insert(tk.END, string)




window = tk.Tk() 
window.geometry("600x300")
window.title("Rock, Paper, Scissors!")

label = tk.Label(window, text="Select your choice", font=('Arial',18))
label.grid(row=0)

# textbox to hold generated password 
p1_textbox = tk.Text(window, height=1, width=20, font=('Arial', 16))
p1_textbox.grid(row=4, column=0, padx=5)


r_button = tk.Button(window, text="Rock", width=10, font=('Arial', 18), command=lambda t= 1: press_button(t))
r_button.grid(row=1, column=0, pady=20)
if (p1_rock == 1):
    p1_textbox.insert(tk.END, "Rock")


p_button = tk.Button(window, text="Paper", width=10, font=('Arial', 18), command=lambda t= 2: press_button(t))
p_button.grid(row=1, column=1, padx=10, pady=20)

s_button = tk.Button(window, text="Scissors", width=10, font=('Arial', 18), command=lambda t= 3: press_button(t))
s_button.grid(row=1, column=2, padx=10, pady=20)

shoot_button = tk.Button(window, text="Shoot!", width=10, font=('Arial', 18), highlightbackground='green', fg='green', command=lambda t= "Shoot Clicked": press_button(t))
shoot_button.grid(row=7, column=1, pady=20)

p1_label = tk.Label(window, text="Player 1", font=('Arial',18))
p1_label.grid(row=5, column=0)

vs_label = tk.Label(window, text="VS", font=('Arial',18))
vs_label.grid(row=4, column=1)

# textbox to hold generated password 
ai_textbox = tk.Text(window, height=1, width=20, font=('Arial', 16))
ai_textbox.grid(row=4, column=2, padx=5)

ai_label = tk.Label(window, text="Computer", font=('Arial',18))
ai_label.grid(row=5, column=2)


# print(play())


window.mainloop()