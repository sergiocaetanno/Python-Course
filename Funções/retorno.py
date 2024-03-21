#Funções podem retornar um conjunto de valores utilizando uma tupla

from random import randint

def sorteia3(lista = []):
    if(isinstance(lista, list) and lista.__len__()!=0):
        a = lista[randint(0,lista.__len__()-1)]
        lista.remove(a)
        b = lista[randint(0,lista.__len__()-1)]
        lista.remove(b)
        c = lista[randint(0,lista.__len__()-1)]
        return a,b,c

        
print(sorteia3([1,2,3,4,5,6,7,8,9,10]))