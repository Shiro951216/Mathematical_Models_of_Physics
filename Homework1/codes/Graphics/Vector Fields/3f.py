import numpy as np
import matplotlib.pyplot as plt

plt.rc('text', usetex=True)
plt.rcParams['font.family']= 'cm'
plt.rc('text.latex', preamble=r'\usepackage{amsmath}')

x = y = np.linspace(-10, 10, 10)
X, Y = np.meshgrid(x, y)

u = 1/np.sqrt(2)
v = -1/np.sqrt(2)

fig = plt.figure(figsize=(8,8))
plt.subplot(111)
plt.quiver(X, Y, u, v, )
plt.title(r"$\vec{\bf{v}} = \dfrac{1}{\sqrt{2}} (\hat{\bf{i}} - \hat{\bf{j}})$", fontsize=15)

plt.tight_layout()
plt.savefig('Fig3f', dpi=300)
plt.show()