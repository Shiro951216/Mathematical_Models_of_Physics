# Import libraries
import numpy as np
import matplotlib.pyplot as plt
# Set LaTeX parameters
plt.rc('text', usetex=True)
plt.rcParams['font.family']= 'cm'
plt.rc('text.latex', preamble=r'\usepackage{amsmath}')
# Define the range of values of x to plot
x = np.linspace(0, 2*np.pi, 200)
# Plotting the function f(x)
y1 = np.sin(x)
fig = plt.figure(figsize=(18,8))
ax1 = fig.add_subplot(121)
ax1.plot(x, y1, 'b', linewidth = 2, label= r'$f(x)$')
ax1.set_xlim(0, 2*np.pi)
ax1.set_ylim(-1.5,1.5)
ax1.set_xticks(np.linspace(0, 2*np.pi, 5))
x1labels = ["$0$", r"$\dfrac{ \pi }{ 2 }$", r"$\pi$", r"$\dfrac{ 3 \pi } { 2 } $", r"$2\pi$"]
ax1.set_xticklabels(x1labels)
ax1.set_yticks(np.arange(-1,2,1))
ax1.set_xlabel(r'\bf{X}')
ax1.set_ylabel(r'\bf{Y}')
ax1.set_title(r'Gráfico de $f(x)=\sin{x}$', fontsize=18)
ax1.grid(color='gray', linewidth=0.15)
ax1.legend(shadow=True, loc='upper left', handlelength=1.5, fontsize=12)
#Plotting the function g(x)
y2 = x**2+3*x
ax2 = fig.add_subplot(122)
ax2.plot(x, y2, 'b', linewidth = 2, label=r'$g(x)$')
ax2.set_xlim(0, 2*np.pi)
ax2.set_ylim(0,60)
ax2.set_xticks(np.arange(0, 2*np.pi+0.01, np.pi/2))
x2labels = ['$0$', r"$\dfrac{ \pi }{ 2 }$", r'$\pi$', r"$\dfrac{3\pi }{ 2 }$", r'$2\pi$']
ax2.set_xticklabels(x2labels)
ax2.set_xlabel(r'\bf{X}')
ax2.set_ylabel(r'\bf{Y}')
ax2.set_title(r'Gráfico de $g(x)=x^2+3x$', fontsize=18)
ax2.grid(color='gray', linewidth=0.15)
ax2.legend(shadow=True, loc='upper left', handlelength=1.5, fontsize=12)
plt.tight_layout()
plt.savefig('Fig1a', dpi=300)
plt.show()