import numpy as np
import matplotlib.pyplot as plt

#Vetor que recebe a transformação
vetorC = np.array([2,2])

#Constante cisalhante
k=3

#Eixo X
Tx = np.array([[1,k],[0,1]])

#Coordenadas do vetor
x1 = [vetorC[0],vetorC[0]]
y1 = [0,vetorC[1]]

#Calculo de transformação
matrizTx = np.dot(Tx,vetorC)

xT = [matrizTx[1]+2,matrizTx[0]]
yT = [0,matrizTx[1]]

###### Eixo Y  #############################################################################################
Ty = np.array([[1,0],[k,1]])

#Coordenadas do vetor
x2 = [0,vetorC[0]]
y2 = [vetorC[1],vetorC[1]]

#Calculo de transformação
matrizTy = np.dot(Ty,vetorC)

xTy = [0,matrizTy[0]]
yTy = [matrizTy[0],matrizTy[1]]

#Plot em relação a X
#plt.plot(x1,y1, color='b')
#plt.plot(xT,yT, color='r')
#plt.show()

#Plot em relação a Y
plt.plot(x2,y2, color='b')
plt.plot(xTy,yTy, color='g')
plt.show()
