import numpy as np

def autoRounding(Hz):
    hzRound = np.array([], dtype=float)
    for i in range(len(Hz)):
        hzRound = np.append(hzRound, round(Hz[i], 3))
    return hzRound