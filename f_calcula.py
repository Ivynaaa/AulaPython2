#função que calcula a soma de todos os elementos de uma lista

def soma_elementos(elementos):
    soma=0
    for i in range(len(elementos)): #for i in elementos:
        soma=soma + elementos[i]    #soma=soma+ i
    return soma

a=[2,2]
print("soma: ",soma_elementos(a))