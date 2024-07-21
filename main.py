import tkinter as tk
import random
import json
from PIL import Image, ImageTk

def center_window(window):
    window.update_idletasks()
    width = window.winfo_width()
    height = window.winfo_height()
    screen_width = window.winfo_screenwidth()
    screen_height = window.winfo_screenheight()
    x = (screen_width - width) // 2
    y = (screen_height - height) // 2
    window.geometry(f"{width}x{height}+{x}+{y}")
    
with open("reversed_countries.json") as file:
    data = json.load(file)
    COUNTRY_LIST = [country.lower() + ".png" for country in data]

def choose_flag():
    file_name = random.choice(COUNTRY_LIST)
    return f"images/{file_name}"

def show_flag():
    flag_path = choose_flag()
    flag_picture = ImageTk.PhotoImage(Image.open(flag_path))
    flag_label.config(image=flag_picture)
    flag_label.image = flag_picture

window = tk.Tk()
window.maxsize(400, 400)
window.minsize(400, 400)
center_window(window)


top_text = tk.Label(window, text="Guess the flag")
top_text.pack(pady=10)  



flag_picture = ImageTk.PhotoImage(Image.open(choose_flag()))
flag_label = tk.Label(window, image=flag_picture)
flag_label.pack(pady=10)

b2=tk.Button(window,text="Next",command=show_flag, width=10, height=2)
b2.pack()

window.mainloop()