import numpy as np
import matplotlib.pyplot as plt
import matplotlib as mpl

plt.rc('text', usetex=True)
plt.rcParams['font.family']= 'cm'
plt.rc('text.latex', preamble=r'\usepackage{amsmath}')
cmap = plt.cm.inferno

u = np.linspace(0,2*np.pi)
v = np.linspace(0,np.pi/2)
U, V = np.meshgrid(u,v)
X = 4*np.sin(V)*np.cos(U)
Y = 4*np.sin(V)*np.sin(U)
Z = 4*np.cos(V)
norm = mpl.colors.Normalize(vmin=Z.min(), vmax=Z.max())

fig = plt.figure(figsize=(10,8))
ax1 = fig.add_subplot(projection='3d')
ax1.plot_surface(X, Y, Z, cmap=cmap)
ax1.set_aspect('equal')
ax1.set_xlabel(r'X')
ax1.set_ylabel(r'Y')
ax1.set_zlabel(r'Z')
plt.colorbar(mappable=mpl.cm.ScalarMappable(norm=norm, cmap=cmap),
             ax=ax1, shrink=0.7, pad=0.1)


plt.suptitle(r'$f(x,y)=\sqrt{16-x^2-y^2}$',y=0.9,fontsize=18)
plt.tight_layout()
plt.savefig('Fig2d', dpi=300)
plt.show()