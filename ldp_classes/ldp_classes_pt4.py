class Dois:
    """
    Ao instanciar esta classe, o objeto reconhecerá um operador unário
    (+ ou -)
    """
    valor = 2

    def __neg__(self):
        """ Função negativa o valor da instância"""
        print('Negativo')
        return -self.valor

    def __pos__(self):
        """ Função positiva o valor da instância"""
        print('Positivo')
        return +self.valor


class InverteString:
    """
    Esta classe utiliza os operadores unários para inverter uma String
    """
    def __init__(self):
        self.s = 'Invertendo Strings'

    def __neg__(self):
        return self.s[::-1]


class Ponto:
    """
    Esta classe utiliza os operadores unários para inverter uma Coordenada xy
    """
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __neg__(self):
        return Ponto(-self.x, -self.y)

    def __pos__(self):
        return Ponto(+self.x, +self.y)

    def __repr__(self):
        return f'Ponto({self.x}, {self.y})'


class Somavel:
    """
    Esta classe sobrecreve os métodos mágicos de operadores
    """
    def __add__(self, valor):
        print('É uma soma')
        return valor

class Soma:
    """
    Esta classe sobrecreve os métodos mágicos de operadores
    """
    def __init__(self, valor):
        self.valor = valor

    def __add__(self, outro_valor):
        return self.valor + outro_valor

    def __radd__(self, outro_valor):
        return self.valor + outro_valor


class ListaLoka:
    def __init(self, l):
        self.l = l or []

    def __add__(self, val):
        """Soma todos os items da lista com val"""
        return ListaLoka([x + val for x in self.l])

    def __lshift(self, val):
        """Faz append na lista usando <<"""
        self.l.append(val)

    def __rshift(self, pos):
        """Remove um item com >>"""
        self.l.pop(pos)

    def __neg__(self):
        """Inverte a lista"""

        return ListaLoka(reversed(self.l))

    def __iadd__(self, val):
        """Soma todos os items da lista com val e mantem no objeto"""
        self.l = [x + val for x in self.l]
