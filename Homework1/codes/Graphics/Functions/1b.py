import numpy as np
import matplotlib.pyplot as plt

plt.rc('text', usetex=True)
plt.rcParams['font.family']= 'cm'

fig, ax = plt.subplots(1,1,figsize=(10,8))

x1 = np.linspace(-10, 10, 200)
y1 = x1**2 + 5*x1-3
ax.plot(x1, y1, 'r--', linewidth = 2, label = r'$f(x)$')
ax.set_xlim(-10,10)
ax.set_xlabel(r'\bf{X}')
ax.set_ylabel(r'\bf{Y}')
ax.set_title(r'Polinomio $f(x)=x^2 + 5x -3$', fontsize=18)
ax.legend(shadow=True, loc='upper left', fontsize=12)
ax.grid()

plt.tight_layout()
plt.savefig('Fig1b', dpi=300)
plt.show()