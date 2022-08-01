#!/Library/Frameworks/Python.framework/Versions/3.8/bin/python3
# Imports
from tkinter import *
import tkinter as ttk
import random 
import sys
from time import sleep

# Define the function for playing it in shell
def playTer():

    x = input("Rock, Paper, or Scissors? ") # Input for player choice
    y = random.randrange(2) # Computer choice (0 = Rock, 1 = paper, and 2 = scissors)
    print(y)
    # Game Logic
    if y == 0 and x == "Rock":
        sleep(0.5)
        print("Tie, both picked rock")
    elif y == 1 and x == "Rock":
        sleep(0.5)

        print("Computer wins, Paper beats Rock")
    elif y == 2 and x == "Rock":
        sleep(0.5)
        print("You win, Rock beats Scissors")
    elif y == 0 and x == "Paper":
        sleep(0.5)
        print("You win, Paper beats Rock")
    elif y == 1 and x == "Paper":
        sleep(0.5)
        print("Tie, both picked Paper")
    elif y == 2 and x == "Paper":
        sleep(0.5)
        print("Computer Wins, Scissors beat Paper")
    elif y == 0 and x == "Scissors":
        sleep(0.5)
        print("Computer Wins, Rock beats scissors")
    elif y == 1 and x == "Scissors":
        sleep(0.5)
        print("You Win, Scissors beat Paper")
    elif y == 2 and x == "Scissors":
        sleep(0.5)
        print("Tie, both picked scissors")
    else: 
        print("Try Again")
        playTer()


    # Loop quitter/restarter
    z = input("Play again? (y/n)")
    if z == "y":
        playTer()
    elif z == "n":
        print("Goodbye!")
        sleep(1)
        sys.exit()

# Define the function for playing it in a window
def playGUI():
    # Define the base window
    root = Tk()
    root.title("Rock Paper Scissors")
    # Define the game function
    def playR(): # Function for the Rock button
        y = random.randrange(4)
        if y == 0:
            L1= ttk.Label(frame, text="Tie, both picked rock")
            L1.pack()
        elif y == 1:
            L2 = ttk.Label(frame, text="You lose, Computer picked paper ")
            L2.pack()
        elif y == 2 or 3:
            L3 = ttk.Label(frame, text="You win, Computer picked Scissors")
            L3.pack()

    def playP(): # Function for the Paper button
        y = random.randrange(2)
        if y ==  0:
            L1 = ttk.Label(frame,text="You win, Computer picked Rock")
            L1.pack()
        elif y == 1:
            L2 = ttk.Label(frame,text="Tie, both picked Paper")
            L2.pack()
        elif y == 2:
            L3 = ttk.Label(frame,text="You lose, Computer picked Scissors")
            L3.pack()

    def playS(): # Function for the Scissors button
        y = random.randrange(2)
        if y == 0:
            L1 = ttk.Label(frame,text="You lose, Computer picked Rock")
            L1.pack()
        elif y == 1:
            L2 = ttk.Label(frame,text="You win, Computer picked Paper")
            L2.pack()
            
        elif y == 2:
            L3 = ttk.Label(frame,text=" Tie, both picked Scissors")
            L3.pack()
    
    # Define Frame(s)
    frame = ttk.LabelFrame(root,text="Rock, Paper, or Scissors?",padx=30, pady=30)
    frame.pack(padx=5,pady=5)

    # Define buttons to be put on screen
    a = ttk.Button(frame, text="Rock", command=playR)
    a.pack()
    b = ttk.Button(frame,text="Paper", command=playP)
    b.pack()
    c = ttk.Button(frame,text="Scissors", command=playS)
    c.pack()


    # Window updater
    root.mainloop()
            

# Choose whether to start game in terminal or window
u = input("Start Game in CLI or GUI? ")
if u == "CLI":
    playTer()
elif u == "GUI":
    playGUI()
else: print("Error, program exit imminent")

