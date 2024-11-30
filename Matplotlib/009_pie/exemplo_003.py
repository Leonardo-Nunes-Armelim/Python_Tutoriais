import matplotlib.pyplot as plt

itens = ['Barco', 'Trêm', 'Caminhão', 'Carro', 'Moto']
porcentagens = [40, 20, 15, 15, 10]

figura, eixo = plt.subplots()

eixo.pie(porcentagens, labels=itens, autopct='%1.1f%%')

plt.show()