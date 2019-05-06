from tkinter import *
from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg, NavigationToolbar2Tk)
from matplotlib.backend_bases import key_press_handler
from matplotlib.figure import Figure
import numpy as np

window = Tk()
window.title("Calculating CoC ROI")

fig = Figure(figsize=(5, 4), dpi=100)
t = np.arange(0, 3, .01)
fig.add_subplot(111).plot(t, 2* t)

canvas = FigureCanvasTkAgg(fig, master=window)  # A tk.DrawingArea.
canvas.draw()
canvas.get_tk_widget().pack(side=TOP, fill=BOTH, expand=1)

toolbar = NavigationToolbar2Tk(canvas, window)
toolbar.update()
canvas.get_tk_widget().pack(side=TOP, fill=BOTH, expand=1)

Label(window, text = "Intercept").pack(side= TOP)
slope = Entry(window, width =3)
slope.pack(side = TOP)
slope.insert(0, "0")

Label(window , text = "Intercept").pack(side = TOP)
intercept = Entry(window, width=3)
intercept.pack(side = TOP)
intercept.insert(0, "0")

def change_graph() :
    Slope = float(slope.get())
    Intercept = float(intercept.get())
    fig = Figure(figsize=(5, 4), dpi=100)
    t = np.arange(0, 3, .01)
    line = Slope * t + Intercept
    ax.set_xlimit(t.min(), t.max())
    ax.set_ylimit(line.min(), line.max())
    fig.add_subplot(111).plot(t, line)

    canvas = FigureCanvasTkAgg(fig, master=window)  # A tk.DrawingArea.
    canvas.draw()
    canvas.get_tk_widget().pack(side=TOP, fill=BOTH, expand=1)
    toolbar = NavigationToolbar2Tk(canvas, window)
    toolbar.update()
    canvas.get_tk_widget().pack(side=TOP, fill=BOTH, expand=1)


btn = Button(window, text= "Change graph", command= change_graph).pack(side = TOP)


def on_key_press(event):
    print("you pressed {}".format(event.key))
    key_press_handler(event, canvas, toolbar)


canvas.mpl_connect("key_press_event", on_key_press)


def _quit():
    window.quit()     # stops mainloop
    window.destroy()  # this is necessary on Windows to prevent
                    # Fatal Python Error: PyEval_RestoreThread: NULL tstate


button = Button(master=window, text="Quit", command=_quit)
button.pack(side=BOTTOM)


window.mainloop()

