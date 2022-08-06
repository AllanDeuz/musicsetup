import numpy as np

def nPrevious(Hz):
    vPrevious = np.array([], dtype=float)
    for i in range(5):
        value = 5/10 - i/10
        vPrevious = np.append(vPrevious, (Hz - value))
    return vPrevious

def nSubsequent(Hz):
    vSubsequent = np.array([], dtype=float)
    for i in range(5):
        value = i/10 + 1/10
        vSubsequent = np.append(vSubsequent, (Hz + value))
    return vSubsequent