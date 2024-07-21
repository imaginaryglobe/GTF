import tkinter as tk
import random
import os
import json

with open("reversed_countries.json") as file:
    data = json.load(file)
    COUNTRY_LIST = [country[0] for country in data]

def choose_flag():
    file_name = random.choice(os.listdir("images/"))
    flag_name = file_name
    return f"images/{flag_name}"
    
def show_flag():
    print("click")
    flag_path = choose_flag()
    flag_picture = tk.PhotoImage(file=flag_path)
    flag_label.config(image=flag_picture)
    flag_label.image = flag_picture

window = tk.Tk()
window.maxsize(400, 400)
window.minsize(400, 400)
window.geometry("400x400+1000+200")

top_text = tk.Label(window, text="Guess the flag")
top_text.pack(pady=10)  



flag_picture = tk.PhotoImage(file=choose_flag())
flag_label = tk.Label(window, image=flag_picture)
flag_label.pack(pady=10)

b2=tk.Button(window,text="Next",command=show_flag)
b2.pack()

window.mainloop()