import matplotlib.pyplot as plt

x =  [0, 1,  2, 3, 4, 5, 6, 7, 8,  9, 10, 11]

y1 = [2, 5,  4, 6, 7, 6, 8, 8, 9, 10, 15, 25]
y2 = [0, 1, -2, 2, 4, 5, 5, 6, 8, 12, 14, 20]
y3 = [0, 0,  1, 2, 3, 4, 4, 5, 6,  7,  8,  9]

figura, eixo = plt.subplots()

eixo.plot(x, y1, linewidth=7.0)
eixo.plot(x, y2, linewidth=7.0)
eixo.plot(x, y3, linewidth=7.0)

eixo.grid(True)

plt.show()
