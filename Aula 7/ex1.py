# Exiba os números pares de 0 até um número solicitado pelo usuário

y = int(input("Informe um numero: ")) # input é uma função pq recebe e retorna
# input sempre traz string; Input() é função pois retorna algo,
# senão retorna(void) chama-se procedimento;
# Python é fortemente tipado por isso int p/ encaixar no fo

# for x in range (0,y):
#     if(x % 2 == 0):
#         print(x)

#OU:

for x in range (0,y,2):  # o 2 aqui seria o passo 2
        print(x)

#Essas duas formas de escrever o for, é um ponto de Expressividade da LP
#Se fosse usado um suporte a abstração de processos ou dados,
#como por ex: struct, union, seria um ponto de Capacidade de Escrita da LP

# Saída:
# Informe um numero: 10
# 0
# 2
# 4
# 6
# 8

# for x in range(0,3):  # 3 não entra, só 0, 1, 2.
#     print(x)
#
# Saída:
# Informe um numero: 10
# 0
# 1
# 2

# for c in "UNISANTOS": # string é imutavel, toda vinculação troca de endereço
#     print(c)
#
#Saída:
# U
# N
# I
# S
# A
# N
# T
# O
# S

