"""
Métodos que podem ser utilizados para iterações e loops.
Obs.: multiplicar iteráveis por um valor numérico x resulta no mesmo tipo de iterável com x vezes os valores do iterável inicial concatenados.
Ex.: [1,2,3] * 2 resulta em [1,2,3,1,2,3,1,2,3]
Vale para outros iteráveis!
"""


"""nome = "teste"
for i,j in enumerate(nome):
    print(j)

print("\n")
for i,j in enumerate(nome):
    print(i)
"""


#enumerate(iterável) retorna um conjunto de tuplas contendo, cada tupla, um índice e o valor do iterável correspondente
    
for i,j in enumerate(['zero','um','dois','três','quatro']):
    print(j)

#range(y) ou range(x,y) ou range(x,y,z) cria uma estrutura iterável numérica que vai de 0 à y-1, ou de x à y-1. O parâmetro z define o passo dessa estrutura (um em um, dois em dois...)
print(range(1,5).__len__())
print(range(5).__len__())

for i in range(0,10,2):
    print(i)

print([1,2,3]*3)