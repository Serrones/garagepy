class Fila:
    """
    Abstração de qualquer tipo de Fila
    """

    c_fila = []

    @classmethod
    def c_entrar(cls, obj):
        cls.c_fila.append(obj)
        print(cls.c_fila)

    def __init__(self):
        self.s_fila = []

    def s_entrar(self, obj):
        self.s_fila.append(obj)
        print(self.s_fila)


class Pizza:
    slice = 8

    @classmethod
    def change_slice(cls, slice):
        cls.slice = slice

    def __init__(self, flavour):
        self.flavour = flavour

    def get_slice(self):
        self.slice -= 1
        print(self.slice)

    @staticmethod
    def ingredients():
        return "Ingredientes"

class Mussarela(Pizza)
    ...

class Calabresa(Pizza):
    ...

class MeioAMeio(Pizza):
    ...
