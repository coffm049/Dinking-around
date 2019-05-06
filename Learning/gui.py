from tkinter import *

window = Tk()
window.title("Welcome to LikeGeeks app")

lbl = Label(window, text="Hello", font=("Arial Bold", 25))
lbl.grid(column=0, row=0)

def clicked():
    res = "Welcome to " + txt.get()
    lbl.configure(text=res)

btn = Button(window, text='Click Me', bg='white', fg='black', command=clicked)
btn.grid(column=1, row=0)

txt = Entry(window, width = 10)
txt.grid(column=0, row = 1)

window.geometry('350x200')
window.mainloop()

