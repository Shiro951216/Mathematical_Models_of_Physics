import numpy as np
import matplotlib.pyplot as plt
import matplotlib as mpl

plt.rc('text', usetex=True)
plt.rcParams['font.family']= 'cm'
plt.rc('text.latex', preamble=r'\usepackage{amsmath}')
cmap = plt.cm.hot

r = np.linspace(0.02, 1, 40)
p = np.linspace(0, 2*np.pi, 40)
R, P = np.meshgrid(r, p)
Z = 1/R

X, Y = R*np.cos(P), R*np.sin(P)

fig = plt.figure(figsize=(13,6))
ax1 = fig.add_subplot(121, projection='3d')
ax1.plot_surface(X, Y, Z, cmap=cmap)
ax1.set_zlim(0,40)
ax1.set_title(r'3D Representation', fontsize=13)
ax1.set_xlabel(r'X')
ax1.set_ylabel(r'Y')
ax1.set_zlabel(r'Z')

ax2 = fig.add_subplot(122)
contour = ax2.contourf(X, Y, Z, levels = 30, cmap=cmap)
ax2.set_xlim(-0.5,0.5)
ax2.set_ylim(-0.5,0.5)
ax2.set_title(r'Contour Filled Map', y=1.02, fontsize=13)
ax2.set_xlabel(r'X')
ax2.set_ylabel(r'Y')

norm = mpl.colors.Normalize(vmin=0, vmax=40)
fig.colorbar(mpl.cm.ScalarMappable(norm=norm, cmap=cmap), ax=ax2)

fig.suptitle(r'$f(r)=\dfrac{1}{r}$', fontsize=15)

plt.tight_layout()
plt.savefig('Fig2a', dpi=300)
plt.show()