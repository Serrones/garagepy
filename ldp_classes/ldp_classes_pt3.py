class Pizzaria:
    def __init__(self):
        self._pizzaiolo = Pizzaiolo()

    def pedido(self, pizza):
        self._pizzaiolo.preparar_pizza(pizza)


class Forno:
    def __init__(self):
        self.pizzas = []
        self.lenha = None

    def assar(self, pizza):
        if not self.lenha:
            print('Não há lenha')


class Pizzaiolo:
    def __init__(self):
        self._forno = Forno()

    def preparar_pizza(self, pizza):
        self._forno.assar(pizza)


class Passaro:
    def __init__(self, nome):
        self.nome = nome

class Papagaio(Passaro):
    def __init__(self, nome, cor):
        # chama o __init__ da superclasse
        super().__init__(nome)
        self.cor = cor
        
    def __str__(self):
        return f'Papagaio(nome="{self.nome}", cor="{self.cor}")'

    def __repr__(self):
        return self.__str__()
