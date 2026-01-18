import numpy as np
import matplotlib.pyplot as plt

##Reflex]ao deve manter sua simetria entre os angulos, diferente da rotação
#Muito utilizado no estudo de reflexão da luz

#Vetor que recebe a transformação
vetorRe = np.array([1,3])

#matriz de transformaçõo
T = np.array([[1,0],[0,-1]])

#Coordenadas do vetor
x = [0,vetorRe[0]]
y = [0,vetorRe[1]]

#Calculo para transformação
matrizT = np.dot(T,vetorRe)

xT = [0,matrizT[0]]
yT = [0,matrizT[1]]

plt.plot(x,y, color = 'b')
plt.plot(xT,yT, color = 'r')
plt.show()
