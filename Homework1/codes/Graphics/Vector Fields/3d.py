import numpy as np
import matplotlib.pyplot as plt

plt.rc('text', usetex=True)
plt.rc('text.latex', preamble=r'\usepackage{amsmath}')
plt.rcParams['font.family']= 'cm'

x = y = np.linspace(-1, 1)
X, Y = np.meshgrid(x, y)

R = np.hypot(X,Y)

u = (3*X*Y)/(R**5)
v = (2*Y**2 - X**2)/(R**5)

fig = plt.figure(figsize=(8,8))
plt.subplot(111)
plt.streamplot(X, Y, u, v, color=10**10*v, cmap='inferno', linewidth=0.5, density=1)
plt.title(r"$\vec{\bf{v}} = \dfrac{3xy}{r^5} \hat{\bf{i}} - \dfrac{2y^2-x^2}{r^5}\hat{\bf{j}}$ ", y=1.03, fontsize=15)

plt.tight_layout()
plt.savefig('Fig3d', dpi=300)
plt.show()