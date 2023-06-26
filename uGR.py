"""
Unterschiede von Mittelwert und Population
"""

import matplotlib.pyplot as plt
import random

plt.ion()
fig, ax = plt.subplots()
line1, = ax.plot([], [])
line2, = ax.plot([], [])
ax.legend(['2^i', 'Population'])
plt.show(block=False)
y1 = []
y2 = []
x1 = []
x = 0
pop = 1

for i in range(18):
    x = i
    for x in range(pop):
        pop += random.randint(0, 2)

    y1.append(2**i)
    y2.append(pop)
    x1.append(i)

    line1.set_data(x1, y1)
    line2.set_data(x1, y2)

    ax.relim()
    ax.autoscale_view()
    fig.canvas.draw()
    plt.pause(0.01)

print(pop)
print(f'Enddifferenz: {pop-2**i}')
input('Exit?')