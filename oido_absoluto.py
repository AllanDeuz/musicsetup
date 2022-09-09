import numpy as np
import scipy.fftpack as fourier
import matplotlib
import matplotlib.pyplot as plt
import scipy.io.wavfile as waves
import pyaudio as pa
import struct
import statsmodels.api as sm
from scipy.signal import find_peaks


def main():
    initialHzFa = 21.826
    initialHzFaS = 23.125
    initialHzSol = 24.50
    initialHzSolS = 25.96
    initialHzLa = 27.50
    initialHzLaS = 29.14
    initialHzSi = 30.87
    initialHzDo = 32.7
    initialHzDoS = 34.65
    initialHzRe = 36.71
    initialHzReS = 38.89
    initialHzMi = 41.2

    vInitialHz = np.array([
        initialHzFa,
        initialHzFaS,
        initialHzSol,
        initialHzSolS,
        initialHzLa,
        initialHzLaS,
        initialHzSi,
        initialHzDo,
        initialHzDoS,
        initialHzRe,
        initialHzReS,
        initialHzMi
    ], dtype=float)

    def vHzValues(Hz):
        Hzvalues = np.array([], dtype=float)
        Hzvalues = np.append(Hzvalues, Hz)
        return Hzvalues

    def autoRounding(Hz):
        hzRound = np.array([], dtype=float)
        for i in range(len(Hz)):
            hzRound = np.append(hzRound, round(Hz[i], 3))
        return hzRound

    def hzAutoStorage(Hz):
        allHz = np.array([], dtype=float)
        allHz = np.append(allHz, vHzValues(Hz))
        #allHz = np.append(allHz, vSubsequent(Hz))
        return allHz

    # Frecuencias de Fa, Fa# y Sol

    hzType1 = np.array([], dtype=float)
    for i in range(3):
        for j in range(9):
            # Multiplico por 2 para que sean las notas de la octava superior
            nextHz = vInitialHz[i] * (2 ** j)
            hzType1 = np.append(hzType1, hzAutoStorage(nextHz))
            hzType1 = autoRounding(hzType1)

    # Frecuencias de Sol#, La, La#, Si, Do, Do#, Re, Re#, Mi

    hzType2 = np.array([], dtype=float)
    for i in range(3, 12):
        for j in range(8):
            nextHz = vInitialHz[i] * (2 ** j)
            hzType2 = np.append(hzType2, hzAutoStorage(nextHz))
            hzType2 = autoRounding(hzType2)

    # Ingreso de las frecuencias en los array de las notas Fa, Fa# y Sol
    # 9 valores en total para cada nota.

    total = 9

    FaHz = np.array([], dtype=float)
    for i in range(total):
        FaHz = np.append(FaHz, hzType1[i])

    FaSHz = np.array([], dtype=float)
    for i in range(total, total * 2):
        FaSHz = np.append(FaSHz, hzType1[i])

    SolHz = np.array([], dtype=float)
    for i in range(total * 2, total * 3):
        SolHz = np.append(SolHz, hzType1[i])

    cluster1 = np.array([FaHz, FaSHz, SolHz], dtype=float)

    # Ingreso de las frecuencias en los array de las notas Sol#, La, La#, Si, Do, Do#, Re, Re# y Mi
    # 8 valores en total para cada nota.

    total = 8

    SolSHz = np.array([], dtype=float)
    for i in range(total):
        SolSHz = np.append(SolSHz, hzType2[i])

    LaHz = np.array([], dtype=float)
    for i in range(total, total * 2):
        LaHz = np.append(LaHz, hzType2[i])

    LaSHz = np.array([], dtype=float)
    for i in range(total * 2, total * 3):
        LaSHz = np.append(LaSHz, hzType2[i])

    SiHz = np.array([], dtype=float)
    for i in range(total * 3, total * 4):
        SiHz = np.append(SiHz, hzType2[i])

    DoHz = np.array([], dtype=float)
    for i in range(total * 4, total * 5):
        DoHz = np.append(DoHz, hzType2[i])

    DoSHz = np.array([], dtype=float)
    for i in range(total * 5, total * 6):
        DoSHz = np.append(DoSHz, hzType2[i])

    ReHz = np.array([], dtype=float)
    for i in range(total * 6, total * 7):
        ReHz = np.append(ReHz, hzType2[i])

    ReSHz = np.array([], dtype=float)
    for i in range(total * 7, total * 8):
        ReSHz = np.append(ReSHz, hzType2[i])

    MiHz = np.array([], dtype=float)
    for i in range(total * 8, total * 9):
        MiHz = np.append(MiHz, hzType2[i])

    cluster2 = np.array([SolSHz, LaHz, LaSHz, SiHz, DoHz,
                        DoSHz, ReHz, ReSHz, MiHz], dtype=float)

    # FUNCIONES PARA DETERMINAR NOTA MUSICAL vvv

    def chooseApproximation(difference, difference2):
        if difference < difference2:
            return True
        elif difference > difference2:
            return False
        else:
            return True

    def errorRange(difference):
        if 0 <= difference < 5:
            return True
        else:
            return False

    def approximateHz(hzType, maxHz):
        hzApproximation = hzType.flat[np.abs(hzType - maxHz).argmin()]
        hzApproximation = np.round(hzApproximation, 3)
        return hzApproximation

    def determineMusicalNote(maxHz):
        hzPosition = np.where(hzType1 == maxHz)[0][0]
        if maxHz in cluster1[0]:
            print("Es un Fa en: ", hzType1[hzPosition], "Hz")
        elif maxHz in cluster1[1]:
            print("Es un Fa# en: ", hzType1[hzPosition], "Hz")
        elif maxHz in cluster1[2]:
            print("Es un Sol en: ", hzType1[hzPosition], "Hz")
        else:
            return 0

    def determineMusicalNote2(maxHz):
        hzPosition = np.where(hzType2 == maxHz)[0][0]
        if maxHz in cluster2[0]:
            print("Es un Sol# en: ", hzType2[hzPosition], "Hz")
        elif maxHz in cluster2[1]:
            print("Es un La en: ", hzType2[hzPosition], "Hz")
        elif maxHz in cluster2[2]:
            print("Es un La# en: ", hzType2[hzPosition], "Hz")
        elif maxHz in cluster2[3]:
            print("Es un Si en: ", hzType2[hzPosition], "Hz")
        elif maxHz in cluster2[4]:
            print("Es un Do en: ", hzType2[hzPosition], "Hz")
        elif maxHz in cluster2[5]:
            print("Es un Do# en: ", hzType2[hzPosition], "Hz")
        elif maxHz in cluster2[6]:
            print("Es un Re en: ", hzType2[hzPosition], "Hz")
        elif maxHz in cluster2[7]:
            print("Es un Re# en: ", hzType2[hzPosition], "Hz")
        elif maxHz in cluster2[8]:
            print("Es un Mi en: ", hzType2[hzPosition], "Hz")
        else:
            return 0

    matplotlib.use('TkAgg')

    FRAMES = 1024 * 10  # Tamaño del paquete a procesar
    FORMAT = pa.paInt16  # Formato de lectura INT 16 bits
    CHANNELS = 1
    Fs = 48000  # Frecuencia de muestreo para audio

    p = pa.PyAudio()

    stream = p.open(  # Abrimos el canal de audio con los parámeteros de configuración
        format=FORMAT,
        channels=CHANNELS,
        rate=Fs,
        input=True,
        output=True,
        frames_per_buffer=FRAMES
    )

    # Creamos una gráfica con 2 subplots y configuramos los ejes

    fig, (ax, ax1) = plt.subplots(2)
    x_audio = np.arange(0, FRAMES, 1)
    x_fft = np.linspace(0, Fs, FRAMES)
    line, = ax.plot(x_audio, np.random.rand(FRAMES), 'r')
    line_fft, = ax1.semilogx(x_fft, np.random.rand(FRAMES), 'b')
    ax.set_ylim(-32500, 32500)
    ax.ser_xlim = (0, FRAMES)
    Fmin = 1
    Fmax = 5000
    ax1.set_xlim(Fmin, Fmax)
    fig.show()

    # Creamos el vector de frecuencia para encontrar la frecuencia dominante
    F = (Fs / FRAMES) * np.arange(0, FRAMES // 2)

    while True:

        data = stream.read(FRAMES)  # Leemos paquetes de longitud FRAMES
        # Convertimos los datos que se encuentran empaquetados en bytes
        dataInt = struct.unpack(str(FRAMES) + 'h', data)

        # Asignamos los datos a la curva de la variación temporal
        line.set_ydata(dataInt)

        # Calculamos la FFT y la Magnitud de la FFT del paqute de datos
        M_gk = abs(fourier.fft(dataInt) / FRAMES)

        ax1.set_ylim(0, np.max(M_gk + 10))
        # Asigmanos la Magnitud de la FFT a la curva del espectro
        line_fft.set_ydata(M_gk)

        # Tomamos la mitad del espectro para encontrar la Frecuencia Dominante
        M_gk = M_gk[0:FRAMES // 2]
        Posm = np.where(M_gk == np.max(M_gk))
        # Encontramos la frecuencia que corresponde con el máximo de M_gk
        maxHz = F[Posm]
        # Redondeamos la frecuencia encontrada a 3 decimales
        maxHz = np.round(maxHz, 3)

        # Calculamos la aproximación de la frecuencia
        hzApproximation = approximateHz(hzType1, maxHz)
        hzApproximation2 = approximateHz(hzType2, maxHz)

        difference = abs(maxHz - hzApproximation)
        difference2 = abs(maxHz - hzApproximation2)
        difference = np.round(difference, 3)
        difference2 = np.round(difference2, 3)

        resp = errorRange(difference)
        resp2 = errorRange(difference2)

        if resp and resp2:
            # Elegimos la aproximación que se va a usar, criterio:
            # la menor se escoge, si d < d2 -> True, si d > d2 -> False, si d = d2 -> True
            chosenHzApproximation = chooseApproximation(
                difference, difference2)
            if chosenHzApproximation:
                determineMusicalNote(hzApproximation)
            else:
                determineMusicalNote2(hzApproximation2)
        elif resp and not resp2:
            determineMusicalNote(hzApproximation)
        elif not resp and resp2:
            determineMusicalNote2(hzApproximation2)
        else:
            print("No estas afinado")

        fig.canvas.draw()
        fig.canvas.flush_events()


if __name__ == '__main__':
    main()
