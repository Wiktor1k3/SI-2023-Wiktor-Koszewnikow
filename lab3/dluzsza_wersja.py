import pandas as pd
import matplotlib.pyplot as plt
from math import sqrt
import numpy as np
from matplotlib.animation import FuncAnimation
from celluloid import Camera

df = pd.DataFrame()
df['X'] = [2000, 2002, 2005, 2007, 2010]
df['Y'] = [6.5, 7.0, 7.4, 8.2, 9.0]

def zlicz(kolumna):
    a = []
    for i in range(df['X'].size):
        a.append(df.at[i, kolumna])
    return a

elem_X = zlicz('X')
elem_Y = zlicz('Y')

def srednia(zbior):
    return float(zbior.sum()) / len(zbior)

Mx = srednia(df['X'])
My = srednia(df['Y'])

def odchylenie(zbior, srednia):
    licznik = 0
    for elem in zbior:
        licznik += (elem - srednia) * (elem - srednia)
    return sqrt(licznik / (len(zbior) - 1))

Sx = odchylenie(df['X'], Mx)
Sy = odchylenie(df['Y'], My)

n = len(df['X'])
vr = pd.DataFrame(df[:])
vr['y2'] = df['Y'] * df['Y']
vr['xy'] = df['X'] * df['Y']
vr['x2'] = df['X'] * df['X']
vr['y2'] = df['Y'] * df['Y']
vr.loc['Σ'] = vr.sum()

def wsp_korelacji_pearsona(n, ΣX, ΣY, Σxy, Σx2, Σy2):
    return ( (n * Σxy - ΣX * ΣY) /
             (sqrt((n * Σx2 - ΣX**2) * (n * Σy2 - ΣY**2))) )

r = wsp_korelacji_pearsona(n, vr['X']['Σ'], vr['Y']['Σ'], vr['xy']['Σ'], vr['x2']['Σ'], vr['y2']['Σ'])
b = r * (Sy / Sx)
a = My - (b * Mx)

def przewidz_y(x, b, a):
    return b * x + a

def wsp_determinacji_r_kwadrat(b, a, df, My):
    SSm = 0.00
    SSt = 0.00
    for _, rzad in df.iterrows():
        x = rzad['X']
        y = rzad['Y']
        y_p = przewidz_y(x, b, a)
        SSm += (y_p - My) **2
        SSt += (y - My) ** 2
    return SSm / SSt

print("Model regresji liniowej: y = "+str(round(b,3))+"*x"+str(round(a,3)))

R2 = wsp_determinacji_r_kwadrat(b, a, df, My)
print("R^2 = ", round(R2,3))

# Okreslanie jakie będzie bezrobocie w danym roku:
rok = 2013
new_row = pd.DataFrame({'X': rok, 'Y': [np.nan]})
df = pd.concat([df, new_row], ignore_index=True)

# Wypełnienie wartości NaN za pomocą interpolacji liniowej
df['Y'] = df['Y'].interpolate()
df.at[5, 'Y'] = przewidz_y(df['X'][5], b, a)
print("W roku "+str(rok)+" bezrobocie będzie wynosić:",round(df.at[5,'Y'],3))

# Przewidywanie w którym roku bezrobocie będzie wynosić 12%
proc_wyliczany = 12
okreslanie =(proc_wyliczany+(a*(-1)))/b
print("Bezrobocie przekroczy "+str(proc_wyliczany)+"% w", int(round(okreslanie,0)))

fig = plt.figure(dpi = 300)
camera = Camera(fig)

for i in range(len(elem_X)):
    plt.plot(elem_X[:i], elem_Y[:i], c = 'royalblue')
    camera.snap()

anim = FuncAnimation(fig, camera.animate, frames=100, interval=100)
plt.show()
