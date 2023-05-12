# cont = 0
# notas = [[5, 2, 8], [6, 9, 4], [10, 9, 7]]
# for i in range(len(notas)):
#     for j in range(len(notas[i])):
#         if notas[i][j] >= 6:
#             cont = cont + 1 #cont+=1
#             #print(notas[i][j])
# print("Alunos aprovados:", cont) 

#in procura dentro do vetor /retorna booleano
# c=[5,4,8,9]
# elem=4
# if elem in c:
#     print("4 esta em c")
# else:
#     print("nao esta")
# print(elem in c) #True

#FUNÇÕES

import operacoe #import soma_elementos, encontra_min_max # import *

a=[5, -2, 4, 8]
print("min e max:", operacoe.encontra_min_max(a)) #operacoes.enco..
print("soma:", operacoe.soma_elementos(a))