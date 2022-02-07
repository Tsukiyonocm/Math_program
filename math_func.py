# Generate Random Numbers for Addition Problems
import random
import tkinter as tk

def gen_ran_num():
    global num_a
    global num_b
    num_a = random.randint(0, 10)
    num_b = random.randint(0, 10)
    print(num_a, num_b)
    return (num_a, num_b)

# def check_answer():
