import tkinter as tk
import random
import operator as op



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
math_type = ""
math_symbol = tk.StringVar(root, "")

"""
Choice Screen Options -
This is the part of the program where you can choose which type of math problem you would like to do.
"""
addition_button = tk.Button(root, text="Addition", width = 20, command=lambda m="add": difficulty_choice(m))
addition_button.grid(row=1, column=1, padx=5, pady=5, ipadx=15)

subtraction_button = tk.Button(root, text="Subtraction", width = 20, command=lambda m="sub": difficulty_choice(m))
subtraction_button.grid(row=1, column=2, padx=5, pady=5, ipadx=15)

multiplication_button = tk.Button(root, text="Multiplication", width = 20, command=lambda m="multi": not_active(m))
multiplication_button.grid(row=2, column=1, padx=5, pady=5, ipadx=15)

division_button = tk.Button(root, text="Division", width = 20, command=lambda m="div": not_active(m))
division_button.grid(row=2, column=2, padx=5, pady=5, ipadx=15)


"""
Difficulty Options -
Here is where you choose how difficult you would like the problem to be. Choices are: 1, 10, 100, 1000.
"""
one_button = tk.Button(root, text="Max Value: 9", width = 15, command=lambda mv="one": start_problems(mv))
one_button.grid_forget()

ten_button = tk.Button(root, text="Max Value: 99", width = 15, command=lambda mv="ten": start_problems(mv))
ten_button.grid_forget()

hund_button = tk.Button(root, text="Max Value: 999", width = 15, command=lambda mv="hund": start_problems(mv))
hund_button.grid_forget()

thou_button = tk.Button(root, text="Max Value: 9999", width = 15, command=lambda mv="thou": start_problems(mv))
thou_button.grid_forget()


# First label
num_1_label = tk.Label(root, textvariable = num_a)
num_1_label.grid_forget()

# Math Symbol
symbol_1_label = tk.Label(root, textvariable = math_symbol)
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
check_button = tk.Button(root, text="Check Answer", command=lambda: check_answer())
check_button.grid_forget()

# Another Problem? Button
another_button = tk.Button(root, text="Another Problem?", command=lambda: gen_problem(diff_val))
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


def check_answer():
    is_num()
    ans = math_answer()
    if ans == int(answer_entry.get()):
        status_bar_var.set(f"This was correct. \n Would you like to do another problem?")
        check_button.grid_forget()
        another_button.grid(row=3, column=1, columnspan=5, sticky="we", pady=10)
    else:
        status_bar_var.set(f"This was incorrect, try again!")
        answer_entry.delete(0, "end")
        quit_button.grid_forget()
        give_up.grid(row=4, column=1, columnspan=5, sticky="we", padx=5, pady=5)

def math_answer():
    math_answers = {"add": op.add(num_a.get(), num_b.get()),
                    "sub": op.sub(num_a.get(), num_b.get())}
    for key in math_answers:
        if key == math_type:
            return math_answers[key]

def is_num():
    try:
        int(answer_entry.get())
    except ValueError:
        status_bar_var.set(f"This was not a number! Try again!")
        answer_entry.delete(0, "end")


def delete_status():
    answer_entry.delete(0, "end")
    status_bar_var.set("")


def difficulty_choice(m):
    one_button.grid(row=1, column=1, padx=10, pady=10)
    ten_button.grid(row=1, column=2, padx=10, pady=10)
    hund_button.grid(row=2, column=1, padx=10, pady=10)
    thou_button.grid(row=2, column=2, padx=10, pady=10)
    turn_off_math_type()
    set_math_type(m)

def set_math_type(m):
    global math_type
    if m == "add":
        math_type = m
    elif m == "sub":
        math_type = m
    elif m == "multi":
        math_type = m
    elif m == "div":
        math_type = m
    print(math_type)

def set_math_dif(mv):
    global diff_val
    if mv == "one":
        diff_val = 10
    elif mv == "ten":
        diff_val = 100
    elif mv == "hund":
        diff_val = 1000
    elif mv == "thou":
        diff_val = 10000

def start_problems(mv):
    set_math_dif(mv)
    if math_type == "add":
        math_choice(diff_val)
        turn_off_diff_opt()
    elif math_type == "sub":
        turn_off_diff_opt()
        math_choice(diff_val)

def gen_problem(diff_val):
    if math_type == "sub":
        set_a_max()
    else:
        num_a.set(gen_ran_num(diff_val))
        num_b.set(gen_ran_num(diff_val))
    another_button.grid_forget()
    delete_status()
    turn_on_prob()

def set_a_max():
    a = gen_ran_num(diff_val)
    b = gen_ran_num(diff_val)
    if a >= b:
        num_a.set(a)
        num_b.set(b)
    else:
        num_a.set(b)
        num_b.set(a)

def math_choice(diff_val):
    gen_problem(diff_val)
    turn_on_prob()

def turn_on_prob():
    set_math_sym()
    num_1_label.grid(row=1, column=1)
    symbol_1_label.grid(row=1, column=2)
    num_2_label.grid(row=1, column=3)
    equal_label.grid(row=1, column=4)
    answer_entry.grid(row=1, column=5)
    check_button.grid(row=2, column=1, columnspan=5, sticky="we", pady=10)
    quit_button.grid(row=4, column=1, columnspan=5, sticky="we", padx=5, pady=5)
    status_bar_label.grid(row=100, column=1, columnspan=5, ipadx=5, ipady=5)


def set_math_sym():
    global math_symbol
    math_types = {"add": " + ", "sub": " - "}
    for key in math_types.keys():
        if key == math_type:
            math_symbol.set(math_types[key])


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
    answer = math_answer()
    status_bar_var.set(f"The correct answer was: {answer}")
    check_button.grid_forget()
    another_button.grid(row=3, column=1, columnspan=5, sticky="we", pady=10)
    give_up.grid_forget()
    quit_button.grid(row=4, column=1, columnspan=5, sticky="we", padx=5, pady=5)

def not_active(m):
    # for testing purposes only
    status_bar_label.grid(row=100, column=1, columnspan=5, ipadx=5, ipady=5)
    set_math_type(m)
    status_bar_var.set(f"This is not active yet!! Sorry!")

# Final Line
root.mainloop()
