import tkinter as tk
import random
import math_func as mf

# First Line
root = tk.Tk()
root.geometry("800x600")

num_a = mf.gen_ran_num()
num_b = mf.gen_ran_num()

num_1_label = tk.Label(root, text=str(num_a))
num_1_label.grid(row=1, column=1)

symbol_1_label = tk.Label(root, text=" + ")
symbol_1_label.grid(row=1, column=2)

num_2_label = tk.Label(root, text=str(num_b))
num_2_label.grid(row=1, column=3)

equal_label = tk.Label(root, text=" = ")
equal_label.grid(row=1, column=4)

answer_entry = tk.Entry(root)
answer_entry.grid(row=1, column=5)

check_button = tk.Button(root, text="Check Answer")
check_button.grid(row=2, column=1, columnspan=5, sticky="we", pady=10)

# Final Line
root.mainloop()
