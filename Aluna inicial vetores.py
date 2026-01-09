##Aula inicial Vetores
import numpy as np
u = [2, -4, 1]
u = np.array(u)
print(type(u))  ##mostra o tipo do atributo
print(u.shape)  ##mostra a quantidade de atributos dentro da chave
v= np.array([3,2,-5])
print(u[0])  ##motra o número que está na posição 0 dentro da chave u
print(v[1])  ##motra o número que está na posição 1 dentro da chave v

##Soma de vetores
soma = u + v
print(soma)

##Produto Interno
prod_int = 0
for i in range(len(u)): ##len retorna a quantidade de variáveis presente na lista ex: u =[2, -4, 1] - retornará 3
    prod_int = prod_int + u[i] * v[i]
    i = i + 1
print(prod_int)

##Multiplicação por escalar
multi = 5*u
print(multi)
