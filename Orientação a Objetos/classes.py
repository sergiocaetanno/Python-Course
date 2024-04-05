"""
Nomes de classe tem iniciais em maiúsculo

Em python arquivos podem ter nomes não relacionados às classes e diversas classes por arquivo, o que não acontece em Java por exemplo. 

Atributo:
    -Atributos de Instância: São declarados dentro do método construtor;
    -Atributos de Classe;
    -Atributos Dinâmicos;

"""

class Construtores:
    def __init__(self, nome = "nome") -> None:
        self.nome = nome

a = Construtores()


print(a.nome)
