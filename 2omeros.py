import numpy as np
import matplotlib.pyplot as plt

def binary_se_gray(binary, M):
    # metatropi se grey
    binary = int(binary, 2)
    binary ^= (binary >> 1)
    gray_code = format(binary, '08b')
    
    # ypologismos tou apetoumenou mikous
    required_length = int(np.log2(M))

    # prosthiki midenikon an xreiastei
    while len(gray_code) < required_length:
        gray_code = '0' + gray_code

    return gray_code


def gray_se_ppm(gray_codes, M):
    # Metatropi kodikon Gray se theseis PPM
    ppm_theseis = []
    for gray_code in gray_codes:
        gray_value = int(gray_code, 2)
        ppm_thesi = gray_value % M
        ppm_theseis.append(ppm_thesi)
    return ppm_theseis

def sxediasidiagrammatos(name, M, ppm_positions, Ts=1e-6):
    # Sxediasmos kyvatomorfon PPM
    pulse_diarkia = Ts / M
    synolikos_xronos = Ts * len(ppm_positions)
    t = np.linspace(0, synolikos_xronos, int(1e5))
    ppm_signal = np.zeros_like(t)

    for i, thesi in enumerate(ppm_positions):
        arxiki_xroniki_stigmi = i * Ts + thesi * pulse_diarkia
        teliki_xroniki_stigmi = arxiki_xroniki_stigmi + pulse_diarkia
        ppm_signal[(t >= arxiki_xroniki_stigmi) & (t < teliki_xroniki_stigmi)] = 1

    plt.figure(figsize=(15, 4))
    plt.plot(t, ppm_signal)
    plt.title(f"PPM Waveform gia M={M}")
    plt.xlabel("Xronos (s)")
    plt.ylabel("Signal")
    plt.grid(True)
    plt.show()

onoma = "Pavlos Papadakis"
dyadiko_onoma = ' '.join(format(ord(char), '08b') for char in onoma)
gray_code_kommatia_m2 = [binary_se_gray(chunk, 2) for chunk in dyadiko_onoma.split()]
gray_code_kommatia_m4 = [binary_se_gray(chunk, 4) for chunk in dyadiko_onoma.split()]
gray_code_kommatia_m8 = [binary_se_gray(chunk, 8) for chunk in dyadiko_onoma.split()]
gray_code_kommatia_m16 = [binary_se_gray(chunk, 16) for chunk in dyadiko_onoma.split()]

# Metatropi se diafores times M
ppm_m2 = gray_se_ppm(gray_code_kommatia_m2, 2)
ppm_m4 = gray_se_ppm(gray_code_kommatia_m4, 4)
ppm_m8 = gray_se_ppm(gray_code_kommatia_m8, 8)
ppm_m16 = gray_se_ppm(gray_code_kommatia_m16, 16)

# Sxediasmos gia kathe timi M
sxediasidiagrammatos(onoma, 2, ppm_m2)
sxediasidiagrammatos(onoma, 4, ppm_m4)
sxediasidiagrammatos(onoma, 8, ppm_m8)
sxediasidiagrammatos(onoma, 16, ppm_m16)
