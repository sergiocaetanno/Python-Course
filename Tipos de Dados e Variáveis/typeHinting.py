#Type Hinting ou Insinuamento de Tipos: ferramenta que oferece a explicitação sugestiva de tipos
#Não proíbe a utilização de tipos diferente das sugeridas pelo Hinting
#Ferramenta utilizada para situar desenvolvedores, mas não restringe a capacidade da tipagem dinâmica

def recebeInteiro(parametro:int=2) -> tuple:
    return parametro,type(parametro)

#type hinting define o tipo esperado para parâmetros e retornos em funções python
#é representado por ":tipo" e "-> tipo" como exemplificado acima

a,b = recebeInteiro(1)

print(a)
print(b)

a,b = recebeInteiro('a')

print(a)
print(b)

####### MYPY #######

#PODEMOS UTILIZAR: pip install mypy
#Esse comando instala o checador de tipos mypy, que pode ser utilizado como segue:
#No terminal digite: mypy file.py
#O mypy irá considerar como erro quando um tipo errado for passado para uma uma função com Type Hint
