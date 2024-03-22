#Utilizam geradores para criar listas com uma sintaxe simples

lista = [int(i) for i in "123456789" if not int(i) % 2 != 0]

print(lista)

#A comprehension aplica um processamento de dados para cada elemento de um iterável
#Esse processamento pode ser ou não acompanhado por uma estrutura condicional simples 'if'

#Podemos utilizar uma estrutura condicional composta 'if else', posicionando-a antes do iterável como segue:

lista = [int(i) if not int(i) % 2 != 0 else 'impar' for i in "123456789"]

print(lista)

#OBS.: podemos utilizar comprehensions para criar listas aninhadas

aninhada = [[i+1 for i in range(3)] for i in range(10)]
print(aninhada)