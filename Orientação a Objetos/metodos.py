#Métodos são funções associadas a objetos ou classes
#Assim como em atributos, convencionamos métodos privados como aqueles começados com __
#Métodos privados só podem ser acessados dentro da classe
#Podem ser métodos de INSTÂNCIA, métodos de CLASSE (decorador @classmethod) ou métodos ESTÁTICOS (decorador @staticmethod)
#Métodos de INSTÂNCIA recebem self como o primeiro parâmetro e não acessam atributos de classe (self se refere a própria instância do objeto)
#Métodos de CLASSE recebem o decorador @classmethod e cls como o primeiro parâmetro. Podem acessar atributos de classe por meio do cls. (cls se refere a própria classe)
#Métodos ESTÁtICOS recebem o decorador @staticmethod e não utilizam o primeiro parâmetro predefinidamente. Não acessam atributos de classe.


class Contador:
    __contador = 0

   
    def __init__(self):
        Contador.__contador +=1

    @staticmethod
    def boasVindas():
        print("Bem vindo a classe Contador!")

    @classmethod
    def printaContador(cls):
        print(cls.__contador)
  
    



a = Contador()
b = Contador()
c = Contador()
d = Contador()
e = Contador()
f = Contador()

Contador.boasVindas()
Contador.printaContador()







