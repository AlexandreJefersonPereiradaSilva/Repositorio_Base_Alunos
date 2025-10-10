# nivel de acesso público
class A:
    def __init__(self, meu_atributo):
        self.meu_atributo = meu_atributo

#nivel de acesso protegido
class B:
    def __init__(self, _meu_atributo):
        self._meu_atributo = _meu_atributo

# Nivel de acesso privado
class A:
    def __init__(self, __meu_atributo):
        self.__meu_atributo = __meu_atributo

# getters e setters

@property
def idade(self):
    return self._idade

@idade.setter
def idade(self, valor):
    self._idade = valor