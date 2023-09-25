import numpy as np
import matplotlib.pyplot as plt

plt.rc('text', usetex=True)
plt.rcParams['font.family']= 'cm'
plt.rc('text.latex', preamble=r'\usepackage{amsmath}')

velocidad_electron = 3e6  # velocidad inicial m/s
campo_electrico = 400  # N/C dirigido hacia arriba
tiempo_total = 3000e-9  # 3000 ns en segundos
incremento_tiempo = 100e-9  # 100 ns en segundos
carga_electron = -1.6e-19 # carga electron
masa_electron = 9.11e-31 # masa electron

def find_position(tiempo):
    aceleracion = campo_electrico * carga_electron / masa_electron
    posicion_horizontal = velocidad_electron * tiempo
    posicion_vertical = 0.5 * aceleracion * (tiempo ** 2)
    return posicion_horizontal, posicion_vertical

tiempos = np.arange(0, tiempo_total + incremento_tiempo, incremento_tiempo)
posiciones = [find_position(t) for t in tiempos]
xdata = [tupla[0] for tupla in posiciones]
ydata = [tupla[1] for tupla in posiciones]

fig = plt.figure(figsize=(8,6))
plt.xlim(min(find_position(t)[0] for t in tiempos),
         max(find_position(t)[0] for t in tiempos))
plt.ylim(min(find_position(t)[1] for t in tiempos),
         max(find_position(t)[1] for t in tiempos))

sc1 = plt.scatter(xdata, ydata, s=60, marker='o', c='b')
sc2 = plt.scatter(xdata, ydata, s=30, marker='_', c='w')

plt.xlabel('X (m)')
plt.ylabel('Y (m)')
plt.title(f'Posición del electrón de $t=0$ a $t=3000$ ns')
plt.savefig('Ejercicio_1a.png')
plt.show()