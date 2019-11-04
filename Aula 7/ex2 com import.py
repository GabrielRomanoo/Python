# Crie um programa para calcular as 4
# operações básicas (usando funções).
# As opções são 1-somar, 2-subtrair,
# 3-multiplar, 4-dividir, 5-sair


import funcoes # Tem que estar no mesmo diretório

x = 10

while(x != 5):
    x = int(input("1-somar, 2-subtrair, 3-multiplar, 4-dividir, 5-sair, Opção: "))
    if(x != 5):
        print("Informe dois valores: ")
        a = int(input())
        b = int(input())
        if(x == 1):
            print("Resultado: ", funcoes.soma(a= a,b = b))
        #     a e b são parametros reais, usando uma chamada nominal
        if(x == 2):
            print("Resultado: ", funcoes.subtrair(a,b))
        #     a e b são parametros reais, usando chamada usando parametro posiconal
        if(x == 3):
            print("Resulado: ", funcoes.multiplicar(a,b)) #usa funcoes.multiplicar para indicar que é no arquivo funcoes
        #     a e b são parametros reais, usando chamada usando parametro posiconal
        if(x == 4):
            print("Resulado: ", funcoes.dividir(a, b))
        #     a e b são parametros reais, usando chamada usando parametro posiconal