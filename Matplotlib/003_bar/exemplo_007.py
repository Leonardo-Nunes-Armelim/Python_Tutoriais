import matplotlib.pyplot as plt

# Coordenada dos Dados
x_1      = [  0,   1,   2,   3,   4,   5,   6,   7]
height_1 = [4.5, 5.8, 3.6, 4.8, 6.7, 6.8, 2.2, 3.5]

x_2      = [0.25, 1.25, 2.25, 3.25, 4.25, 5.25, 6.25, 7.25]
height_2 = [ 6.2,  6.5,  4.1,  5.2,  7.5,  7.5,  2.5,  4.5]

x_3      = [0.5, 1.5, 2.5, 3.5, 4.5, 5.5, 6.5, 7.5]
height_3 = [  5,   6,   4,   5,   7,   7, 1.5,   4]

figura, eixo = plt.subplots()

eixo.bar(x_1, height_1, align='edge', width=0.25, color=(1, 0, 0))
eixo.bar(x_2, height_2, align='edge', width=0.25, color=(0, 1, 0))
eixo.bar(x_3, height_3, align='edge', width=0.25, color=(0, 0, 1))

eixo.grid(axis='y')

plt.show()
