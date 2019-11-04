# 2.Dados 2 números naturais p e q,
# calcule o valor se p≥q, ou
#  caso contrário.
# p !
# q ! p−q !
# q !
# p! q−p !

# def fatorial(n):
#     for i in range(n, 1, -1):
#         n = n * (i - 1);
#     return n

def fatorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        n = n * fatorial(n-1)
    return n;

# a = int(input())
# print(fatorial(a))

p = int(input())
q = int(input())

def calcular(p,q):
    if p > q:
        return fatorial(p)/(fatorial(q)*(fatorial(p-q)))
    else:
        return fatorial(q) / (fatorial(p) * (fatorial(q - p)))

print(calcular(p,q))

#SAÍDA:
#5
#10
#252.0