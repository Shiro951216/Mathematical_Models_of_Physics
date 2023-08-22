import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

plt.rc('text', usetex=True)
plt.rcParams['font.family']= 'cm'
plt.rc('text.latex', preamble=r'\usepackage{amsmath}')
cmap = plt.cm.inferno
norm = mpl.colors.Normalize(vmin=0, vmax=400)

fig = plt.figure(figsize=(13,6))

k = np.linspace(0,400,160)
u = np.linspace(0,2*np.pi)
v = np.linspace(0,np.pi)
U, V = np.meshgrid(u,v)

def animate(n):
    fig.clear()
    ax1 = fig.add_subplot(1,2,1,projection='3d')
    ax2 = fig.add_subplot(1,2,2)
    
    X1 = np.sqrt(k[n])*np.sin(V)*np.cos(U)
    Y1 = np.sqrt(k[n])*np.sin(V)*np.sin(U)
    Z1 = np.sqrt(k[n])*np.cos(V)
    ax1.plot_surface(X1, Y1, Z1, alpha=0.5, cmap=cmap)
    ax1.set_aspect('equal')
    ax1.set_xlim(-20,20)
    ax1.set_ylim(-20,20)
    ax1.set_zlim(-20,20)
    ax1.set_xlabel(r'X')
    ax1.set_ylabel(r'Y')
    ax1.set_zlabel(r'Z')
    ax1.set_title(r'Surface levels for $f(x,y,z)=k$', fontsize=14)

    ax2.contour(X1, Y1, X1**2 + Y1**2, levels=10, norm=norm, cmap=cmap)
    fig.colorbar(mpl.cm.ScalarMappable(norm=norm, cmap=cmap), ax=ax2)
    ax2.set_xlim(-20,20)
    ax2.set_ylim(-20,20)
    ax2.set_xlabel(r'X')
    ax2.set_ylabel(r'Y')
    ax2.set_title(r'$f(x,y,0)$', fontsize=14)
    fig.suptitle(f'$f(x,y,z)=x^2+y^2+z^2=k={k[n]:.2f}$', fontsize=18)
    plt.tight_layout()

    if n==130:
        plt.savefig('Fig2e', dpi=300)

anim = FuncAnimation(fig=fig, func=animate, frames=len(k), interval=1)
anim.save('2e.mp4', fps=30, dpi=300)