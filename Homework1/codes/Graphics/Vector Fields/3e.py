import numpy as np
import matplotlib.pyplot as plt

plt.rc('text', usetex=True)
plt.rcParams['font.family']= 'cm'

x = y = np.linspace(-1, 1)
X, Y = np.meshgrid(x, y)

u = X
v = -Y

fig = plt.figure(figsize=(8,8))
plt.subplot(111)
plt.streamplot(X, Y, u, v, linewidth=0.5)
plt.title(r"$\vec{\bf{v}} = x \hat{\bf{i}} - y \hat{\bf{j}}$", fontsize=15)

plt.tight_layout()
plt.savefig('Fig3e', dpi=300)
plt.show()