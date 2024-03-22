#Funciona como as list comprehensions.

dicionarioTeste = {'lucas':6, 'Yolanda':2}


dicionario1 = {chave:valor for chave,valor in dicionarioTeste.items() if valor >= 6 }
dicionario2 = {chave:valor if valor >=6 else 'reprovado' for chave,valor in dicionarioTeste.items()}

print(dicionario1)
print(dicionario2)