#retorna uma lista ordenada
lista = [5,4,3,2,1]

lista.sort()

print(lista)

#Diferentemente da função .sort(), a sorted() ordena um iterável passado e retorna uma lista, não alterando seu parâmetro

lista = [5,4,3,2,1]
print(sorted(lista))
print(lista)