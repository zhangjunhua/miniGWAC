
from mpl_toolkits.mplot3d.axes3d import Axes3D
from matplotlib import cm

import numpy as np
import matplotlib.pyplot as plt
def f1():
    plt.figure(1)  # 创建图表1
    plt.figure(2)  # 创建图表2

    ax1 = plt.subplot(211)  # 在图表2中创建子图1
    ax2 = plt.subplot(212)  # 在图表2中创建子图2
    plt.figure(3)
    plt.figure(3)
    # plt.plot([1,2,3,4], [1,4,9,16], 'ro')
    plt.plot([1, 2, 3, 4], [1, 4, 9, 16])
    plt.axis([0, 6, 0, 20])

    x = np.linspace(0, 3, 100)
    for i in range(5):
        plt.figure(1)  # ❶ # 选择图表1
        plt.plot(x, np.exp(i * x / 3))
        plt.sca(ax1)  # ❷ # 选择图表2的子图1
        plt.plot(x, np.sin(i * x))
        plt.sca(ax2)  # 选择图表2的子图2
        plt.plot(x, np.cos(i * x))

    plt.show()
def f2():
    fig = plt.figure()
    ax = fig.add_subplot(111)
    t = np.arange(0.0, 5.0, 0.01)
    s = np.cos(2*np.pi*t)
    line, = ax.plot(t, s, lw=2)
    print(t*2)
    ax.annotate('local max', xy=(2, 1), xytext=(3, 1.5),
                arrowprops=dict(facecolor='black', shrink=0.05),
                )

    ax.set_ylim(-2,2)
    plt.show()




def f3():
    fig = plt.figure()
    ax = fig.add_subplot(111, polar=True)
    r = np.arange(0, 1, 0.001)
    theta = 2 * 2 * np.pi * r
    line, = ax.plot(theta, r, color='#ee8d18', lw=3)

    ind = 800
    thisr, thistheta = r[ind], theta[ind]
    ax.plot([thistheta], [thisr], 'o')
    ax.annotate('a polar annotation',
                xy=(thistheta, thisr),  # theta, radius
                xytext=(0.05, 0.05),  # fraction, fraction
                textcoords='figure fraction',
                arrowprops=dict(facecolor='black', shrink=0.05),
                horizontalalignment='left',
                verticalalignment='bottom',
                )
    plt.show()


def f4():
    fig = plt.figure()

    ax = fig.add_subplot(1, 2, 1, projection='3d')
    X = np.arange(-5, 5, 0.25)
    Y = np.arange(-5, 5, 0.25)
    X, Y = np.meshgrid(X, Y)
    R = np.sqrt(X ** 2 + Y ** 2)
    Z = np.sin(R)
    surf = ax.plot_surface(X, Y, Z, rstride=1, cstride=1, cmap=cm.jet,
                           linewidth=0, antialiased=False)
    ax.set_zlim3d(-1.01, 1.01)

    # ax.w_zaxis.set_major_locator(LinearLocator(10))
    # ax.w_zaxis.set_major_formatter(FormatStrFormatter('%.03f'))

    fig.colorbar(surf, shrink=0.5, aspect=5)

    from mpl_toolkits.mplot3d.axes3d import get_test_data
    ax = fig.add_subplot(1, 2, 2, projection='3d')
    X, Y, Z = get_test_data(0.05)
    ax.plot_wireframe(X, Y, Z, rstride=10, cstride=10)

    plt.show()

def f5():
    plt.plot([1, 2, 3, 4], [1, 4, 9, 16],'ro')
    plt.axis([0, 6, 0, 20])
    plt.show()


f1()