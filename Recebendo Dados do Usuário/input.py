"""
Utilizamos para isso a função input()

help(input)

---
print("Digite seu nome: ")
nome = input()
print("Seja bem vindo, %s" %nome)

print("Digite a sua idade: ")
idade = input()

print("%s tem %s anos de idade" %(nome, idade))
---

Utilizamos o operador % para formatar strings com dados fornecidos. Exemplo:

print("String com percents %d %s %f" %(10, 'dez', 10.0))

%d -> número
%s -> cadeia de caracteres
%f -> número real
"""
#Formas mais recentes de formatar strings
nome = "Serg"
idade = 23

print("{0}: {1} anos!".format(nome, idade))
print(f"{nome}: {idade} anos!")              #mais atual


