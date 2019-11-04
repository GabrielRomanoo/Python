#  Faça uma função que retorne a quantidade de
# espaços presentes em uma string.
from functools import reduce


x = 'Universidade Catolica de Santos'

espaco = list(filter(lambda s: s==' ', x))

#filter(funcao, sequencia)
#Retorna lista que pode ser de tamanho diferente da
#sequencia original. Retorna na verdade um objeto
#iterator, que deve ser convertido para uma list,
#utilizando o list()

#(lambda x,y : x+y)(1,2)
#Resultado 3

print(espaco)

espaco = len(espaco)

print(espaco)

#SAÍDA:
#[' ', ' ', ' ']
#3





