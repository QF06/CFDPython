import numpy as np
import matplotlib.pyplot as plt

nx = 41
dx = 2/(nx-1)
nt = 25
dt = .025
u = np.ones(nx)
u[int(.5/dx):int(1/dx)]=2
l=np.linspace(0,2,nx)
plt.plot(l,u)
plt.show()