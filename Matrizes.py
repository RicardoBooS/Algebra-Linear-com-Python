import numpy as np
matriz = np.array([[1,-2,3],[-4,5,6],[7,8,-9]])
print(matriz)
print(type(matriz))
print(matriz.shape)

##Matriz somente com numeros 1
matriz2 = np.ones((2,3))
print(matriz2)

##Matriz Nula
matrizo = np.zeros((2,3))
print(matrizo)

##Matriz diagonal
matriz3 = np.diag((2,3,6,8,10))
print(matriz3)

##Matriz identidade
matriz4= np.identity(3) ##OU UTILIZAR np.eye
print(matriz4)

##Matriz Transposta
matriz5 = np.array(matriz).T
print(matriz5)

##Matriz Oposta
matriz6 = -1*matriz
print(matriz6)

#Matriz linha e matriz coluna
linha = np.array([[2,3,4,5]])
print(linha)
coluna = np.array([[2],[3],[4],[5]])
print(coluna)
