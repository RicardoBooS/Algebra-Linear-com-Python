##Função para o calculo do teorema de Pitágoras

def pitagoras (cat1, cat2, hip):
    if hip == 'x':
        hip = (cat1**2 + cat2**2)**(1/2)
        print('A hipotenusa é ',hip)
    elif cat1 == 'x':
        cat1 = (hip**2 - cat2**2)**(1/2)
        print('O cateto é', cat1)
    elif cat2 == 'x':
        cat2 = (hip**2 - cat1**2)**(1/2)
        print('O cateto é', cat2)

pitagoras(13, 24, 'x')

## Otimização de listas

lista = [valor + 10 for valor in range(5)]
print(lista)

conceito = [('azul',nota) if nota >=6 else ('vermelho', nota) for nota in range(1,11)]
print(conceito)







