import numpy as np
import matplotlib.pyplot as plt

plt.rc('text', usetex=True)
plt.rcParams['font.family']= 'cm'

x = np.linspace(-10, 10, 200)
y1 = 3*x*np.exp(x)
y2 = np.sin(x + 3)

plt.figure(figsize=(12,10))

plt.subplot(211)
plt.plot(x, y1, 'b-', linewidth = 2, label= r"$f(x)=3xe^x$")
plt.plot(x, y2, 'r--', linewidth = 2, label= r"$g(x)= \sin{(x+3)}$")
plt.xlim(0,6)
plt.ylim(-1,10)
plt.xlabel(r'\bf{X}')
plt.ylabel(r'\bf{Y}')
plt.title(r'Gráfico de $f(x)$ y $g(x)$ en el intervalo $\left[ 0,6 \right]$', fontsize=15)
plt.legend(shadow=True, loc='upper left', handlelength=1.5, fontsize=12)
plt.grid()

plt.subplot(223)
plt.plot(x, y1, 'b-', linewidth = 2, label= r"$f(x)$")
plt.xlim(0,6)
plt.ylim(-1,7500)
plt.xlabel(r'\bf{X}')
plt.ylabel(r'\bf{Y}')
plt.title(r'Gráfico de $f(x)=3xe^x$', fontsize=15)
plt.legend(shadow=True, loc='upper left', handlelength=1.5, fontsize=12)
plt.grid()

plt.subplot(224)
plt.plot(x, y2, 'r--', linewidth = 2, label= r"$g(x)$")
plt.xlim(0,6)
plt.ylim(-1.5,1.5)
plt.xlabel(r'\bf{X}')
plt.ylabel(r'\bf{Y}')
plt.title(r'Gráfico de $g(x)= \sin{(x+3)}$', fontsize=15)
plt.legend(shadow=True, loc='upper left', handlelength=1.5, fontsize=12)
plt.grid()

plt.tight_layout()
plt.savefig('Fig1c', dpi=300)
plt.show()