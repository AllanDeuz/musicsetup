
import numpy as np
import scipy.fftpack as fourier
import matplotlib
import matplotlib.pyplot as plt
import pyaudio as pa
import struct

import hzApproximation as hzAp
import hzType as hzT
import errorRange as eR
import chooseApproximation as cA
import NoteDetection as nD

matplotlib.use('TkAgg')

FRAMES = 1024*10                                  # Tamaño del paquete a procesar
FORMAT = pa.paInt16                               # Formato de lectura INT 16 bits
CHANNELS = 1
Fs = 48000                                        # Frecuencia de muestreo para audio

p = pa.PyAudio()

stream = p.open(                                  # Abrimos el canal de audio con los parámeteros de configuración
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
F = (Fs/FRAMES)*np.arange(0, FRAMES//2)

while True:

    # Leemos paquetes de longitud FRAMES
    data = stream.read(FRAMES)
    # Convertimos los datos que se encuentran empaquetados en bytes
    dataInt = struct.unpack(str(FRAMES) + 'h', data)

    # Asignamos los datos a la curva de la variación temporal
    line.set_ydata(dataInt)

    # Calculamos la FFT y la Magnitud de la FFT del paqute de datos
    M_gk = abs(fourier.fft(dataInt)/FRAMES)

    ax1.set_ylim(0, np.max(M_gk+10))
    # Asigmanos la Magnitud de la FFT a la curva del espectro
    line_fft.set_ydata(M_gk)

    # Tomamos la mitad del espectro para encontrar la Frecuencia Dominante
    M_gk = M_gk[0:FRAMES//2]
    Posm = np.where(M_gk == np.max(M_gk))
    # Encontramos la frecuencia que corresponde con el máximo de M_gk
    maxHz = F[Posm]
    # Redondeamos la frecuencia encontrada a 3 decimales
    maxHz = np.round(maxHz, 3)

    # Calculamos la aproximación de la frecuencia
    hzApproximation = hzAp.approximateHz(hzT.hzType1, maxHz)
    hzApproximation2 = hzAp.approximateHz(hzT.hzType2, maxHz)

    difference = abs(maxHz - hzApproximation)
    difference2 = abs(maxHz - hzApproximation2)
    difference = np.round(difference, 3)
    difference2 = np.round(difference2, 3)

    resp = eR.errorRange(difference)
    resp2 = eR.errorRange(difference2)

    if resp and resp2:

        # Elegimos la aproximación que se va a usar, criterio: la menor se escoge, si d < d2 -> True, si d > d2 -> False, si d = d2 -> True

        chosenHzApproximation = cA.chooseApproximation(difference, difference2)
        if chosenHzApproximation:
            nD.determineMusicalNote(hzApproximation)
        elif not chosenHzApproximation:
            nD.determineMusicalNote2(hzApproximation2)
        else:
            print("maxHz")
    elif resp and not resp2:
        nD.determineMusicalNote(hzApproximation)
    elif not resp and resp2:
        nD.determineMusicalNote2(hzApproximation2)
    else:
        print("maxHz")

    fig.canvas.draw()
    fig.canvas.flush_events()
