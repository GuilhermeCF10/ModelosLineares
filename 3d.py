import matplotlib.pyplot as plt
import pandas as pd 
import math
import numpy as np
from mpl_toolkits.mplot3d import Axes3D

betas = [381688.0823883057, 0.005685266373947227, -34.18806501727921]

plothiper = plt.figure()
grafico = plothiper.gca(projection='3d')

x1g = np.linspace(-10000,10000,20)
x2g = np.linspace(-10000,10000,20)

XG, YG = np.meshgrid(x1g, x2g)
Z = betas[0] + XG*betas[1] + YG*betas[2]

# grafico = plt.axes(projection='3d')

grafico.plot_wireframe(XG,YG,Z)
plt.show()

# 381688.0823883057	0.005685266373947227	-34.18806501727921