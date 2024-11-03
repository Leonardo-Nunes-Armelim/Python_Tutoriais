import matplotlib.pyplot as plt
import numpy as np

# Dados
x = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
y = [5, 6, 4, 5, 7, 7, 3, 3, 5, 9]

# Linha inclinada: y = 0.5x + 1
bottom_line = 0.5 * np.array(x) + 1

figura, eixo = plt.subplots()

eixo.plot(x, bottom_line, 'r--', label='Linha Inclinada (y = 0.5x + 1)')

# Desenha as hastes manualmente usando linhas verticais (vlines)
for xi, yi, bi in zip(x, y, bottom_line):
    eixo.vlines(xi, bi, yi, color='C0')

# Desenha os pontos do gráfico
eixo.scatter(x, y, s=50)

# Adiciona legenda da linha vermelha
eixo.legend()

# Adiciona grade aos dois eixos do gráfico
eixo.grid(axis='both')
# Ajusta escala dos eixos
eixo.set(xlim=(0, 11), xticks=np.arange(1, 11), ylim=(0, 11), yticks=np.arange(1, 11))

plt.show()
