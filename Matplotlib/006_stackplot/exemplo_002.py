import matplotlib.pyplot as plt

# Coordenada dos Dados
x   = [0, 2, 4, 6, 8]
y_1 = [1, 1, 2, 2, 3]
y_2 = [1, 1, 1, 1, 1]
y_3 = [1, 2, 1, 2, 3]

figura, eixo = plt.subplots()

#'zero': Constant zero baseline, i.e. a simple stacked plot.
#'sym':  Symmetric around zero and is sometimes called 'ThemeRiver'.
#'wiggle': Minimizes the sum of the squared slopes.
#'weighted_wiggle': Does the same but weights to account for
#    size of each layer. It is also called 'Streamgraph'-layout. More
#    details can be found at http://leebyron.com/streamgraph/.

#eixo.stackplot(x, [y_1, y_2, y_3], baseline='zero')
eixo.stackplot(x, [y_1, y_2, y_3], baseline='sym')
#eixo.stackplot(x, [y_1, y_2, y_3], baseline='wiggle')
#eixo.stackplot(x, [y_1, y_2, y_3], baseline='weighted_wiggle')

eixo.grid(axis='both')

plt.show()
