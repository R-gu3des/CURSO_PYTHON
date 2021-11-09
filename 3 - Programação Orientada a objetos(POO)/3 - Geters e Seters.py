class Produto():
    def __init__(self, nome, preco):
        self.preco = preco
        self.nome = nome

    def desconto(self, percentual):
        self.preco = self.preco - self.preco * (percentual / 100)

    #Getter
    @property
    def preco(self):
        return self._preco
    

    @preco.setter
    def preco(self, valor):
        if isinstance(valor, str):
            valor = float(valor.replace("R$", ""))
        self._preco = valor

    @property
    def nome(self):
        return self._nome
    
    @nome.setter
    def nome(self, valor):
        self._nome = valor.title()


p1 = Produto("PS5", 5000)
print(p1.preco, p1.nome)
p1.desconto(5)
print(p1.preco)

p2 = Produto("CARRO", 25000)
print(p2.nome)
