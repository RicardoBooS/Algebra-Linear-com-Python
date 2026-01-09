import numpy as np
matrizA = np.array([[2,-3],[4,-6],[6,9]])
matrizB = np.array([[1,7],[-3,4],[5,-8]])

##Soma de Matrizes
somaAB = matrizA + matrizB
print(somaAB)

somaBA = matrizB + matrizA
print(somaBA)

##Subtração de matrizes
subAB = matrizA - matrizB
print(subAB)

subBA = matrizB - matrizA
print(subBA)

##Multiplicação por um escalar
multi1 = matrizA * 2
print(multi1)

multi2 = matrizB * -3
print(multi2)

##Multiplicação entre matrizes
matrizC = np.array([[2,1],[3,4],[5,6]])
matrizD = np.array([[7,8,0],[10,5,-2]])

multiCD = np.dot(matrizC,matrizD)
print(multiCD)

multiDC = np.dot(matrizD,matrizC)
print(multiDC)

##OBS- Para a multiplicação de matrizes o numero de colunas de uma matriz deve ser o mesmo de linhas da outra matriz