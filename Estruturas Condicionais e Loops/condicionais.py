#if, elif e else são estruturas que trabalham com os operadores (and, or, is, >, <, ==, !=, >=, <=), funções como __eq__ e tipos booleanos (True e False) como segue:

nome = 'serg'
sobrenome = 'Mentos'
idade = 17

if nome == 'serg' and sobrenome.__eq__('caetano'):
    print('Usuário correto')
elif idade >= 18:
    print("Realize o seu cadastro!")
else:
    print("Acesso negado!")

print(False is False)