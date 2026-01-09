##Distância, norma e representação
import numpy as np
u = [2, -4, 1]
u = np.array(u)
v= np.array([3,2,-5])
def dist (vetor1, vetor2): ##Distancia
        soma_quad = 0
        for i in range (len(u)):
            soma_quad = soma_quad + (u[i] - v[i])**2
            i = i + 1
        dist = soma_quad**(1/2)
        print('A distãncia entre os vetores é igual {:.2f}'.format(dist))
dist(u, v)

##Normas = comprimento do vetor em relação a origem
print(np.linalg.norm(u))
print(np.linalg.norm(v))

##Representação Geométrica
import matplotlib.pyplot as plt
m = ([4,5])
p = ([-2,5])
soma = []
for i in range(len(m)):
    soma.append(m[i]+p[i])
    i = i + 1
print(soma)

v= np.array([m, p , soma])
origin = np.array([[0,0,0],[0,0,0]])# Origem dos vetores
plt.quiver(*origin, v[:,0],v[:,1], color=['r', 'b', 'y'], scale=35)
plt.show()
