# def encontra_menor(elementos): #def define função
#     menor= 9999999  #float("inf") ->infinito ou -inf menos infinito
#     for i in range(len(elementos)):
#         if elementos[i]< menor:
#             menor=elementos[i]
#     return menor #(menor, outro valor)
# a= [5,8,-2,4,0]
# print("Menor elemento de a:", encontra_menor(a))#chamada da função

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