# Programa para controlar dispositivos conectados a sua rede wifi que estao consumindo
# sua banda larga. O programa deve perguntar quantos dispositivos existem, quais sao
# eles, quais estao ligados e calcular o consumo total da banda.

class Dispositivo(object):
    __IP = " "
    _ligado = True
    _aplicacao = 0  #apenas um unico _ indica que ele pode ser usado pelos filhos, se nao fizesse isso, teria que fazer as 3 variaveis pra cada classe

    def __init__(self, ip, l, a):
        self.__IP = ip
        self._ligado = l
        self._aplicacao = a

    def getConsumo(self):
        pass #ele passa pra vc poder sobrescrever nos outros lugares


class SmartPhone(Dispositivo):

    def __init__(self, ip, l, a):
        Dispositivo.__init__(self,ip,l,a)

    def getConsumo(self):
        if self._ligado == True:
            if (self._aplicacao == 0):
                return 300
            if (self._aplicacao == 1):
                return 1
            if (self._aplicacao == 2):
                return 150


class Tablet(Dispositivo):

    def __init__(self, ip, l, a):
        Dispositivo.__init__(self,ip,l,a)

    def getConsumo(self):
        if self._ligado == True:
            if (self._aplicacao == 0):
                return 400
            if (self._aplicacao == 1):
                return 10
            if (self._aplicacao == 2):
                return 300

class PC(Dispositivo):

    def __init__(self, ip, l, a):
        Dispositivo.__init__(self,ip,l,a)

    def getConsumo(self):
        if self._ligado == True:
            if (self._aplicacao == 0):
                return 400
            if (self._aplicacao == 1):
                return 10
            if (self._aplicacao == 2):
                return 350

