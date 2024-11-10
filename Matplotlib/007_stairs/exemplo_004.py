import matplotlib.pyplot as plt

y = [1, 6, 4, 8, 6, 7, 9, 8, 10, 7]

figura, eixo = plt.subplots()

eixo.stairs(y, linewidth=7, fill=True)

eixo.grid(axis='both')

plt.show()
