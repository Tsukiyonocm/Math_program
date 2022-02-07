import tkinter as tk
import random

# First Line
root = tk.Tk()
root.geometry("800x600")

# Generate Random Numbers
def gen_ran_num():
    rand_num = random.randint(0,10)
    return rand_num

# Random Numbers to be used in problems
num_a = tk.IntVar()
num_b = tk.IntVar()
num_a.set(gen_ran_num())
num_b.set(gen_ran_num())

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
check_button = tk.Button(root, text="Check Answer", command=lambda: check_answer_add(answer_entry))
check_button.grid(row=2, column=1, columnspan=5, sticky="we", pady=10)

# Status Bar
status_bar_var = tk.StringVar()
status_bar_label = tk.Label(root, textvariable=status_bar_var)
status_bar_label.grid(row=100, column=1, columnspan=5, ipadx=5, ipady=5)

def check_answer_add(answer_entry):
    # print(num_a.get())
    if num_a.get() + num_b.get() == int(answer_entry.get()):
        status_bar_var.set(f"This was correct.")
        check_button.grid_forget()
    else:
        status_bar_var.set(f"This was incorrect, try again!")
    print(answer_entry.get())

gen_ran_num()
# Final Line
root.mainloop()
