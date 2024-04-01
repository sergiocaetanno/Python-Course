"""
Iterables (iteráveis): coleções ou objetos que podem ser percorridos, elemento a elemento, por meio de um Iterator. Esse iterador é criado com o método iter(iterable)
Iterator (iteradores): objeto que fornece a funcionalidade de percorrer um iterável elemento a elemento por meio da função next(iterator).

Generator(geradores): Iterador criado por meio de uma Expressão Geradora. Um exemplo de expressão geradora é o "yield" que atua como um "return", porém, esperando que
uma função next() seja chamada para que esse retorno ocorra. Diferentemente do return, o yield não abandona um laço de repetição ou escopo ao ser executado, tendo a sua
execução repetida até que outra expressão intervenha (break, return, etc).

Um generator pode ser criado utilizando-se da sintaxe de uma list comprehension no formato de tupla. Ex.: (num for num in range(10)) retorna um generator com os elementos de 0 a 9.
"""

#Exemplos de iteradores e geradores em uso são apresentados na seção de Funções, no módulo sobre Lambdas e Funções integradas