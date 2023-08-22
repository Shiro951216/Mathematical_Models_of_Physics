import numpy as np
import matplotlib.pyplot as plt

plt.rc('text', usetex=True)
plt.rcParams['font.family']= 'cm'

x = y = np.linspace(-10, 10, 10)
X, Y = np.meshgrid(x, y)

u = X
v = Y

fig = plt.figure(figsize=(8,6))
plt.subplot(111)
plt.quiver(X, Y, u, v, units='xy', color='b')
plt.title(r"$\vec{\bf{v}} = \vec{\bf{r}}$ ", fontsize=15)

plt.savefig('Fig3b', dpi=300)
plt.show()