import numpy as np
import matplotlib.pyplot as plt

#Vetor que recebe a transformação
vetorT = np.array([[3,2],[2,5]])

#matriz de transformaçõo
T = np.array([[4,1],[4,1]])

#coordenadas do vetor
x = [vetorT[0][0],vetorT[1][0]]
y = [vetorT[0][1],vetorT[1][1]]

##Calculo para transformação
matrizT = vetorT + T

xT = [matrizT[0][0],matrizT[1][0]]
yT = [matrizT[0][1],matrizT[1][1]]

plt.plot(x,y, color='r')
plt.plot(xT,yT, color='b')
plt.show()