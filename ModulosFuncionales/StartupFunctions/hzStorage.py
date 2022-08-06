import numpy as np

import hzExpansion as hzExp

def vPrevious(Hz):
    valuesPrevious = np.array([], dtype=float)
    valuesPrevious = np.append(valuesPrevious, hzExp.nPrevious(Hz))
    valuesPrevious = np.append(valuesPrevious, Hz)                                  # Add the original value
    return valuesPrevious

def vSubsequent(Hz):
    valuesSubsequent = np.array([], dtype=float)
    valuesSubsequent = np.append(valuesSubsequent, hzExp.nSubsequent(Hz))
    return valuesSubsequent