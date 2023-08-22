import numpy as np
import matplotlib.pyplot as plt

plt.rc('text', usetex=True)
plt.rcParams['font.family']= 'cm'
plt.rc('text.latex', preamble=r'\usepackage{amsmath}')

x = y = np.linspace(-1, 1, 10)
X, Y = np.meshgrid(x, y)

u = 2*Y
v = 0

fig = plt.figure(figsize=(10,8))
plt.subplot(111)
plt.quiver(X, Y, u, v, u, cmap='inferno')
plt.suptitle(r"$\vec{\bf{v}} = 2y \hat{\bf{i}}$ ", fontsize=18)
plt.colorbar()
plt.tight_layout()
plt.savefig('Fig3h', dpi=300)
plt.show()