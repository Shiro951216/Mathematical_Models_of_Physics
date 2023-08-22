import numpy as np
import matplotlib.pyplot as plt

plt.rc('text', usetex=True)
plt.rcParams['font.family']= 'cm'
plt.rc('text.latex', preamble=r'\usepackage{amsmath}')

x = y = np.linspace(-8, 8, 28)
X, Y = np.meshgrid(x, y)

u = np.cos(X)
v = np.sin(Y)

fig = plt.figure(figsize=(10,8))
plt.subplot(111)
plt.xlim(-7,7)
plt.ylim(-7,7)
plt.quiver(X, Y, u, v, np.hypot(u,v), cmap='magma')
plt.suptitle(r"$\vec{\bf{v}} = \cos{x} \hat{\bf{i}} + \sin{y} \hat{\bf{j}}$ ",
          fontsize=15)
cb = plt.colorbar()
cb.set_label(label='Vector magnitude', size=15, labelpad=-60)

plt.tight_layout()
plt.savefig('Fig3l', dpi=300)
plt.show()