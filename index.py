import matplotlib
import matplotlib.pyplot as plt
import numpy as np
import rsg

n = 12
W = 2400
N = 1024
time = range(N)
signal = rsg.getRandomSignal(n, W, N)

fig, ax1 = plt.subplots()
ax1.plot(time, signal)
ax1.set(xlabel='time', ylabel='signal(t)',
       title='Random signal')
fig.savefig("signal.png")
plt.show()