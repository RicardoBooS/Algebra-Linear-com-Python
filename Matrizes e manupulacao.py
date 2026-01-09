import numpy as np
matriz = np.array([[1,-2,3],[-4,5,6],[7,8,-9]])
print(matriz)

print(matriz[0,0])
print(matriz[0,1])
print(matriz[2,:])
print(matriz[:,1])

matriz7 = matriz.copy() ##copiar matrizes


matriz7[0,2] = 10 ## Substituição de valores da matriz
matriz7[1,1] = -12

matriz8 = matriz7[1,:] ##cria outra matriz apenas com partes das informações da matriz 7

matriz9 = matriz7[:,0] ##cria outra matriz apenas com partes das informações da matriz 7

matriz10 = matriz7[1,1:3] ##o numero 3 não conta para trazer a informação neste caso (trazendo assim as informações do 2)
print(matriz10)

##OBS:  Sempre prestar atenção na indexação do Python
