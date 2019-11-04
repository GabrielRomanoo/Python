# 2. Aplicando o Paradigma Funcional
# b. Entre com uma sequencia de números inteiros na mesma linha, exiba a soma somente
# dos números pares da sequencia digitada.

x = list(map(int,input().split()))

pares = list(filter(lambda y: not y % 2, x))

#print(pares)

print(sum(pares))

#SAÍDA:
#1 2 3 4
#6


