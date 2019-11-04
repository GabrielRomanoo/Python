#coding : latin-1

class Pessoa(object):
	__nome = " "
	__data_nascimento = " "

	def __init__(self, n, data): #construtor
		self.__nome = n
		self.__data_nascimento = data

	def exibir(self):
		print("Nome...: "+self.__nome) #self ta indicando que é o atributo da classe
		print("Data Nascimento..: "+self.__data_nascimento)

class PessoaFisica(Pessoa):  #pessoa é uma referencia nessa linha
	__cpf = ""

	def __init__(self, n, data, n_cpf):
		Pessoa.__init__(self,n,data)
		self.__cpf = n_cpf

	def exibir(self):
		Pessoa.exibir(self)
		print("CPF...: "+self.__cpf)

class PessoaJuridica(Pessoa):
	__cnpf = ""
	__inscricao_estadual = " "

	def __init__(self, n, data, n_cnpj, n_ie):
		Pessoa.__init__(self,n,data)
		self.__cnpj = n_cnpj
		self.__inscricao_estadual = n_ie

	def exibir(self):
		Pessoa.exibir(self)
		print("CNPJ...: "+self.__cnpj)
		print("Inscrição Estadual...: "+self.__inscricao_estadual)

'''
p1 = Pessoa("João","01/04/1999")
p2 = Pessoa("Maria","01/01/2001")
p1.exibir()
p2.exibir()
'''
'''
pf1 = PessoaFisica("Joao", "12/12/2012", "234.567.345-X")
pf1.exibir()
'''
'''
pj1 = PessoaJuridica("Padaria do Manoel", "12/12/1890", "001.001.345/1234-0","0013003")
pj1.exibir()
'''