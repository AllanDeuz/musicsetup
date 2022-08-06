import numpy as np

from hzType import hzType1, hzType2

#Ingreso de las frecuencias en los array de las notas Fa, Fa#, Sol
# 99 valores en total para cada nota.

def cluster1():

    total = 99

    FaHz = np.array([], dtype=float)
    for i in range(total):
        FaHz = np.append(FaHz, hzType1[i])

    FaSHz = np.array([], dtype=float)
    for i in range(total, total*2):
        FaSHz = np.append(FaSHz, hzType1[i])

    SolHz = np.array([], dtype=float)
    for i in range(total*2, total*3):
        SolHz = np.append(SolHz, hzType1[i])

    cluster1 = np.array([FaHz, FaSHz, SolHz], dtype=float)
    return cluster1


#Ingreso de las frecuencias en los array de las notas Sol#, La, La#, Si, Do, Do#, Re, Re#, Mi
# 88 valores en total para cada nota.

def cluster2():

    total = 88

    SolSHz = np.array([], dtype=float)
    for i in range(total):
        SolSHz = np.append(SolSHz, hzType2[i])

    LaHz = np.array([], dtype=float)
    for i in range(total, total*2):
        LaHz = np.append(LaHz, hzType2[i])

    LaSHz = np.array([], dtype=float)
    for i in range(total*2, total*3):
        LaSHz = np.append(LaSHz, hzType2[i])

    SiHz = np.array([], dtype=float)
    for i in range(total*3, total*4):
        SiHz = np.append(SiHz, hzType2[i])

    DoHz = np.array([], dtype=float)
    for i in range(total*4, total*5):
        DoHz = np.append(DoHz, hzType2[i])

    DoSHz = np.array([], dtype=float)
    for i in range(total*5, total*6):
        DoSHz = np.append(DoSHz, hzType2[i])

    ReHz = np.array([], dtype=float)
    for i in range(total*6, total*7):
        ReHz = np.append(ReHz, hzType2[i])

    ReSHz = np.array([], dtype=float)
    for i in range(total*7, total*8):
        ReSHz = np.append(ReSHz, hzType2[i])

    MiHz = np.array([], dtype=float)
    for i in range(total*8, total*9):
        MiHz = np.append(MiHz, hzType2[i])

    cluster2 = np.array([SolSHz, LaHz, LaSHz, SiHz, DoHz, DoSHz, ReHz, ReSHz, MiHz], dtype=float)
    return cluster2