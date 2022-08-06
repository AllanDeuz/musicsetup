import numpy as np
import sys
print(sys.path)
print(dir())
from StartupFunctions.hzClustering import cluster1, cluster2
from StartupFunctions.hzType import hzType1, hzType2

def determineMusicalNote(maxHz):

    hzPosition = np.where(hzType1==maxHz)[0][0]

    if (maxHz in cluster1.FaHz): print( "Es un Fa en: ", hzType1[hzPosition], "Hz")
    elif (maxHz in cluster1.FaSHz): print( "Es un Fa# en: ", hzType1[hzPosition], "Hz")
    elif (maxHz in cluster1.SolHz): print( "Es un Sol en: ", hzType1[hzPosition], "Hz")

def determineMusicalNote2(maxHz):

    hzPosition = np.where(hzType2==maxHz)[0][0]

    if (maxHz in cluster2.SolSHz): print( "Es un Sol# en: ", hzType2[hzPosition], "Hz")
    elif (maxHz in cluster2.LaHz): print( "Es un La en: ", hzType2[hzPosition], "Hz")
    elif (maxHz in cluster2.LaSHz): print( "Es un La# en: ", hzType2[hzPosition], "Hz")
    elif (maxHz in cluster2.SiHz): print( "Es un Si en: ", hzType2[hzPosition], "Hz")
    elif (maxHz in cluster2.DoHz): print( "Es un Do en: ", hzType2[hzPosition], "Hz")
    elif (maxHz in cluster2.DoSHz): print( "Es un Do# en: ", hzType2[hzPosition], "Hz")
    elif (maxHz in cluster2.ReHz): print( "Es un Re en: ", hzType2[hzPosition], "Hz")
    elif (maxHz in cluster2.ReSHz): print( "Es un Re# en: ", hzType2[hzPosition], "Hz")
    elif (maxHz in cluster2.MiHz): print( "Es un Mi en: ", hzType2[hzPosition], "Hz")