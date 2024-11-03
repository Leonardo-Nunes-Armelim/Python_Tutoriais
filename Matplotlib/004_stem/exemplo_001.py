import matplotlib.pyplot as plt

# Coordenada dos Dados
x = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
y = [5, 6, 4, 5, 7, 6, 1, 3, 5, 7]

figura, eixo = plt.subplots()

eixo.stem(x, y, bottom=2)

eixo.grid(axis='both')

plt.show()
