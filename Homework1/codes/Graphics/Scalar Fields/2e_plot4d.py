import numpy as np
import matplotlib as mpl
from matplotlib import cm
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

plt.rc('text', usetex=True)
plt.rcParams['font.family']= 'cm'
plt.rc('text.latex', preamble=r'\usepackage{amsmath}')
cmap = plt.cm.hot

fig = plt.figure(figsize=(10,8))
ax = fig.add_subplot(projection='3d')
ax.set_aspect('equal')
ax.set_xlabel(r'X')
ax.set_ylabel(r'Y')
ax.set_zlabel(r'Z')

x = np.linspace(-20 , 20, 10)
y = np.linspace(-20 , 20, 10)
z = np.linspace(-20 , 20, 10)

X, Y, Z = np.meshgrid(x, y, z)
F = X**2 + Y**2 + Z**2

norm = mpl.colors.Normalize(vmin=0, vmax=F.max())
ax.scatter(X, Y, Z, s=60, c=F, alpha=0.7, marker = '.', cmap=cmap)
plt.colorbar(mpl.cm.ScalarMappable(norm=norm, cmap=cmap), ax=ax)
plt.suptitle(r'$f(x)=x^2+y^2+z^2$', y=0.95, fontsize=18)

plt.savefig('Fig2e4d', dpi=300)
plt.show()