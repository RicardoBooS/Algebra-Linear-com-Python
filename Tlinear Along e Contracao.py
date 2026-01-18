import numpy as np
import matplotlib.pyplot as plt

#Vetor que recebe a transformação
vetorA = np.array([4,2])
vetorB = np.array([6,2])
#Constante
#alongamento/ dilatação k > 1
#contração 0 < k < 1
k=2

#################### Eixo X ###############################

#Matriz de transformação
T = np.array([[k,0],[0,1]])

#Coordenadas de vetor
x = [0,vetorA[0]]
y = [vetorA[1],vetorA[1]]

#Calculo de transformação
matrizT = np.dot(T,vetorA)

xT = [0+6,matrizT[0]+6]
yT = [matrizT[1],matrizT[1]]

#plt.plot(x,y, color='red')
#plt.plot(xT,yT, color='blue')
#plt.show()

################### Eixo Y ################################

#Matriz de transformação
Ty = np.array([[1,0],[0,k]])

#Coordenadas de vetor
x1 = [vetorA[0],vetorA[0]]
y1 = [0,vetorA[1]]

x2 = [vetorB[0],vetorB[0]]
y2 = [0,vetorB[1]]

#Calculo de transformação
matrizTy = np.dot(Ty,vetorA)
matrizTy2 = np.dot(Ty,vetorB)

xTy = [matrizTy[0],matrizTy[0]]
yTy = [0+4,matrizTy[1]+4]

xTy2 = [matrizTy2[0],matrizTy2[0]]
yTy2 = [0+4,matrizTy2[1]+4]
plt.plot(x1,y1, color='red')
plt.plot(x2,y2, color='red')
plt.plot(xTy,yTy, color='blue')
plt.plot(xTy2,yTy2, color='blue')
plt.show()