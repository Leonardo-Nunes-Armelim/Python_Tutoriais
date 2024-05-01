import matplotlib.pyplot as plt

# Coordenada dos Dados
x      = [  0,   1,   2,   3,   4,   5,   6,   7]
height = [4.5, 5.8, 3.6, 4.8, 6.7, 6.8, 2.2, 3.5]

figura, eixo = plt.subplots()

# O alinhamento das barras já vem centralizado como padrão => Exemplo: align='center'
eixo.bar(x, height, align='edge')

eixo.grid(axis='y')

plt.show()
