import numpy as np
import pandas as pd

##Importação de data frame
massa = 'C:\\Users\\Ricardo\\PycharmProjects\\PythonProject1\\inspecao.csv'
df = pd.read_csv(massa,sep=';')
#print(df.head())


##Verificação de valores faltantes
#print(df.isnull().sum())

#Exclusão dos valores faltantes
df = df.dropna()

##Criação da matriz de covariancia
matriz = df.drop(columns=['amostra'])
matriz = matriz.values
#print(matriz)

#calculando a variancia
matriz_cov = np.cov(np.transpose(matriz)) #matriz transposta
#print(matriz_cov)

##Autovalores e Autovetores da covariancia
autovalor,autovetor = np.linalg.eig(matriz_cov)
print('O autovalor {:.3f} está associado aos autovetores {:.3f} e {:.3f}'.format(autovalor[0],autovetor[0][0],autovetor[1][0]))
print('O autovalor {:.3f} está associado aos autovetores {:.3f} e {:.3f}'.format(autovalor[1],autovetor[0][1],autovetor[1][1]))


#Taxa de Variancia explicada (EVR)
EVR = autovalor/np.sum(autovalor)
print(EVR)

