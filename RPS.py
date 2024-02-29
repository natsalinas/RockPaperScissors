import random
import tkinter as tk

window = tk.Tk() 
window.geometry("600x300")
window.title("Rock, Paper, Scissors!")

#font=('Comic Sans MS',16)
intro = "Welcome to the game of Rock, Paper, Scissors.\n\nYou may select one out of the three available options. Select 'Shoot' once you are ready to go against your opponent.\n\nMay the odds be in your favor!"
label = tk.Label(window, text=intro, anchor="w", justify="left", wraplength=500)
label.pack(pady=20)

def play():
    computer = random.choice(["Rock", "Paper", "Scissors"])
    return computer

def is_win(player, opponent):
    # return true if player wins 
    # r > s, s > p, p > r
    if(player == "Rock" and opponent == "Scissors") or (player == "Scissors" and opponent == "Paper") or (player == "Paper" and opponent == "Rock"):
        return True

# Create player class
# Each player has it's own buttons and textbox 
class game:
    def __init__(self, main):
        top = tk.Frame(main)
        bottom = tk.Frame(main)
        top.pack(side="top")
        bottom.pack(side="bottom", expand=True)

        # buttons on the top 
        self.r_button = tk.Button(top, text="Rock", width=10, height=2, command=self.rock_button)
        self.r_button.pack(side="left")

        self.p_button = tk.Button(top, text="Paper", width=10, height=2, command=self.paper_button)
        self.p_button.pack(side="left")

        self.s_button = tk.Button(top, text="Scissors", width=10, height=2, command=self.scissors_button)
        self.s_button.pack(side="left")

        self.sh_button = tk.Button(top, text="Shoot!", width=10, height=2, command=self.shoot_button, highlightbackground="#2E35FF", fg="#3B81FF")
        self.sh_button.pack(side="left", padx=20)

        self.p1_textbox = tk.Text(bottom, height=1, width=20, font=("",16))
        self.p1_textbox.pack(side="left")

        self.vs_label = tk.Label(bottom, text="VS", font=("",16))
        self.vs_label.pack(side="left", padx=5)

        self.ai_textbox = tk.Text(bottom, height=1, width=20, font=("",16))
        self.ai_textbox.pack(side="left")

        self.results_label = tk.Label(window, text="", font=("",18))
        self.results_label.pack(side="bottom")


    def rock_button(self):
        self.p1_textbox.delete(1.0, "end") # clear existing text
        self.p1_textbox.insert("end", "Rock")

    def paper_button(self):
        self.p1_textbox.delete(1.0, "end") # clear existing text
        self.p1_textbox.insert("end", "Paper")

    def scissors_button(self):
        self.p1_textbox.delete(1.0, "end") # clear existing text
        self.p1_textbox.insert("end", "Scissors")

    def shoot_button(self):
        # grab both player and AI selections. 
        p_choice = self.p1_textbox.get("1.0", "end-1c")
        if (p_choice == ""):
            self.results_label.config(text="Please select a valid option.", fg="white")
        else:
            computer_choice = play()

            # update computer textbox
            self.ai_textbox.delete(1.0, "end") # clear existing text
            self.ai_textbox.insert("end", computer_choice)
            
            # compare selections to determine who won. 
            if p_choice == computer_choice:
                self.results_label.config(text="Tie.", fg="yellow")
            # r > s, s > p, p > r
            elif is_win(p_choice, computer_choice):
                self.results_label.config(text="You won!", fg="#76BA1B")
            else: 
                self.results_label.config(text="You lost!", fg="#FF2800")
    
# create game window
g = game(window)

# print(play())


window.mainloop()