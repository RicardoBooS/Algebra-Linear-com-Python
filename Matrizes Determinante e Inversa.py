import numpy as np
matrizA = np.array([[2,5],[1,3]])
matrizB = np.array([[3,-5],[-1,2]])

multi = np.dot(matrizA,matrizB)
print(multi)

##Matriz inversa
matriz_inv = np.linalg.inv(matrizA)
print(matriz_inv)

matriz_invB = np.linalg.inv(matrizB)
print(matriz_invB)

matrizC = np.array([[-11,2,2],[-4,0,1],[6,-1,-1]])
matriz_invC = np.linalg.inv(matrizC)
print(matriz_invC)

##OBS quando o determinante da matriz for igual a zero é sinal que ela não é inversivel

##Determinantes de matrizes
matrizE = np.array([[1,3,2],[4,2,4],[3,1,5]])
detE = np.linalg.det(matrizE)
print(detE)

import scipy as sp ## Melhor para calculos com determinates
from scipy import linalg

detE = sp.linalg.det(matrizE)
print(detE)

matrizG = np.array([[1,2,3],[4,5,6],[7,8,9]]) ## Essa matriz não tem inversa, resultado igual a Zero
detG = sp.linalg.det(matrizG)
print(detG)

matrizH = np.array([[1,3,0,-2,1],[4,2,4,5,4],[0,1,5,-3,2],[-2,3,1,0,7],[0,1,9,3,2]])
detH = sp.linalg.det(matrizH)
print(detH)

