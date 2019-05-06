import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0, 4, 100)
y = 2 ** x

# You probably won't need this if you're embedding things in a tkinter plot...
plt.ion()

fig = plt.figure()
ax = fig.add_subplot(111)

line1, = ax.plot(x, y, 'r-') # Returns a tuple of line objects, thus the comma

for number in np.linspace(0, 10, 50):
    line1.set_ydata((x) + number)
    fig.canvas.draw()
    fig.canvas.flush_events()
