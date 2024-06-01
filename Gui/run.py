import sys
import os
import tkinter as tk
import random

from errors import InvalidUserInputError, ZeroUserInputError, NegativeInputError, ChooseWrongWordError
from random_list_of_words import random_list
window = tk.Tk()

list_of_words = random_list()
answer = random.choice(list_of_words)
num_of_chances = 0
counter = 1 

list_lbl = tk.Label(
    master=window,
    fg="#000080",
    text=f"{list_of_words}",
    width=60,
)

list_lbl.grid(row=0, column=1, columnspan=3,)

result_lbl = tk.Label(
    master=window,
    text="set the number of chances",
    width=40,
)

result_lbl.grid(row=3, column=1, columnspan=3)

chances_lbl = tk.Label(
    master=window,
    text="chances: ",
    height=2,
    width=20,
)

chances_lbl.grid(row=1, column=0, columnspan=1)

chances_ent = tk.Entry(
    master=window,
    width=50,
)

chances_ent.grid(row=1, column=1, columnspan=3)


def get_num_of_chances_from_user(*args):  
    global num_of_chances
    
    num_of_chances = chances_ent.get()
    len_list = len(list_of_words)
    try:
        num_of_chances = int(num_of_chances)
        if num_of_chances >= len_list:
            raise InvalidUserInputError

        if num_of_chances == 0:
            raise ZeroUserInputError
        
        if num_of_chances < 0:
            raise NegativeInputError
        
        chances_ent.config(state="disabled")
        set_btn.config(state="disabled")
        choice_btn.config(state="active")
        num_of_chances = int(num_of_chances)
        result_lbl['text'] = "You can guess {} times.".format(num_of_chances)

    except ValueError:
        result_lbl['text'] = "enter integer number"
        
    except InvalidUserInputError:
        result_lbl["text"] = "enter number less than the length of the list"
    
    except ZeroUserInputError:
        result_lbl["text"] = "zero is invalid input. Please try again"
    
    except NegativeInputError:
        result_lbl["text"] = "enter positive number"


def guess_the_answer(*args ,answer:str = answer, my_list:list[str] = list_of_words):
    global counter
    
    user_choice = guess_ent.get()
    if counter == num_of_chances:
        result_lbl['text'] = f"You lost the game, The answer was {answer}"
        guess_ent.config(state='disabled')
        choice_btn.config(state="disabled")
    
    else: 
        try:
            if user_choice not in my_list:
                raise ChooseWrongWordError
            else:
                result_lbl["text"] = f"{num_of_chances - counter}"
                counter += 1
                if user_choice == answer:
                    result_lbl['text'] = "You won the game!"
                    choice_btn.config(state="disabled")
                    
        except ChooseWrongWordError:
            result_lbl["text"] = "Your word must be choosen from the list."
              
set_btn = tk.Button(
    master=window,
    fg="red",
    text="set",
    width= 3,
    command=get_num_of_chances_from_user
)

set_btn.grid(row=1, column=4, columnspan=2)

guess_lbl = tk.Label(
    master=window,
    text="guess: ",
    height=3,
    width=5,
)

guess_lbl.grid(row=2, column=0, columnspan=1)

guess_ent = tk.Entry(
    master=window,
    width=50,
)

guess_ent.grid(row=2, column=1, columnspan=3)

choice_btn = tk.Button(
    master=window,
    fg="#32CD32",
    text="word",
    width= 3,
    state="disabled",
    command= lambda : guess_the_answer()
)

choice_btn.grid(row=2, column=4, columnspan=2)

def restart_program(*args):
    """Restarts the current program.
    Note: this function does not return. Any cleanup action (like
    saving data) must be done before calling this function."""
    python = sys.executable
    os.execl(python, python, * sys.argv)
    
restart_btn = tk.Button(
    master=window,
    width=3,
    fg = "blue",
    text = "reset",
    command= restart_program
)

restart_btn.grid(row=3, column=4, columnspan=2)

# def bin_button():
#     window.bind("<s>", get_num_of_chances_from_user)
#     window.bind("<w>", guess_the_answer)
#     window.bind("<q>", quit)
#     window.bind("<r>", restart_program)

# bin_button()

window.mainloop()

