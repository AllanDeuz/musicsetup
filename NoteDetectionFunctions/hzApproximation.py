import numpy as np

def approximateHz (hzType, maxHz):
    hzApproximation = hzType.flat[np.abs(hzType - maxHz).argmin()]
    hzApproximation = np.round(hzApproximation, 3)
    return hzApproximation