import matplotlib.pyplot as plt
import numpy as np

def classroom_average(notas):
    # Soma as notas
    soma_das_notas = 0
    for i in notas:
        soma_das_notas += i

    return soma_das_notas / len(notas)

aluno = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
notas = [6, 7, 8, 3, 9, 5, 6, 8, 7, 5]
media_da_sala = classroom_average(notas)
print("Média da sala:", media_da_sala)

figura, eixo = plt.subplots()

eixo.stem(aluno, notas, bottom=media_da_sala)

# Adiciona grade aos dois eixos do gráfico
eixo.grid(axis='both')
# Ajusta escala dos eixos
eixo.set(xlim=(0, 11), xticks=np.arange(1, 11), ylim=(0, 11), yticks=np.arange(1, 11))

plt.show()
