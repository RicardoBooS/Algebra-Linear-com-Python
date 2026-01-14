import numpy as np
import pandas as pd
import scipy as sp

##Importando a tabela para o Pyhton
nota = 'C:\\Users\\Ricardo\\PycharmProjects\\PythonProject1\\concurso.xlsx'
df = pd.read_excel(nota)
print(df.head())

#print(df.shape)
#print(df.dtypes)

A = df.drop(columns=['nota'])
A = A.values #Matriz dos Coeficientes
print(A)

#Matriz das constantes
b = df.drop(columns=['inicio_estudo','tempo_estudo_dia'])
b = b.values
print(b)