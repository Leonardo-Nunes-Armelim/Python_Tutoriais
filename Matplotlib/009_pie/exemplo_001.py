import matplotlib.pyplot as plt

porcentagens = [40, 20, 15, 15, 10]

figura, eixo = plt.subplots()

eixo.pie(porcentagens)

plt.show()