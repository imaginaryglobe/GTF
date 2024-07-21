import tkinter as tk


window = tk.Tk()
window.maxsize(400, 400)
window.minsize(400, 400)
window.geometry("400x400+1000+200")

top_text = tk.Label(window, text="Guess the flag")
top_text.place(x = 150, y = 10)

window.mainloop()