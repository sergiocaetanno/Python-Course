"""
Funcionam como vetores ou matrizes em outras linguagens.
São coleções dinâmicas de tipagem fraca (sem tipo definido de dados/sem tamanho definido).


print(list(range(11)))
print(list("String"))

#Funções:

print(dir(list))


__add__', '__class__', '__class_getitem__', '__contains__', '__delattr__', '__delitem__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__',
'__getattribute__', '__getitem__', '__getstate__', '__gt__', '__hash__', '__iadd__', '__imul__', '__init__', '__init_subclass__', '__iter__', 
'__le__', '__len__', '__lt__', '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__reversed__', '__rmul__', '__setattr__', 
'__setitem__', '__sizeof__', '__str__', '__subclasshook__', 'append', 'clear', 'copy', 'count', 'extend', 'index', 'insert', 'pop', 'remove', 'reverse', 'sort'


#Condicionais com lista

lista = [1,2,3,4,5]
valor = 2
if valor in lista:
    lista.remove(valor)
    print(lista)

Operações entre listas

lista1 + lista2 concatena os elementos das duas listas em uma nova lista ex.: [1,2] + [3,4] retorna [1,2,3,4]
lista1 * x      cria uma nova lista com x vezes os elementos da lista 1 concatenados

Podemos percorrer listas assim como percorremos outros iteráveis na forma indexada: 
lista[valor inicial:valor final+1:passo] ex.: lista1[0,11,2] (percorre a lista de 0 a 10 de dois em dois elementos)

lista = [[0,1,2],[3,4,5,11],[6,7,8,17],[9,10,11,0,0,0],[12,13,14,12,12,12,12]]

for i in range(lista.__len__()):
    print('')
    for j in range(lista[i].__len__()):
        print(f'{lista[i][j]} ', end="")

"""

#podemos utilizar as funções sum, min, max para encontrar valores máximos, mínimos ou o somatório de valores de um iterável
        
lista = [[0,1,2],[3,4,5,11],[6,7,8,17],[9,10,11,0,0,0],[12,13,14,12,12,12,12]]

print(sum(lista[0]))
print(max(lista[0]))
print(min(lista[0]))

#OBS.: LISTAS SÃO PASSADAS POR REFERÊNCIA. PARA COPIAR UMA LISTA PARA OUTRA VARIÁVEL DEVE-SE UTILIZAR LISTA.COPY()

lista1,lista2,lista3,lista4,lista5 = lista #desempacotamento
print(lista3) 



