import matplotlib.pyplot as plt

# Coordenada dos Dados
x      = [  1,   2,   3,   4,   5,   6,   7,   8]
height = [4.5, 5.8, 3.6, 4.8, 6.7, 6.8, 2.2, 3.5]

figura, eixo = plt.subplots()

eixo.bar(x, height)

eixo.grid(axis='y')

plt.show()
