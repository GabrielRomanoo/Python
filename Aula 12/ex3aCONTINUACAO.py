from ex3a import *

x = list(map(int,input().split()))

dp = Numeros(x) #instanciou o objeto

print(dp.Maior())
print((dp.Menor()))

#SAIDA:
#1 2 3 4
#4
#1