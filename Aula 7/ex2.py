# Crie um programa para calcular as 4
# operações básicas (usando funções).
# As opções são 1-somar, 2-subtrair,
# 3-multiplar, 4-dividir, 5-sair

def soma(a,b): # a e b são parametros formais
    return a + b
#Se não tivesse feito a conversão para int no while
# essa função usaria do polimorfismo (dados ou subprogramas(funções ou procedimentos) com o mesmo
#identificador mas com tipos ou logicas diferentes
#No polimorfismo, é possível fazer sobrecarga, principalmente em funções
#Sobrecarga: Rescrever o mesmo método: def soma(a,b) -> exemplo: rescrever a função para int, float, etc

def subtrair(a,b): # a e b são parametros formais
    return a - b

def multiplicar(a,b): # a e b são parametros formais
    return a * b

def dividir(a,b): # a e b são parametros formais
    return a/b

x = 10

while(x != 5):
    x = int(input("1-somar, 2-subtrair, 3-multiplar, 4-dividir, 5-sair, Opção: "))
    if(x != 5):
        print("Informe dois valores: ")
        a = int(input())
        b = int(input())
        if(x == 1):
            print("Resultado: ", soma(a= a,b = b))
        #     a e b são parametros reais, usando uma chamada nominal
        if(x == 2):
            print("Resultado: ", subtrair(a,b))
        #     a e b são parametros reais, usando chamada usando parametro posiconal
        if(x == 3):
            print("Resulado: ", multiplicar(a,b))
        #     a e b são parametros reais, usando chamada usando parametro posiconal
        if(x == 4):
            print("Resulado: ", dividir(a, b))
        #     a e b são parametros reais, usando chamada usando parametro posiconal



