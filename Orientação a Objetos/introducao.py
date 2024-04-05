"""
Classe - representa molde de objeto, ou seja, molde para uma abstração de algo do mundo real
    Atributos (variáveis/características associadas ao objeto)

    Métodos (funções/comportamentos de onjetos)
        Construtores: métodos que criam objetos

Objeto: Instância de uma classe
"""

class Classe:
    nome = "" #não recomendado
    pass #palavra reservada para indicar que ainda não há implementação para algum bloco (loop, fução, atributo)

objeto = Classe()
objeto.nome = "Joao"

print(objeto.nome)