import matplotlib.pyplot as plt

x = [0, 1, 2, 3, 4, 5, 6, 7, 8,  9, 10, 11]
y = [2, 5, 4, 6, 7, 6, 8, 8, 9, 10, 15, 25]

figura, eixo = plt.subplots()

eixo.plot(x, y, linewidth=7.0)

plt.show()
