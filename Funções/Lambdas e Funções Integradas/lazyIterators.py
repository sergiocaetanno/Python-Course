#Iteradores preguiçosos como os iteradores retornados pelas funções map(), filter() e reduce() são iteradores que
#não geram a lista de resultados de uma só vez, mas sim passo a passo, à medida que são iterados. 
#Após realizar algum processamento de dados com lazy iterables, eles são removidos da memória

#O que se assemelharia a Tuple Comprehensions cria os generators, ou seja, um conjunto iterável cujos elementos são apagados da memória após um processamento qualquer

#Exemplo

lista1 = [1,2,3]
lista2 = [3,4]
lista3 = [1,2,3,4,5]

a = zip(lista1,lista2,lista3)

for i in a:
    print(i)

if list(a).__len__() == 0:
    print("Elementos de 'a' removidos da memoria")

#Generator:
    
a = (num for num in range(10))

print(f'\n\n{type(a)}')
for i in a:
    print(type(i))
    print(i)
    
#print([i for i in a])   #<------ é apagado da memória