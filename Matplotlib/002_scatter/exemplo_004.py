import matplotlib.pyplot as plt

# Coordenada dos Dados
x  = [1, 2, 3, 4, 5]
y1 = [1, 2, 3, 4, 5]
y2 = [2, 3, 4, 5, 6]
y3 = [3, 4, 5, 6, 7]

#color_1 = (1, 0, 0)
color_2 = (0, 1, 0)
color_3 = (0, 0, 1)
color_1 = [(1, 0, 0), (0, 1, 0), (0, 0, 1), (1, 1, 0), (1, 0, 1)]

figura, eixo = plt.subplots()

# Para adicionar um contorno colorido para os pontos de um conjunto de dados basta adicionar o parâmetro "edgecolors"
eixo.scatter(x, y1, s=200, c=color_1)
eixo.scatter(x, y2, s=200, c=color_2)
eixo.scatter(x, y3, s=200, c=color_3, edgecolors=(0, 0, 0))

eixo.grid(True)

plt.show()
