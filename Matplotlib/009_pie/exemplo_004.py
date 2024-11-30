import matplotlib.pyplot as plt

itens = ['Barco', 'Trêm', 'Caminhão', 'Carro', 'Moto']
porcentagens = [40, 20, 15, 15, 10]

colors = ['red', 'green', 'blue', 'pink', 'gray']

figura, eixo = plt.subplots()

eixo.pie(porcentagens, labels=itens, colors=colors)

plt.show()