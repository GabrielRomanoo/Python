#coding: latin-1
#fun��o que recebe dois fatores de qualquer tipo e retorna o resultado em uma string


#  Altere a fun��o multiplicar do slide 6,
# para que retorne o produto sempre do
# mesmo tipo do fator1

#Esses s�o os parametros formais
def multiplicar(fator1,fator2):
    if type(fator2) == str:
            fator2 = float(fator2)
    if type(fator1) == str:
            fator1 = float(fator1)
            produto = fator1 * fator2
            return str(produto)
    if type(fator1) == float:
            produto = fator1 * fator2
            return float(produto)
    if type(fator1) == int:
            fator1 = float(fator1)
            produto = fator1 * fator2
            return int(produto)

numero1 = input("Entre com o primeiro fator..: ")
print(type(numero1))
numero2 = input("Entre com o segundo fator..: ")
print("Resultado...:"+ multiplicar(numero1,numero2))
print("Resultado de 10 * 50...: ", multiplicar(10,50))
print("Resultado de 10.5 * 4..: ", multiplicar(10.5,4))
#Esses s�o os parametros reais posicionado

# 1)Comentar quais parametros formais e quais reais
# 2)Identificar passagem por parametro ou referencia
#Resp: Todos s�o por parametro
# 3)Sua fun��o � polimorfica ou monomorfica?
#Resp: Polimorfico

