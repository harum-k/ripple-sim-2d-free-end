# free end refrections
# 自由端反射 2次元版

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
#import matplotlib as mpl

X_SU = 120
Y_SU = 40

fig = plt.figure(figsize = (12.8, 7.2))
ax = fig.add_subplot(111, projection="3d")

#print(mpl.rcParams.get('figure.figsize'))
#mpl.rcParams.update({'figure.figsize':[15,5]})
#print(mpl.rcParams.get('figure.figsize'))
plt.subplots_adjust(left=0, bottom=0, right=1, top=1)

x, y = np.meshgrid(range(0,X_SU),range(0,Y_SU))
z = 0.0 * x * y

z1 = z.copy()
k = z.copy()
#z[-20,25] = 40.0 # 中央
#z[-2,2] = 30.0 # 左上端
#z[int(Y_SU/2),2] = 30.0 # 左端中央
z[2,2] = 30.0 # 左下端
#z[-12,10] = 40.0 # 左上
#z[:,:10] = 0.5 # 津波
#z[-15:,:15] = 0.7


def update(i):
    global z,z1,k
    print(i)
    z[0,:] = z[1,:]
    z[-1,:] = z[-2,:]
    z[:,0] = z[:,1]
    z[:,-1] = z[:,-2]
    for ix in range(1,X_SU-1):
        for iy in range(1,Y_SU-1):
            z1[iy,ix] = (np.sum(z[iy-1:iy+2,ix]) + z[iy,ix-1] + z[iy,ix+1])/5 + k[iy,ix]
    if i > 6:
        k = z1 - z
    z[1:-1,1:-1] = z1[1:-1,1:-1] #.copy()
    ax.clear()
    vminmax = np.max(z)
    pl = ax.plot_surface(x, y, z, cmap = "viridis", vmin=-vminmax, vmax=vminmax)
    ax.set_zlim(-1,1)
    XYHAMI = int(X_SU*0.1)
    ax.set_xlim(XYHAMI,X_SU-XYHAMI)
    ax.set_ylim(0,X_SU-XYHAMI*4) #*0.8)

ani = animation.FuncAnimation(fig, update, interval=120, blit=False, save_count=720)
#ani.save("nami2d_freeend.mp4")
plt.show()
