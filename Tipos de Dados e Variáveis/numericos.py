"""
Tipos numéricos:
int -> inteiro
float -> ponto flutuante
conplex -> complexos

operadores:
+    soma
-    subtração
*    multiplicação
/    divisão
//   parte inteira da divisão
%    módulo
**   exponenciação
>    comparação maior
<    comparação menor
>=   comparação maior ou igual
<=   comparação menor ou igual
==   igual
!=   diferente

Podemos separar unidades numéricas com underline '_'
Ex.: 

print(1_000_000) #printa 1000000
print(4_4) #printa 44

num = num + 2 equivale a num += 2 
O mesmo pode ser feito para todos os outros operadores.

num = 2

num **= 3

print(num) #printa 8, ou seja, num = num ** 3
"""

#Obs,: casas decimais são separadas por ponto. Vírgulas separam componentes de estruturas de dados, como números em tuplas ou listas.

num = 1
print(type(num))
print(type(num + 1.0))  #tipos numéricos diferentes podem ser convertidos entre si em operações numéricas