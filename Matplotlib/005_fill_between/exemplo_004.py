import matplotlib.pyplot as plt
import numpy as np

x = np.array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])

y1 = (0.4 * x)**2 + (0.2 * x) + 3
y2 = (0.4 * x)**2 - (0.2 * x) + 1

figura, eixo = plt.subplots()

eixo.fill_between(x, y1, y2, alpha=0.5, linewidth=0)
eixo.plot(x, (y1 + y2)/2, linewidth=2)

# Adiciona grade aos dois eixos do gráfico
eixo.grid(axis='both')

plt.show()
