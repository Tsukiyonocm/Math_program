# Generate Random Numbers for Addition Problems
import random
import tkinter as tk

def gen_ran_num():
    global num_a
    num_return = random.randint(0, 10)
    print(num_return)
    return num_return

# def check_answer():
def check_answer(answer_entry):
    print(answer_entry.get())