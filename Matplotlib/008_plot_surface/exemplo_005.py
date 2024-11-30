import matplotlib.pyplot as plt
from matplotlib import cm
import numpy as np

# Coordenada dos Dados
X = np.arange(-5, 5, 0.25)
Y = np.arange(-5, 5, 0.25)
X, Y = np.meshgrid(X, Y)
Z = np.sin(X) * np.cos(Y)

norm = plt.Normalize(Z.min(), Z.max())
colors = cm.viridis(norm(Z))

figura, eixo = plt.subplots(subplot_kw={"projection": "3d"})

eixo.plot_surface(X, Y, Z, facecolors=colors)

eixo.set_xlabel('Eixo X')
eixo.set_ylabel('Eixo Y')
eixo.set_zlabel('Eixo Z')

plt.show()