# 3. Aplicando o Paradigma Orientado a Objeto
# a) Crie uma classe com um atributo nums, um método maior() que irá retornar o maior
# número, um método menor() que irá retornar o menor número. Entre com uma sequencia
# numérica de inteiros em uma linha, instancie um objeto, e exiba na tela o retorno dos
# métodos maior e menor deste objeto.

class Numeros(object):
    __lista = []

    def __init__(self, l):
        self.__lista = l

    def Maior(self):
        return max(self.__lista)

    def Menor(self):
        return min(self.__lista)







