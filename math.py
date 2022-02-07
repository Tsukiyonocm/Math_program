import tkinter as tk
import random

# First Line
root = tk.Tk()
root.geometry("800x600")

# Generate Random Numbers
def gen_ran_num():
    rand_num = random.randint(0,20)
    return rand_num

# Random Numbers to be used in problems
num_a = tk.IntVar()
num_b = tk.IntVar()

# First label
num_1_label = tk.Label(root, textvariable = num_a)
num_1_label.grid(row=1, column=1)

# Math Symbol
symbol_1_label = tk.Label(root, text=" + ")
symbol_1_label.grid(row=1, column=2)

# Second Label
num_2_label = tk.Label(root, textvariable = num_b)
num_2_label.grid(row=1, column=3)

# Equal Sign
equal_label = tk.Label(root, text=" = ")
equal_label.grid(row=1, column=4)

# Answer Entry Box
answer_entry = tk.Entry(root)
answer_entry.grid(row=1, column=5)

# Check Answer Button
check_button = tk.Button(root, text="Check Answer", command=lambda: check_answer_add())
check_button.grid(row=2, column=1, columnspan=5, sticky="we", pady=10)

# Another Problem? Button
another_button = tk.Button(root, text="Another Problem?", command=lambda: another_problem())
another_button.grid_forget()

# Status Bar
status_bar_var = tk.StringVar()
status_bar_label = tk.Label(root, textvariable=status_bar_var)
status_bar_label.grid(row=100, column=1, columnspan=5, ipadx=5, ipady=5)


def check_answer_add():
    is_num()
    if num_a.get() + num_b.get() == int(answer_entry.get()):
        status_bar_var.set(f"This was correct. \n Would you like to do another problem?")
        check_button.grid_forget()
        another_button.grid(row=3, column=1, columnspan=5, sticky="we", pady=10)
    else:
        status_bar_var.set(f"This was incorrect, try again!")
        answer_entry.delete(0, "end")
    print(answer_entry.get())


def is_num():
    try:
        int(answer_entry.get())
    except ValueError:
        status_bar_var.set(f"This was not a number! Try again!")


def delete_status():
    answer_entry.delete(0, "end")
    status_bar_var.set("")


def another_problem():
    num_a.set(gen_ran_num())
    num_b.set(gen_ran_num())
    another_button.grid_forget()
    check_button.grid(row=2, column=1, columnspan=5, sticky="we", pady=10)
    delete_status()


another_problem()
# Final Line
root.mainloop()
