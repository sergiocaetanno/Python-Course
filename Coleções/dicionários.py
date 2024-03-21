"""
Tipo de dado não indexado que agrupa conjuntos chave:valor
É delimitado por chaves.
"""

#inicialização

dicionario = dict(chave1= "valor1", chave2= "valor2") 

#ou

dicionario = {'chave1':'um', 'chave2':2}

#print(dicionario.get('chave3'))

#qualquer tipo de dado hashble (imutável) pode ser utilizado como chave de dicionário

tuple1 = (1,2,3)
dicionario1 = {tuple1: "teste"}

if tuple1 in dicionario1:
    print(dicionario1.get((1,2,3)))
