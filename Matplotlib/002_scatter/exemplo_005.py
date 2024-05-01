import matplotlib.pyplot as plt

# Coordenada dos Dados
x = [1, 2, 3, 4, 5]
y = [1, 2, 3, 4, 5]

figura, eixo = plt.subplots()

eixo.scatter(x, y, s=200, marker='s')

eixo.grid(True)

plt.show()

# Outros tipos de Makers

# '.' point marker
# ',' pixel marker
# 'o' circle marker
# 'v' triangle_down marker
# '^' triangle_up marker
# '<' triangle_left marker
# '>' triangle_right marker
# '1' tri_down marker
# '2' tri_up marker
# '3' tri_left marker
# '4' tri_right marker
# '8' octagon marker
# 's' square marker
# 'p' pentagon marker
# 'P' plus (filled) marker
# '*' star marker
# 'h' hexagon1 marker
# 'H'	hexagon2 marker
# '+' plus marker
# 'x' x marker
# 'X' x (filled) marker
# 'D' diamond marker
# 'd' thin_diamond marker
# '|' vline marker
# '_' hline marker
