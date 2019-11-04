#  Crie uma classe Imovel, com os atributos: inscricao (inteiro),
# area (real), valor_m2 (real), e o método: calcularIPTU, que
# retorna a multiplicacao da area pelo valor_m2
#  Crie a classe Casa, filha de Imovel, com o atributo,
# area_construida (real) e taxa_construcao (real). Sobreescrever
# o método calcularIPTU, acrescentando a multiplicacao da
# taxa_construcao pela area_construida ao cálculo normal de
# um imóvel.
#  Crie 2 objetos Imóvel, 3 objetos casa, coloque-os em uma
# lista, informe o valor de IPTU de cada objeto, e a somatória
# total dos IPTUs de todos os imóveis.

#coding : latin-1

class Imovel(object):
    __inscricao = 0
    __area = 0.0
    __valorm2 = 0.0

    def __init__(self, i, a, v): #construtor
        self.__inscricao = i
        self.__area = a
        self.__valorm2 = v

    def calcularIPTU(self):
        return self.__area * self.__valorm2

class Casa(Imovel):  #imovel uma referencia nessa linha
    __areaConstruida = 0.0
    __taxaConstrucao = 0.0

    def __init__(self, i, a, v, ac, tc):
        Imovel.__init__(self,i,a,v)
        self.__areaConstruida = ac
        self.__taxaConstrucao = tc

    def calcularIPTU(self):
        return (Imovel.calcularIPTU(self)) + (self.__areaConstruida * self.__taxaConstrucao)

