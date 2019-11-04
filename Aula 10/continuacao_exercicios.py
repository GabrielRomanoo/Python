from exercicios import *

im1 = Imovel(2460756,100.0,5000.0)
im2 = Imovel(5598271,150.0,7000.0)

cs1 = Casa(123456,100.0,2500.0,80.0,1000.0)
cs2 = Casa(123458,150.0,3000.0,100.0,1500.0)
cs3 = Casa(123459,200.0,3500.0,120.0,2000.0)

imoveis = [im1,im2,cs1,cs2,cs3]

contador = 0.0

for p in imoveis:
    print(p.calcularIPTU()) #INSTACIANDO O OBJETO
    contador = p.calcularIPTU() + contador

print(contador)

#SAIDA:
#500000.0
#1050000.0
#330000.0
#600000.0
#940000.0
#3420000.0
