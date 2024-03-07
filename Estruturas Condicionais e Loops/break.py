"""
Podemos utilizar break para sair de loops quando a linha break é alcançada.
"""

while True:
    sair = input('Digite "sair" para sair:')
    if sair.__eq__('sair'):
        break