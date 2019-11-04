# 2. Aplicando o Paradigma Funcional
# a) Usuário deve entrar com uma sequencia numérica de inteiros, e deve exibir na telas duas
# linhas, uma linha com os números ímpares, e outra linha com os pares.

x = list(map(int,input("Entre com uma sequencia numérica de inteiros: ").split()))

impares = list(filter(lambda y: y % 2, x))

#y % 2 retorna 0 ou 1, ou seja, false ou true, entao se for impar ele vai retornar 1

print("Impares: ", impares)

pares = list(filter(lambda y: not y % 2, x))

#y % 2 retorna 0 ou 1, ou seja, false ou true, entao se for impar ele vai retornar 1

print("Pares: ", pares)

#SAÍDA:
#Entre com uma sequencia numérica de inteiros: 1 2 3 4 5
#Impares:  [1, 3, 5]
#Pares:  [2, 4]
