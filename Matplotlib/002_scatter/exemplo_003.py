import matplotlib.pyplot as plt

# Coordenada dos Dados
x1 = [1, 5, 3, 7, 10, 12,  9, 18, 20, 13, 22, 27, 25, 30, 32, 28, 35, 37, 40, 45, 42, 50]
y1 = [1, 2, 5, 3,  8, 15, 10, 15, 18, 13, 25, 23, 25, 25, 31, 33, 35, 40, 37, 42, 47, 50]

x2 = [41, 22, 42, 36, 31, 48, 24, 47, 27, 29, 40, 40, 45, 32, 24, 47, 24, 45, 42, 48, 47, 23]
y2 = [ 7, 12, 24, 19,  6, 10,  5, 17,  6,  1, 17, 15,  1, 10, 17, 10,  1, 18,  9, 11, 15, 11]

x3 = [1,  7,  10,  4,  3,  9, 10, 20, 25, 18,  1,  5, 20,  4, 23, 22, 17, 12, 15,  7,  4, 17]
y3 = [50, 45, 40, 44, 39, 30, 35, 38, 40, 44, 33, 32, 39, 41, 42, 44, 35, 38, 40, 44, 48, 38]

figura, eixo = plt.subplots()

eixo.scatter(x1, y1, s=100)
eixo.scatter(x2, y2, s=100)
eixo.scatter(x3, y3, s=100)

eixo.grid(True)

plt.show()
