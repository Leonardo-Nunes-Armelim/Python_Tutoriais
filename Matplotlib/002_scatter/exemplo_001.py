import matplotlib.pyplot as plt

# Coordenada dos Dados
x = [1, 2, 3, 4, 5]
y = [1, 2, 3, 4, 5]

figura, eixo = plt.subplots()

eixo.scatter(x, y, s=200)

eixo.grid(True)

plt.show()
