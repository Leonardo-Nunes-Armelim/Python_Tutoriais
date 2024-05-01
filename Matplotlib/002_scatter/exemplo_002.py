import matplotlib.pyplot as plt

# Coordenada dos Dados
x = [1, 2, 3, 4, 5]
y = [1, 2, 3, 4, 5]

# Tamanho dos dados
size = [100, 200, 300, 400, 500]

figura, eixo = plt.subplots()

eixo.scatter(x, y, s=size)

eixo.grid(True)

plt.show()
