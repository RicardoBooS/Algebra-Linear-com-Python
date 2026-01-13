import numpy as np
import scipy as sp
from scipy import linalg

#Matriz dos coeficientes
matriz = np.array([[1,2,3],[2,-1,1],[-2,-3,3]])

#Vetor das constantes
vet = np.array([2,-1,-11])

## .flatten() - transforma a matriz em uma unica sequencia
#matriz = np.array([matriz[:,0], matriz[:,1], matriz[:,2]]).T #Transformar a matriz em transposta

#Função regra de Cramer 3x3
def cramer3 (A,b): #A = matriz - v = Vetor
    det = sp.linalg.det(np.array([A[:,0],A[:,1],A[:,2]]).T)
    if det != 0:
        detx = sp.linalg.det(np.array([b[:],A[:,1],A[:,2]]).T)
        dety = sp.linalg.det(np.array([A[:,0],b[:],A[:,2]]).T)
        detz = sp.linalg.det(np.array([A[:,0],A[:,1],b[:]]).T)
        x = detx/det
        y = dety/det
        z = detz/det
        print('O valor de x é {:.2f}'.format(x))
        print('O valor de y é {:.2f}'.format(y))
        print('O valor de z é {:.2f}'.format(z))
    else:
        print('Determinante da Matriz dos coeficientes é nula')
cramer3(matriz,vet)

matriz2 = np.array([[3,2,7],[4,-29,3],[2,3,5]])
vet2 = np.array([1,2,2])

cramer3(matriz2,vet2)



#Função regra de Cramer 2x2
def cramer2 (A,b): #A = matriz - v = Vetor
    det = sp.linalg.det(np.array([A[:,0],A[:,1]]).T)
    if det != 0:
        detx = sp.linalg.det(np.array([b[:],A[:,1]]).T)
        dety = sp.linalg.det(np.array([A[:,0],b[:]]).T)
        x = detx/det
        y = dety/det
        print('O valor de x é {:.2f}'.format(x))
        print('O valor de y é {:.2f}'.format(y))
    else:
        print('Determinante da Matriz dos coeficientes é nula')


matriz3 = np.array([[1,4],[2,3]])
vet3 = np.array([200,180])
cramer2(matriz3,vet3)