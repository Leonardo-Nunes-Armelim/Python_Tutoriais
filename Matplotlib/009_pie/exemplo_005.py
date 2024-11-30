import matplotlib.pyplot as plt

itens = ['Barco', 'Trêm', 'Caminhão', 'Carro', 'Moto']
porcentagens = [40, 20, 15, 15, 10]

figura, eixo = plt.subplots()

# Tipos de hatch = '/', '\\', '|', '-', '+', 'x', 'o', 'O', '.', '*'
# Exemplos de combinações
# '/', '\\', '|', '-', '+', 'x', 'o', 'O', '.', '*'
# '//', '\\\\', '||', '--', '++', 'xx', 'oo', 'OO', '..', '**'
# '/o', '\\|', '|*', '-\\', '+o', 'x*', 'o-', 'O|', 'O.', '*-'

eixo.pie(porcentagens, labels=itens, hatch=['O', 'oO', 'O.O', '.||.', '*'])

plt.show()