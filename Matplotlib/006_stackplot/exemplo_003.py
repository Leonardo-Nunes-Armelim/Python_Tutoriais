import matplotlib.pyplot as plt

# Coordenada dos Dados
x   = [0, 2, 4, 6, 8]
y_1 = [1, 1, 2, 2, 3]
y_2 = [1, 1, 1, 1, 1]
y_3 = [1, 2, 1, 2, 3]

figura, eixo = plt.subplots()

eixo.stackplot(x, [y_1, y_2, y_3], labels=['azul', 'laranja', 'verde'])

eixo.legend()

eixo.grid(axis='both')

plt.show()
