##Função lambda e map

##geralmente como argumentos para outras funções de ordem superior (que aceitam outras funções como parâmetro).

##(Map = é uma função de ordem superior (ou seja, ela aceita outra função como argumento) que tem o objetivo de aplicar uma determinada
##função a cada item de um iterável (como uma lista) e retornar um novo iterável com os resultados.)

L = [4,5,6,7,11,9,10]
areas = list(map(lambda x: x**2, L))
print(areas)
