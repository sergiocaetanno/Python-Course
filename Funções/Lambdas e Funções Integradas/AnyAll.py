#All verifica se todos os elementos de um iterável são verdadeiros e Any se algum elemento é verdadeiro


lista = [-2,-4,1,2]

print(all([num>0 for num in lista]))


print(any([num>0 for num in lista]))