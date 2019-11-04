# def quadrado(x): Esse é o parametro formal
def quadrado(x):
    if type(x) == float:
        x = x * x
        return x
    if type(x) == int:
        x = float(x)
        x = x * x
        return int(x)
    if type(x) == str:
        x = float(x)
        x = x * x
        return str(x);

print("Quadrado do numero inteiro 2...: ", quadrado(2))
print("Quadrado do numero float 2.5...: ", quadrado(2.5))
print("Quadrado do numero str '6'...: "+ quadrado('6')) #Esse é o parametro real e posicionado

# 1)Comentar quais parametros formais e quais reais
# 2)Identificar passagem por parametro ou referencia
#É passagem por parametro
# 3)Sua função é polimorfica ou monomorfica?
#É polimorfico