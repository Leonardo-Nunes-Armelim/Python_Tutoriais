import matplotlib.pyplot as plt
import numpy as np

# Coordenada dos Dados
X = np.arange(-5, 5, 0.25)
Y = np.arange(-5, 5, 0.25)
X, Y = np.meshgrid(X, Y)
Z = np.sin(X) * np.cos(Y)

figura, eixo = plt.subplots(subplot_kw={"projection": "3d"})

eixo.plot_surface(X, Y, Z)

plt.show()