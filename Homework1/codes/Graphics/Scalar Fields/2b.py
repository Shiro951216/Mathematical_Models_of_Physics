import numpy as np
import matplotlib.pyplot as plt
import matplotlib as mpl

plt.rc('text', usetex=True)
plt.rcParams['font.family']= 'cm'
plt.rc('text.latex', preamble=r'\usepackage{amsmath}')
cmap = plt.cm.twilight_shifted

x = y = np.linspace(-2,2)
X, Y = np.meshgrid(x, y)
Z = 1/np.hypot(X, Y-1)  -  1/np.hypot(X, Y+1)
norm = mpl.colors.Normalize(vmin=Z.min(), vmax=Z.max())

fig = plt.figure(figsize=(13,6))
ax1 = fig.add_subplot(121, projection='3d')
ax1.plot_surface(X, Y, Z, cmap=cmap)
ax1.set_zlim(0,20)
ax1.set_title(r'3D Representation', fontsize=13)
ax1.set_xlabel(r'X')
ax1.set_ylabel(r'Y')
ax1.set_zlabel(r'Z')

ax2 = fig.add_subplot(122)
ax2.contourf(X, Y, Z, levels = 50, cmap=cmap)
ax2.contour(X, Y, Z, levels = np.arange(-6,6,0.4), colors='k')
ax2.set_xlim(-2,2)
ax2.set_ylim(-2,2)
ax2.set_title(r'XY Plane projection', fontsize=13)
ax2.set_xlabel(r'X')
ax2.set_ylabel(r'Y')
fig.colorbar(mappable=mpl.cm.ScalarMappable(norm=norm, cmap=cmap), ax=ax2)

fig.suptitle(r'$f(r)=\dfrac{1}{\sqrt{x^2+(y-1)^2}} -\dfrac{1}{\sqrt{x^2+(y+1)^2}} $', fontsize=15)

plt.tight_layout()
plt.savefig('Fig2b', dpi=300)
plt.show()