#coding : latin-1

from pessoa import *

pf1 = PessoaFisica("Joao", "12/12/2012", "234.567.345-X")
pf2 = PessoaFisica("Maria", "01/01/2011", "233.345.566-1")

pj1 = PessoaJuridica("Padaria do Manoel", "12/12/1890", "001.001.345/1234-0","0013003")
pj2 = PessoaJuridica("Oficina do José", "01/09/1980", "010.011.112/1233-2", "0993045")

pessoas = [pf1,pj1,pf2,pj2]

for p in pessoas: #laço que pratica o polimorfismo
	p.exibir()
