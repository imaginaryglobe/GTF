import tkinter as tk
import random
import json
from PIL import Image, ImageTk
import time

COUNTRY_ABBS = ["BD", "BE", "BF", "BG", "BA", "BB", "BN", "BO", "BH", "BI", "BJ", "BT", "JM", "BW", "WS", "BR", "BS", "BY", "BZ", "RU", "RW", "RS", "TL", "TM", "TJ", "RO", "GW", "GT", "GR", "GQ", "JP", "GY", "GE", "GD", "GB", "GA", "SV", "GN", "GM", "GH", "OM", "TN", "JO", "HR", "HT", "HU", "HN", "VE", "PW", "PT", "PY", "IQ", "PA", "PG", "PE", "PK", "PH", "PL", "ZM", "EE", "EG", "ZA", "EC", "IT", "VN", "SB", "ET", "SO", "ZW", "SA", "ES", "ER", "ME", "MD", "MG", "MA", "MC", "UZ", "MM", "ML", "MN", "MH", "MK", "MU", "MT", "MW", "MV", "UG", "TZ", "MY", "MX", "IL", "FR", "FI", "FJ", "NI", "NL", "NO", "NA", "VU", "NE", "NG", "NZ", "NP", "NR", "CI", "CH", "CO", "CN", "CM", "CL", "CA", "CG", "CF", "CD", "CZ", "CY", "CR", "CV", "CU", "SZ", "SY", "KG", "KE", "SS", "SR", "KI", "KH", "KN", "KM", "ST", "SK", "KR", "SI", "KP", "KW", "SN", "SM", "SL", "SC", "KZ", "SG", "SE", "SD", "DO", "DM", "DJ", "DK", "DE", "YE", "DZ", "US", "UY", "LB", "LC", "LA", "TV", "TW", "TT", "TR", "LK", "LI", "LV", "TO", "LT", "LU", "LR", "LS", "TH", "TG", "TD", "LY", "VA", "VC", "AE", "AD", "AG", "AF", "IS", "IR", "AM", "AL", "AO", "IN", "AZ", "IE", "ID", "UA", "QA", "MZ"]

TERRITORY_ABBS = ["AQ", "AS", "AW", "AX", "BL", "BM", "BQ", "BV", "CK", "CX", "CW", "EH", "FK", "FM", "FO", "GI", "GL", "GP", "GS", "GU", "HK", "IM", "IO", "JE", "KY", "MO", "MP", "MS", "NC", "NF", "NU", "PF", "PM", "PN", "PR", "PS", "RE", "SH", "SJ", "SX", "TC", "TF", "TK", "UM", "VG", "VI", "WF", "YT"]



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
    COUNTRY_NAMES = list(data.values())

def choose_flag():
    file_name = random.choice(COUNTRY_LIST)
    return f"images/{file_name}"

def show_flag():
    flag_path = choose_flag()
    flag_picture = ImageTk.PhotoImage(Image.open(flag_path))
    flag_label.config(image=flag_picture)
    flag_label.image = flag_picture
    show_cities(flag_path)

    
def show_cities(flag_path):
    lb_of_cities.delete(0, tk.END)
    global correct_position
    correct_position = random.randint(0, 3)
    for i in range(4):
        if i == correct_position:
            city = flag_path[7:9]
            print(data[city.upper()])  # TO SHOW ANSWERS
            lb_of_cities.insert(i, data[city.upper()])
        else:
            city = random.choice(COUNTRY_NAMES)
            lb_of_cities.insert("end", city)

def check_correct():
    selected = lb_of_cities.curselection()
    if selected:
        if selected[0] == correct_position:
            window.config(bg="#00FF00")
            window.after(500, lambda: window.config(bg=bgcolor))
            show_flag()
        else:
            window.config(bg="#FF0000")
            window.after(500, lambda: window.config(bg=bgcolor))
            show_flag()
      
    
window = tk.Tk()
bgcolor = window.cget("bg")
window.maxsize(400, 400)
window.minsize(400, 400)
center_window(window)


top_text = tk.Label(window, text="Guess the flag", bd=0)
top_text.pack(pady=10)  

territories_cb = tk.Checkbutton(window, text="Include territories", variable=tk.IntVar())
territories_cb.pack(side="top", anchor="ne")

first_flag = choose_flag()
flag_picture = ImageTk.PhotoImage(Image.open(first_flag))
flag_label = tk.Label(window, image=flag_picture)
flag_label.pack(pady=10)



lb_of_cities = tk.Listbox(window, selectmode="SINGLE", width = 36, justify="center")
lb_of_cities.config(font=("Times New Roman", 18))
lb_of_cities.pack(pady=10)

b2=tk.Button(window,text="Submit",command=check_correct, width=10, height=2, bd=0)
b2.pack()

show_cities(first_flag)
window.mainloop()