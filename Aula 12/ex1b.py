# 1. Aplicando o Paradigma Imperativo
# b. Entre com uma sequencia de no mínimo 5 números reais, calcule a média ponderada,
# utilizando 0.3 para os dois primeiros valores e para os dois últimos valores, e a 0.1 para
# os valores intermediários, exiba o resultado.

x = list(map(int,input().split()))

primeiros = []

for i in range(0,2):
    #print(i)
    primeiros.append(x[i])

print("Primeiros: ", primeiros)

ultimos = []

for i in range(len(x) - 2, len(x)):
    #print(i)
    ultimos.append(x[i])

print("Ultimos: ", ultimos)

meio = []

for i in range(2, len(x) - 2):
    #print(i)
    meio.append(x[i])

print("Numeros do meio: ", meio)

for i in range(0,2):
    #print(i)
    primeiros[i] = primeiros[i] * 0.3

print("Primeiros: ", primeiros)

for i in range(0,2):
    #print(i)
    ultimos[i] = ultimos[i] * 0.3

print("Ultimos: ", ultimos)

for i in range(0, len(meio)):
    #print(i)
    meio[i] = meio[i] * 0.1

print("Numeros do meio: ", meio)

todos = []

for i in range(0,2):
    todos.append(primeiros[i])

for i in range(0, len(meio)):
    todos.append(meio[i])

for i in range(0,len(ultimos)):
    todos.append(ultimos[i])

#print(todos)

media = sum(todos)/len(todos)

print(media)

#SAÍDA:
#1 2 3 4 5
#Primeiros:  [1, 2]
#Ultimos:  [4, 5]
#Numeros do meio:  [3]
#Primeiros:  [0.3, 0.6]
#Ultimos:  [1.2, 1.5]
#Numeros do meio:  [0.30000000000000004]
#0.78

