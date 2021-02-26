import numpy as np

def getVar(N):
    length = len(N)
    res = [0] * length
    for i in range(length):
        res[i] = np.var(N)
    return res