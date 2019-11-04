# Escreva uma função para calcular a hipotenusa de
# um triângulo retângulo, recebendo como
# parâmetros cateto oposto e cateto adjacente. Aceite
# apenas valores positivos.

import math

hipotenusa = lambda x,y: math.sqrt(x*x + y*y)

print(hipotenusa(3,4))

#SAÍDA:
#5

