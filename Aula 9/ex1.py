# Faça uma função que recebe uma lista de strings, e
# retorna uma lista com todas essas strings com a
# primeira letra em maiúsculo (capitalize())

lista = ['gabriel','romano']

string = list(map(str.capitalize,lista))

print(string)

#map(funcao, sequencia)
#Retorna uma lista modificada pela aplicação da
#função. Retorna na verdade um objeto iterator,
#que deve ser convertido para uma list,
#utilizando o list()

#SAÍDA:
#['Gabriel', 'Romano']
