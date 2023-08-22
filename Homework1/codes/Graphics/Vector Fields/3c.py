import numpy as np
import matplotlib.pyplot as plt

plt.rc('text', usetex=True)
plt.rcParams['font.family']= 'cm'
plt.rc('text.latex', preamble=r'\usepackage{amsmath}')

x = y = np.linspace(-1, 1, 20)
r = np.hypot(x,y)
X, Y = np.meshgrid(x, y)

u = X/r**3
v = Y/r**3

fig = plt.figure(figsize=(8,8))
plt.subplot(111)
plt.quiver(X, Y, u, v, color='b')
plt.title(r"$\vec{\bf{v}} = \dfrac{ \vec{ \bf{r} } }{r^2}$ ", y = 1.02, fontsize=15)

plt.tight_layout()
plt.savefig('Fig3c', dpi=300)
plt.show()