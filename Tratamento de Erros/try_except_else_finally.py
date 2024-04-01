"""
Try / Except / Else / Finally

Dica de quando e onde tratar código:

TODA ENTRADA DEVE SER TRATADA!

OBS: A função do usuário é DESTRUIR seu sistema.

# Else -> É executado somente se não ocorrer o erro.

# Finally

try:
    num = int(input('Informe um número: '))
except ValueError:
    print('Você não digitou um valor válido.')
else:
    print(f'Você digitou o número {num}')
finally:
    print('Executando o finally')


# OBS: O bloco finally é SEMPRE executado. Independente se houve exceção ou não.

# O finally, geralmente, é utilizado para fechar ou desalocar recursos.

"""


def dividir(a, b):
    try:
        a = int(a) / int(b)
    except (ValueError, ZeroDivisionError,TypeError) as err:
        return f'Ocorreu um problema: {err}'
    else: 
        return(a)
    finally:
        print("finally")


num1 = input('Informe o primeiro número: ')
num2 = input('Informe o segundo número: ')

print(dividir(num1, num2))

