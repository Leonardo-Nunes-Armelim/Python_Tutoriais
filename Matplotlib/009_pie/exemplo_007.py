import matplotlib.pyplot as plt

itens = ['Barco', 'Trêm', 'Caminhão', 'Carro', 'Moto']
porcentagens = [40, 20, 15, 15, 10]

destacar = (0, 0.1, 0, 0, 0)

figura, eixo = plt.subplots()

eixo.pie(porcentagens, labels=itens, autopct='%1.1f%%', explode=destacar)

plt.show()