from functools import reduce
cubo = lambda x: x * x * x

soma = lambda  x,y: x + y #paradigma funcional

print(soma(2,3))

lista= [10,2]

isMaior10 = lambda x : x > [10]

# maiores10 = lambda  x : isMaior10(x)

print(isMaior10(lista))

print(sorted(lista)) #ordena crescente

print(sorted(lista,reverse=True)) #ordem decrescente

int_float = list(map(float,lista))

print(int_float)

int_float = list(map(cubo,lista))

print(int_float)

fatorial = lambda n : reduce(lambda x,y : x*y, range(1,n+1))

print(fatorial(3))

impares = list(filter(lambda x: x % 2, [1,2,3,4]))

print(impares)

pares = list(filter(lambda x: not x % 2, [1,2,3,4]))

print(pares)

maior5 = list(filter(lambda x: x > 5, [1,2,3,4]))

print(maior5)

#SAIDA:
#5
#True
#[2, 10]
#[10, 2]
#[10.0, 2.0]
#[1000, 8]
#6
#[1, 3]
#[2, 4]
#[]
