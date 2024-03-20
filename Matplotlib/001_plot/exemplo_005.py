import matplotlib.pyplot as plt

x =  [0, 1, 2, 3, 4, 5,  6,  7,  8,  9, 10, 11]
y1 = [1, 2, 3, 4, 5, 6,  7,  8,  9, 10, 11, 12]
y2 = [2, 3, 4, 5, 6, 7,  8,  9, 10, 11, 12, 13]
y3 = [3, 4, 5, 6, 7, 8,  9, 10, 11, 12, 13, 14]
y4 = [4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]

figura, eixo = plt.subplots()

eixo.plot(x, y1, linewidth=10, linestyle='dotted')
eixo.plot(x, y2, linewidth=10, linestyle='dashed')
eixo.plot(x, y3, linewidth=10, linestyle=(0, (1, 2)))
eixo.plot(x, y4, linewidth=10, linestyle=(0, (1, 2, 3)))

eixo.grid(True)

plt.show()
