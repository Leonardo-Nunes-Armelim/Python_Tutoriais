import matplotlib.pyplot as plt
import numpy as np

x = np.arange(9)
up = np.random.uniform(0.0, 0.5, len(x))
bottom = np.random.uniform(0.0, 0.5, len(x))

y1 = 2.75 + 3 * x / 6 + up
y2 = 2.25 + 2 * x / 6 + bottom
y3 = 3 + 3 * x / 6 + up
y4 = 2 + 2 * x / 6 + bottom
y5 = 3.5 + 3 * x / 6 + up
y6 = 1.5 + 2 * x / 6 + bottom

figura, eixo = plt.subplots()

eixo.fill_between(x, y1, y2, alpha=0.5, linewidth=0, color='b')
eixo.fill_between(x, y3, y4, alpha=0.4, linewidth=0, color='g')
eixo.fill_between(x, y5, y6, alpha=0.3, linewidth=0, color='r')
eixo.plot(x, (y1 + y2)/2, linewidth=3, c='r')

# Adiciona grade aos dois eixos do gráfico
eixo.grid(axis='both')
# Ajusta escala dos eixos
eixo.set(xlim=(0, 8), xticks=np.arange(1, 8), ylim=(0, 8), yticks=np.arange(1, 8))

plt.show()
