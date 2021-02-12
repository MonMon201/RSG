import matplotlib
import matplotlib.pyplot as plt
import numpy as np
import rsg

n = 14
W = 2500
N = 64
time = range(N)
signal = rsg.getRandomSignal(n, W, N)

print("Expected value", np.mean(signal))
print("Variance", np.std(signal))

fig, ax1 = plt.subplots()
ax1.plot(time, signal)
ax1.set(xlabel='time', ylabel='signal(t)',
       title='Random signal')
fig.savefig("signal.png")
plt.show()