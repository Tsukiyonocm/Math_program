import tkinter as tk
import random


# First Line
root = tk.Tk()
root.geometry("800x600")

# Generate Random Numbers
def gen_ran_num(diff_val):
    rand_num = random.randint(0,diff_val)
    # print(f"variables chose are between 0 and {diff_val}")
    return rand_num

# Random Numbers to be used in problems
num_a = tk.IntVar()
num_b = tk.IntVar()
diff_val = 0

"""
Choice Screen Options -
This is the part of the program where you can choose which type of math problem you would like to do.
"""
addition_button = tk.Button(root, text="Addition", width = 20, command=lambda: difficulty_choice())
addition_button.grid(row=1, column=1, padx=5, pady=5, ipadx=15)

subtraction_button = tk.Button(root, text="Subtraction", width = 20, command=lambda: not_active())
subtraction_button.grid(row=1, column=2, padx=5, pady=5, ipadx=15)

multiplication_button = tk.Button(root, text="Multiplication", width = 20, command=lambda: not_active())
multiplication_button.grid(row=2, column=1, padx=5, pady=5, ipadx=15)

division_button = tk.Button(root, text="Division", width = 20, command=lambda: not_active())
division_button.grid(row=2, column=2, padx=5, pady=5, ipadx=15)


"""
Difficulty Options -
Here is where you choose how difficult you would like the problem to be. Choices are: 1, 10, 100, 1000.
"""
one_button = tk.Button(root, text="Max Value: 9", width = 15, command=lambda: add_diff_set_1())
one_button.grid_forget()

ten_button = tk.Button(root, text="Max Value: 99", width = 15, command=lambda: add_diff_set_10())
ten_button.grid_forget()

hund_button = tk.Button(root, text="Max Value: 999", width = 15, command=lambda: add_diff_set_100())
hund_button.grid_forget()

thou_button = tk.Button(root, text="Max Value: 9999", width = 15, command=lambda: add_diff_set_1000())
thou_button.grid_forget()


# First label
num_1_label = tk.Label(root, textvariable = num_a)
num_1_label.grid_forget()

# Math Symbol
symbol_1_label = tk.Label(root, text=" + ")
symbol_1_label.grid_forget()

# Second Label
num_2_label = tk.Label(root, textvariable = num_b)
num_2_label.grid_forget()

# Equal Sign
equal_label = tk.Label(root, text=" = ")
equal_label.grid_forget()

# Answer Entry Box
answer_entry = tk.Entry(root)
answer_entry.grid_forget()

# Check Answer Button
check_button = tk.Button(root, text="Check Answer", command=lambda: check_answer_add())
check_button.grid_forget()

# Another Problem? Button
another_button = tk.Button(root, text="Another Problem?", command=lambda: another_problem(diff_val))
another_button.grid_forget()

# Give Up Button
give_up = tk.Button(root, text="Give up?", command=lambda: gave_up())
give_up.grid_forget()

# Quit Button
quit_button = tk.Button(root, text="Quit For Now?", command=lambda: quit_prog())
quit_button.grid(row=4, column=1, columnspan=5, sticky="we", padx=5, pady=5)

# Status Bar
status_bar_var = tk.StringVar()
status_bar_label = tk.Label(root, textvariable=status_bar_var)
status_bar_label.grid_forget()


def check_answer_add():
    is_num()
    if num_a.get() + num_b.get() == int(answer_entry.get()):
        status_bar_var.set(f"This was correct. \n Would you like to do another problem?")
        check_button.grid_forget()
        another_button.grid(row=3, column=1, columnspan=5, sticky="we", pady=10)
    else:
        status_bar_var.set(f"This was incorrect, try again!")
        answer_entry.delete(0, "end")
        quit_button.grid_forget()
        give_up.grid(row=4, column=1, columnspan=5, sticky="we", padx=5, pady=5)
    print(answer_entry.get())


def is_num():
    try:
        int(answer_entry.get())
    except ValueError:
        status_bar_var.set(f"This was not a number! Try again!")
        answer_entry.delete(0, "end")


def delete_status():
    answer_entry.delete(0, "end")
    status_bar_var.set("")


def difficulty_choice():
    one_button.grid(row=1, column=1, padx=10, pady=10)
    ten_button.grid(row=1, column=2, padx=10, pady=10)
    hund_button.grid(row=2, column=1, padx=10, pady=10)
    thou_button.grid(row=2, column=2, padx=10, pady=10)
    turn_off_math_type()

def add_diff_set_1():
    global diff_val
    diff_val = 10
    addition_choice(diff_val)
    turn_off_diff_opt()

def add_diff_set_10():
    global diff_val
    diff_val = 100
    addition_choice(diff_val)
    turn_off_diff_opt()

def add_diff_set_100():
    global diff_val
    diff_val = 1000
    addition_choice(diff_val)
    turn_off_diff_opt()

def add_diff_set_1000():
    global diff_val
    diff_val = 10000
    addition_choice(diff_val)
    turn_off_diff_opt()

def another_problem(diff_val):
    num_a.set(gen_ran_num(diff_val))
    num_b.set(gen_ran_num(diff_val))
    another_button.grid_forget()
    delete_status()
    turn_on_add()

def addition_choice(diff_val):
    another_problem(diff_val)
    turn_on_add()

def turn_on_add():
    num_1_label.grid(row=1, column=1)
    symbol_1_label.grid(row=1, column=2)
    num_2_label.grid(row=1, column=3)
    equal_label.grid(row=1, column=4)
    answer_entry.grid(row=1, column=5)
    check_button.grid(row=2, column=1, columnspan=5, sticky="we", pady=10)
    quit_button.grid(row=4, column=1, columnspan=5, sticky="we", padx=5, pady=5)
    status_bar_label.grid(row=100, column=1, columnspan=5, ipadx=5, ipady=5)

def turn_off_math_type():
    addition_button.grid_forget()
    subtraction_button.grid_forget()
    multiplication_button.grid_forget()
    division_button.grid_forget()

def turn_off_diff_opt():
    one_button.grid_forget()
    ten_button.grid_forget()
    hund_button.grid_forget()
    thou_button.grid_forget()

def quit_prog():
    root.destroy()

def gave_up():
    answer = num_a.get() + num_b.get()
    status_bar_var.set(f"The correct answer was: {answer}")
    another_button.grid(row=3, column=1, columnspan=5, sticky="we", pady=10)
    give_up.grid_forget()

def not_active():
    # for testing purposes only
    status_bar_label.grid(row=100, column=1, columnspan=5, ipadx=5, ipady=5)
    status_bar_var.set(f"This is not active yet!! Sorry!")

# Final Line
root.mainloop()
