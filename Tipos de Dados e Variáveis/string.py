#Uma string é uma cadeia de caracteres. É representada entre aspas simples, duplas, simples triplas ou duplas triplas. Nesse último caso preserva quebra de linha. 
#Não há o tipo caractere em python!
#\n representa a quebra de linha

"""
nome = '''Angelina
Jolie'''

print(nome)

nome = "Angelina \nJolie"

print(nome)

Funções que podem ser aplicadas a strings:

print(dir(str))

__sizeof__()
capitalize()
format()
index()
lower()
upper()
split()

help(str.split) #...
"""

#Obs.: uma string em python é uma lista de caracteres. 

nome = "Serg"
print(nome[0])

#Podemos percorrer uma string da seguinte forma nome[valorInicial:valorFinal:x] -> percorre a string de i = valorInicial até i < valorFinal no passo p = x. Por padrão p é 1. 
#Essa operação se chama Slice de Strings. Ocultar valores implica em percorrer a string até aquele o seu fim.

print("Teste"[0:3:1])
print("Teste"[::2])
print("Teste"[::-1])

