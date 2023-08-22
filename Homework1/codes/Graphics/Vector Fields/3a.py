import numpy as np
import matplotlib.pyplot as plt

plt.rc('text', usetex=True)
plt.rcParams['font.family']= 'cm'
plt.rc('text.latex', preamble=r'\usepackage{amsmath}')

x = y = np.linspace(-10, 10, 10)
X, Y = np.meshgrid(x, y)

u = 3
v = -5

fig = plt.figure(figsize=(8,6))
plt.subplot(111)
plt.quiver(X, Y, u, v, color='b')
plt.title(r"$\vec{\bf{v}} = 3 \hat{\textbf{i}} -5 \hat{\textbf{j}}$ ", fontsize=15)

plt.savefig('Fig3a', dpi=300)
plt.show()