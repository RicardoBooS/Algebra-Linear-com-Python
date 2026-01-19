import numpy as np

A = np.array([[3,0],[0,1]])

autovalor, autovetor = np.linalg.eig(A)

print('O autovetor {:.3f} está associado aos autovetores {:.3f}'.format(autovalor[0],autovetor[0][0],autovetor[1][0]))
print('O autovetor {:.3f} está associado aos autovetores {:.3f}'.format(autovalor[1],autovetor[0][1],autovetor[1][1]))

B = np.array([[4,-3],[2,-1]])

autovalor1, autovetor1 = np.linalg.eig(B)

print('O autovalor {:.3f} está associado aos autovetores {:.3f} e {:.3f}'.format(autovalor1[0],autovetor1[0][0],autovetor1[1][0]))
print('O autovalor {:.3f} está associado aos autovetores {:.3f} e {:.3f}'.format(autovalor1[1],autovetor1[0][1],autovetor1[1][1]))