"""
Casts, ou conversões de dados de um tipo para o outro podem ser realizados.

Podemos converter um dado de String para Inteiro como segue o exemplo.
"""

palavra = "100"

print(type(palavra + 1)) #somar um numero à variável palavra nesse momento do código retorna um erro
print(type(int(palavra) + 1)) #nesse momento do código o mesmo não retorna erro