"""
Erwartungswert vs Simulation
"""

import matplotlib.pyplot as plt
import random


def choose(posi):
    li = []
    for z in posi:
        for wahr in range(posi[z]):
            li.append(z)

    return random.choice(li)


def erwartungswert(posi):
    e = 0
    for z in posi:
        e += (z * (posi[z]/100))

    return e


dic = {1: 50, 2: round(5/22*100), 0: round(6/22*100)}

plt.ion()
fig, ax = plt.subplots()
line1, = ax.plot([], [])
line2, = ax.plot([], [])
ax.legend(['Population', 'Erwartungswert'])
ax.set_xlabel('Iterations')
ax.set_ylabel('Population Size')

plt.show(block=False)
y1 = []
y2 = []
x1 = []

print(erwartungswert(dic))
start = 100
pop = 100

it = int(input('Wieviele Wdhs: '))

for i in range(it):
    n = 0
    start = erwartungswert(dic)*start + start
    y1.append(start)

    for x in range(pop):
        n += choose(dic)

    pop += n
    y2.append(pop)

    x1.append(i)

    line1.set_data(x1, y1)
    line2.set_data(x1, y2)

    ax.relim()
    ax.autoscale_view()
    fig.canvas.draw()
    plt.pause(0.01)


print(pop - start)
input('exit?')