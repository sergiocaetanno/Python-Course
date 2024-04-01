"""
raise --> palavra reservada que lança exceções

Assim como o return, o raise finaliza a execução da função (nada abaixo do raise é executado)
"""



# def teste():
#     raise NameError

from ast import Name


try:
    test()
except: #trata erros genéricamente
    print("teste1")


try:
    test()
except NameError as err: #trata erros de forma específica
    print(err)