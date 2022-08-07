import numpy as np

import hzDefinition as hzDef
import allHz as allHz
import hzRounding as hzRound

#Frecuencias de Fa, Fa# y Sol

hzType1 = np.array([], dtype=float)
for i in range(3):                                                          #Tomo las notas Fa, Fa# y Sol
    for j in range(9):                                                      
        nextHz = hzDef.vInitialHz[i] * (2 ** j)                            #Multiplico por 2 para que sean las notas de la octava superior
        hzType1 = np.append(hzType1, allHz.hzAutoStorage(nextHz))
        hzType1 = hzRound.autoRounding(hzType1)

#Frecuencias de Sol#, La, La#, Si, Do, Do#, Re, Re#, Mi

hzType2 = np.array([], dtype=float)
for i in range(3, 12):
    for j in range(8):
        nextHz = hzDef.vInitialHz[i] * (2 ** j)
        hzType2 = np.append(hzType2, allHz.hzAutoStorage(nextHz))
        hzType2 = hzRound.autoRounding(hzType2)


