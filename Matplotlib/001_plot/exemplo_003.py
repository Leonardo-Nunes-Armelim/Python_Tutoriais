import matplotlib.pyplot as plt

x =  [0, 1,  2, 3, 4, 5, 6, 7, 8,  9, 10, 11]

y1 = [[1,  2 , 1],
      [2,  1 , 2],
      [3,  4 , 4],
      [5,  3 , 8],
      [7,  5 , 16],
      [10, 8 , 8],
      [8,  10, 4],
      [10, 15, 2],
      [13, 12, 1],
      [15, 17, 5],
      [16, 18, 10],
      [16, 20, 15]]

figura, eixo = plt.subplots()

eixo.plot(x, y1, linewidth=7.0)

eixo.grid(True)

plt.show()
