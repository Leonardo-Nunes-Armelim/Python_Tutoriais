import matplotlib.pyplot as plt

x =  [0, 1, 2, 3, 4, 5,  6,  7,  8,  9, 10, 11]

y1 = [2, 5,  4, 6, 7, 6, 8, 8, 9, 10, 15, 25]
y2 = [0, 1, -2, 2, 4, 5, 5, 6, 8, 12, 14, 20]
y3 = [0, 0,  1, 2, 3, 4, 4, 5, 6,  7,  8,  9]

figura, eixo = plt.subplots()

eixo.plot(x, y1, linewidth=2, marker='o')
eixo.plot(x, y2, linewidth=2, marker='s')
eixo.plot(x, y3, linewidth=2, marker='^')

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
