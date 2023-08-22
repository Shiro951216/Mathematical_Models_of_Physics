import numpy as np
import matplotlib.pyplot as plt
import matplotlib as mpl

plt.rc('text', usetex=True)
plt.rcParams['font.family']= 'cm'
plt.rc('text.latex', preamble=r'\usepackage{amsmath}')
cmap = plt.cm.plasma

x = y = np.linspace(-2,2)
X, Y = np.meshgrid(x, y)
Z = X - Y + 2
norm = mpl.colors.Normalize(vmin=Z.min(), vmax=Z.max())

fig = plt.figure(figsize=(12,6))
ax1 = fig.add_subplot(121, projection='3d')
ax1.view_init(elev=30, azim=105)
ax1.plot_surface(X, Y, Z, cmap=cmap)
ax1.set_xlabel(r'X')
ax1.set_ylabel(r'Y')
ax1.set_zlabel(r'Z')
ax1.set_title(r'3D Representation')

ax2 = fig.add_subplot(122)
ax2.contour(X, Y, Z, levels=np.arange(-10,10,0.1), cmap=cmap, linewidths=2)
ax2.set_xlim(-2,2)
ax2.set_ylim(-2,2)
ax2.set_title(r'Curve Levels', fontsize=13)
ax2.set_xlabel(r'X')
ax2.set_ylabel(r'Y')

fig.colorbar(mappable=mpl.cm.ScalarMappable(norm=norm, cmap=cmap), ax=ax2)

plt.suptitle(r'$f(x,y)=x-y+2$', fontsize=15)

plt.tight_layout()
plt.savefig('Fig2c', dpi=300)
plt.show()