import numpy as np
import matplotlib.pyplot as plt

#Vetor que recebe a transformação
vetorH = [2,1]
vetorH = np.array(vetorH)

#Parametro de proporção
k = 3

#matriz de transformaçõo
T = np.array([[k,0],[0,k]])

#Coordenadas do vetor
x = [vetorH[0],0]
y = [0,vetorH[1]]

#calculo para transformação
matrizT = np.dot(T,vetorH)
#print(matrizT)

xT = [matrizT[0],0]
yT = [0,matrizT[1]]

plt.plot(x,y, color='r')
plt.plot(xT,yT, color='b')
plt.show()