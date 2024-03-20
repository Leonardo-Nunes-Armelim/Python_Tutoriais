import matplotlib.pyplot as plt

x =  [0, 1,  2, 3, 4, 5, 6, 7, 8,  9, 10, 11]

y1 = [2, 5,  4, 6, 7, 6, 8, 8, 9, 10, 15, 25]
y2 = [0, 1, -2, 2, 4, 5, 5, 6, 8, 12, 14, 20]
y3 = [0, 0,  1, 2, 3, 4, 4, 5, 6,  7,  8,  9]

figura, eixo = plt.subplots()

# (Vermelho, Verde, Azul)=(Red, Green, Blue)=(R, G, B)
#cor = (1, 0, 0)
# (Vermelho, Verde, Azul, Alpha)=(Red, Green, Blue)=(R, G, B, A)
#cor = (1, 0, 0, 0.2)
#cor = 'red'
cor = 'r'

eixo.plot(x, y1, color=cor, linewidth=7.0)
eixo.plot(x, y2, color='purple', linewidth=7.0)
eixo.plot(x, y3, color=(0.8, 0.8, 1), linewidth=7.0)

eixo.grid(True)

plt.show()
