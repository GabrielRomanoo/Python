# 1. Aplicando o Paradigma Imperativo
# a) Usuário deve entrar com uma sequencia numérica de inteiros em uma linha, exiba na
# tela qual o maior, qual o menor, e calcule a média aritmética dos valores.

x = input("Entre com uma sequencia numérica de inteiros: ")

x = x.split()

#poderia ser direto: x = input("Entre com uma sequencia numérica de inteiros: ").split()

#split transforma a string x em uma lista, com cada elemento da lista sendo uma string
#print(x)

x = list(map(int,x))

# o map pega cada elemento da lista x e transforma em int

media = sum(x)/len(x)

#sum(x) retorna a soma dos elementos da lista
#len(x) retorna o tamanho da lista

print("O maior deles: ", max(x))
print("O maior deles: ", min(x))
print("A media aritmetica deles: ", media)

#max(x) retorna o maior da lista
#min(x) retorna o menor da lista

#SAIDA:
#Entre com uma sequencia numérica de inteiros: 1 2 3 4 5 6
#O maior deles:  6
#O maior deles:  1
#A media aritmetica deles:  3.5


