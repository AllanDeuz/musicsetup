import numpy as np

import hzStorage as hzStr

def hzAutoStorage(Hz):
    allHz = np.array([], dtype=float)
    allHz = np.append(allHz, hzStr.vPrevious(Hz))
    allHz = np.append(allHz, hzStr.vSubsequent(Hz))

    return allHz