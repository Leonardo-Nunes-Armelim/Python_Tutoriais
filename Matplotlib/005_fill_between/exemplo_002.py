import matplotlib.pyplot as plt
import numpy as np

x = np.array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
up = np.random.uniform(0.0, 0.5, len(x))
bottom = np.random.uniform(0.0, 0.5, len(x))

y1 = 3 + 3 * x / 6 + up
y2 = 1 + 2 * x / 6 + bottom

figura, eixo = plt.subplots()

eixo.fill_between(x, y1, y2, alpha=0.3, linewidth=0)
#eixo.fill_between(x, y1, y2, alpha=0.3, linewidth=0, step='pre')
eixo.fill_between(x, y1, y2, alpha=0.3, linewidth=0, step='mid')
#eixo.fill_between(x, y1, y2, alpha=0.3, linewidth=0, step='post')
eixo.scatter(x, (y1 + y2)/2, s=50, c='C0')
eixo.plot(x, (y1 + y2)/2, linewidth=2)

# Adiciona grade aos dois eixos do gráfico
eixo.grid(axis='both')
# Ajusta escala dos eixos
eixo.set(xlim=(0, 9), xticks=np.arange(1, 9), ylim=(0, 9), yticks=np.arange(1, 9))

plt.show()
