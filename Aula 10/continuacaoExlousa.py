from exlousa import *

x = int(input("Quantos Dispositivos ? "))

contador = 0

dp = []

while (contador < x):
    print("Qual é o Dispositivo ? ")
    op = int(input("1-Smartphone 2-Tablet 3-PC"))
    if op == 1:
        ip = input("Informe o ip: ")
        l = int(input("Esta ligado? "))
        ap = int(input("Qual é a aplicação? 0-Netflix; 1-CandyCrush;2-Youtube"))
        dp.append(SmartPhone(ip,l,ap))
    if op == 2:
        ip = input("Informe o ip: ")
        l = int(input("Esta ligado? "))
        ap = int(input("Qual é a aplicação? 0-Netflix; 1-CandyCrush;2-Youtube"))
        dp.append(Tablet(ip,l,ap))
    if op == 3:
        ip = input("Informe o ip: ")
        l = int(input("Esta ligado? "))
        ap = int(input("Qual é a aplicação? 0-Netflix; 1-CandyCrush;2-Youtube"))
        dp.append(PC(ip,l,ap))

    contador = contador + 1

consumo = 0

for x in dp:
    consumo = x.getConsumo() + consumo

print("O consumo total é: ",consumo)

#Quantos Dispositivos ? 1
#Qual é o Dispositivo ?
#1-Smartphone 2-Tablet 3-PC1
#Informe o ip: 255
#Esta ligado? 1
#Qual é a aplicação? 0-Netflix; 1-CandyCrush;2-Youtube0
#O consumo total é:  300