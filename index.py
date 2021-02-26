import matplotlib
import matplotlib.pyplot as plt
import numpy as np
import rsg
import additionalTask as at

n = 12
W = 2400
N = 1024
time = range(N)
signal = rsg.getRandomSignal(n, W, N)

print("Expected value", np.mean(signal))
print("Variance", np.std(signal))

fig, (ax1, ax2) = plt.subplots(2, 1)
ax1.plot(time, signal)
ax1.set(xlabel='time', ylabel='signal(t)',
       title='Random signal')

newN = range(0, N)
varianceN = at.getVar(newN)

ax2.plot(newN, varianceN)
ax2.set(xlabel='N', ylabel='Variance(N)', title='Variance versus N')

fig.savefig("lab1.png")

plt.show()

