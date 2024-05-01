import matplotlib.pyplot as plt
import numpy as np

# Coordenada dos Dados
x        = [0, 1, 2, 3, 4, 5, 6, 7]
height   = [4, 5, 3, 4, 6, 6, 2, 3]
altura   = [0, 2, 1, 2, 1, 5, 5, 4]

figura, eixo = plt.subplots()

eixo.bar(x, height, bottom=altura)

eixo.grid(axis='y')

plt.show()
