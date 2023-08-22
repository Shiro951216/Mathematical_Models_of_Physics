import numpy as np
import matplotlib.pyplot as plt

plt.rc('text', usetex=True)
plt.rcParams['font.family']= 'cm'
plt.rc('text.latex', preamble=r'\usepackage{amsmath}')

x = y = np.linspace(-11, 11, 20)
X, Y = np.meshgrid(x, y)

u = X/np.hypot(X, Y)
v = -Y/np.hypot(X, Y)

fig = plt.figure(figsize=(8,8))
plt.subplot(111)
plt.quiver(X, Y, u, v)
plt.xlim(-10,10)
plt.ylim(-10,10)
plt.title(r"$\vec{\bf{v}} = \dfrac{x}{\sqrt{x^2+y^2}} \hat{\bf{i}} - \dfrac{y}{\sqrt{x^2+y^2}} \hat{\bf{j}}$ ",
          y=1.03, fontsize=15)

plt.tight_layout()
plt.savefig('Fig3j', dpi=300)
plt.show()