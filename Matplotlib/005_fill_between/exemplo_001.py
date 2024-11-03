import matplotlib.pyplot as plt
import numpy as np

x      = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
up     = [2, 3, 3, 3, 5, 6, 7, 7, 9, 8]
bottom = [1, 2, 2, 1, 3, 4, 5, 4, 7, 6]

figura, eixo = plt.subplots()

eixo.fill_between(x, up, bottom, alpha=0.5, linewidth=0)
eixo.plot(x, (np.array(up) + np.array(bottom)) / 2, linewidth=2)

# Adiciona grade aos dois eixos do gráfico
eixo.grid(axis='both')
# Ajusta escala dos eixos
eixo.set(xlim=(0, 8), xticks=np.arange(1, 8), ylim=(0, 8), yticks=np.arange(1, 8))

plt.show()
