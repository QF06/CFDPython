import numpy as np
import matplotlib.pyplot as plt

nx = 41 # 长度上采样的个数
dx = 2/(nx-1) # 计算所关心的长度范围
nt = 25 # 时间上采样的个数
dt = 10/(nt-1) # 计算所关心的时间范围
c = 0.05 # 假设波速
u = np.ones(nx)
u[int(.5/dx):int(1/dx)] = 2 #初始值
l = np.linspace(0,2,nx)

un = np.ones(nx)
for n in range(nt):
    un = u.copy()
    for i in range(nx):
        u[i] = un[i] - c*dt/dx*(un[i]-un[i-1])

plt.plot(l,u)
plt.show()