#Semelhantes a listas, porém, imutáveis. Sua definição é realizada com um conjunto de valores de qualquer tipo, necessariamente separados por vírgulas.
#São delimitadas por parêntesis, contudo, esses podem ser emitidos em algumas situações, como no desempacotamento de iteráveis.

x = um, dois, três, quatro, cinco, seis  = ("um","dois","três","quatro") + (1, 2)

print(um, cinco)
print(type(um))
print(type(cinco))
print(type(x))

#tuplas são imutáveis, mas podem ser sobrescritas

tupla = 1, 2
tuplas = 3, 4

print(tuplas) #não podemos alterá-la por meio de operações ou métodos associados a tuplas