import numpy as np
import matplotlib.pyplot as plt

plt.rc('text', usetex=True)
plt.rcParams['font.family']= 'cm'
plt.rc('text.latex', preamble=r'\usepackage{amsmath}')

x = y = np.linspace(-10, 10, 20)
X, Y = np.meshgrid(x, y)

u = X**2
v = Y**2

fig = plt.figure(figsize=(8,8))
plt.subplot(111)
plt.quiver(X, Y, u, v)
plt.xlim(-10,10)
plt.ylim(-10,10)
plt.title(r"$\vec{\bf{v}} = x^2 \hat{\bf{i}} + y^2 \hat{\bf{j}}$ ", fontsize=15)

plt.tight_layout()
plt.savefig('Fig3i', dpi=300)
plt.show()