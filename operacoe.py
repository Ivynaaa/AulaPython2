def encontra_min_max(elementos): #def define função
    min= float("inf") 
    max= float("-inf") 
    for i in range(len(elementos)):
        if elementos[i]< min:
            min=elementos[i]
        if elementos[i]>max:
            max=elementos[i]
    return (min, max) 
a= [5,8,-2,4,8]
print("Menor e maior elemento de a:", encontra_min_max(a))# (-2,8)tupla  a[1]
(min, max)=encontra_min_max(a)
print(min, max)

def soma_elementos(elementos):
    soma=0
    for i in range(len(elementos)): #for i in elementos:
        soma=soma + elementos[i]    #soma=soma+ i
    return soma

a=[2,2]
print("soma: ",soma_elementos(a))