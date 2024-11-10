import matplotlib.pyplot as plt

# Coordenada dos Dados
x   = [0, 2, 4, 6, 8]
y_1 = [1, 1, 2, 2, 3]
y_2 = [1, 1, 1, 1, 1]
y_3 = [1, 2, 1, 2, 3]

figura, eixo = plt.subplots()

# Tipos de hatch = '/', '\\', '|', '-', '+', 'x', 'o', 'O', '.', '*'
eixo.stackplot(x, [y_1, y_2, y_3], hatch=['/', '+', 'O'])

eixo.grid(axis='both')

plt.show()
