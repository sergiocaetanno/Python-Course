#Atributos de classes podem ser públicos ou privados
#Utiliza-se o duplo underscore __ no início de atributos para convencioná-los como privados

class Lampada:
    def __init__(self,estado = 'desligada'):  #A palavra self é uma convenção utilizada para passar o próprio objeto como primeiro parâmetro para seus métodos
        self.__estado = estado
        self.voltagem = '220V'

    def getEstado(self):
        return self.__estado


lamp = Lampada()

print(lamp.getEstado())
print(lamp.voltagem)

#Podem ser criados e excluidos atributos dinâmicamente, estes sendo atributos apenas de instância, mas não de classe.
#Não é recomendado!

# lampadaLed = Lampada()

# lampadaLed.cor = 'vermelho'

# print(lampadaLed.cor) #não é comum o fazer. Por isso verificadores de sintaxe podem apontar como erro

# del lampadaLed.cor

# print(lampadaLed.cor)