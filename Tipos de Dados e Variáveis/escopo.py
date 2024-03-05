"""
Variáveis podem ser locais ou globais.

Variáveis tem o seu tipo inferido no momento de sua atribuição. Python é uma linguagem de tipagem dinâmica, ou seja, podemos reatribuir tipos a variáveis!

Locais: reconhecidas apenas no bloco onde foi declarada.

Globais: reconhecidas em todo o código.
"""

novo = 4
def func():
    novo = 2

print(novo)

func()
print(novo)

#Observamos que a variável local 'novo' dentro da função func é uma variável diferente da variável global 'novo'.