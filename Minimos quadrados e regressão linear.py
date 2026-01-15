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
#print(A)

#Matriz das constantes
b = df.drop(columns=['inicio_estudo','tempo_estudo_dia'])
b = b.values
#print(b)

##Estimativa por Minimos Quadrados
At = np.array(A).T # Transposta de A

#Multiplicação da transposta de A pela matriz A
AtA = np.dot(At,A)

#Matriz inversa de ATA
inv = np.linalg.inv(AtA)

#Transposta de b
Atb = np.dot(At,b)

x = np.dot(inv, Atb)
#print(x)

#x = np.dot(np.dot(np.linalg.inv(np.dot(At,A)),At),b) ## Mesma equação acima porém em apenas 1 linha

result = df

result['previsao'] = result['inicio_estudo']*x[0]+result['tempo_estudo_dia']*x[1]
#print(result)


#Erro médio absoluto
from sklearn.metrics import mean_absolute_error
mean_absolute_error(result.nota, result.previsao)

result['erro_abs'] = abs(result.nota - result.previsao)
#print(result)


#Regressão Linear Multipla

B = result.drop(columns=['nota','previsao', 'erro_abs'])

B = B.assign(unidade=1)

B = B[['unidade','inicio_estudo','tempo_estudo_dia']] #reformulando a ordem dos valores

Bt = np.array(B).T #Tramsposta de B

x2 = np.dot(np.dot(np.linalg.inv(np.dot(Bt,B)),Bt),b)
#print(x2)



result['previsao2'] = x2[0]+result['inicio_estudo']*x2[1]+result['tempo_estudo_dia']*x2[2]
#print(result)

##Erro médio absoluto
mean_absolute_error(result.nota, result.previsao2)

result['erro_abs2'] = abs(result.nota - result.previsao2)
print(result)

#Criação de um modelo matemático com regressão linear
import statsmodels.formula.api as smf
import statsmodels.stats.api as sms

modelo = smf.ols('nota ~ inicio_estudo + tempo_estudo_dia',data=df).fit()
print(modelo.summary())
