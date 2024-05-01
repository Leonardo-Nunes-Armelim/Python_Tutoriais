import matplotlib.pyplot as plt
import numpy as np

# Coordenada dos Dados
x = [0, 1, 2, 3, 4, 5, 6, 7]

height_1 = [4, 5, 3, 4, 6, 6, 2, 3]
height_2 = [2, 2, 1, 2, 1, 5, 5, 4]
height_3 = [1, 2, 3, 3, 2, 1, 1, 2]

figura, eixo = plt.subplots()

eixo.bar(x, height_1)

eixo_2 = height_1
eixo.bar(x, height_2, bottom=eixo_2)

eixo_3 = np.array(height_1) + np.array(height_2)
eixo.bar(x, height_3, bottom=eixo_3)

eixo.grid(axis='y')

plt.show()
