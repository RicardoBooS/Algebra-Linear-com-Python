import numpy as np
import matplotlib.pyplot as plt

#Vetor que recebe a transformação
vetorR = np.array([4,1])

# Pi radiano = 180 graus
#Angulo de rotação (30 graus = pi/6 radianos)
alfa = (np.pi/6)

#matriz de transformaçõo
T = np.array([[np.cos(alfa),(-np.sin(alfa))],# sinal negativo no 1º sen significa que a rotação será no sentido anti-horário
              [np.sin(alfa),np.cos(alfa)]]) # Caso esteja no 2º sen a rotação acontece no sentido horário
print(T)

#Coordenadas do vetor
x = [0,vetorR[0]]
y = [0,vetorR[1]]

#calculo para transformação
matrizT = np.dot(T,vetorR)

xT = [0,matrizT[0]]
yT = [0,matrizT[1]]

plt.plot(x,y,color='b')
plt.plot(xT,yT,color='r')
plt.show()



