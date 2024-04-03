"""
Funções em python podem ter parâmetros posicionais obrigatórios (arguments), 
opcionais com valor padrão ou (keyword arguments),
ou de múltiplos valores de ambos os tipos: *args (múltiple arguments) e **kwargs (multiple keyword arguments)

Keyword arguments (opcionais com valor padrão) não podem preceder arguments (posicionais obrigatórios)!
Parâmetros de múltiplos valores não devem preceder parâmetros únicos!

Ordem correta:

arg1, ..., argn, *args, kwarg1, ..., kwargn, **kwargs
"""

def func(teste1,teste2,*args,teste3=None,**kwargs):
    """Exemplo de documentação de função: 
    func testa os diferentes tipos de parâmetros estudados"""
    print(teste1,teste2)
    print(args)
    print(teste3)
    print(kwargs)

func(1,2,3,4,5,6,7,teste3 = 'teste3', a = 2, b = 4)
print(func.__doc__)
