import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

plt.rc('text', usetex=True)
plt.rcParams['font.family']= 'cm'
plt.rc('text.latex', preamble=r'\usepackage{amsmath}')

velocidad_electron = 3e6  # velocidad inicial m/s
campo_electrico = 400  # N/C dirigido hacia arriba
tiempo_total = 3000e-9  # 3000 ns en segundos
incremento_tiempo = 100e-9  # 100 ns en segundos
carga_electron = -1.6e-19 # carga electron
masa_electron = 9.11e-31 # masa electron

def calcular_posicion(tiempo):
    velocidad_x = velocidad_electron
    aceleracion_y = campo_electrico * carga_electron / masa_electron
    x = velocidad_x * tiempo
    y = 0.5 * aceleracion_y * tiempo**2
    return x, y

def animate(n):
    fig.clear()
    ax1 = fig.add_subplot()
    X1 = calcular_posicion(dt[n])[0]
    Y1 = calcular_posicion(dt[n])[1]
    ax1.plot(X1, Y1, 'bo', markersize=12)
    ax1.plot(X1, Y1, 'w_', markersize=11)
    ax1.set_xlim(limites_X[0],limites_X[1])
    ax1.set_ylim(limites_Y[0],limites_Y[1])
    ax1.set_xlabel(r'X')
    ax1.set_ylabel(r'Y')
    ax1.set_title(f'Posición del electrón en $t = {dt[n]*10**9:.0f}$ ns')
    ax1.grid()
    plt.tight_layout()

fig = plt.figure(figsize=(8,7))
dt = np.linspace(0,tiempo_total,100)
posiciones = [calcular_posicion(t) for t in dt]
pos_x  = [tupla[0] for tupla in posiciones]
pos_y  = [tupla[1] for tupla in posiciones]
limites_X = [min(pos_x), max(pos_x)]
limites_Y = [min(pos_y), max(pos_y)]

ani = FuncAnimation(fig, animate, frames=len(dt))
ani.save('electron_animation.mp4', fps=30, dpi = 300)