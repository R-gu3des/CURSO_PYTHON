class CarrihoDeCompra:
    def __init__(self):
        self.produtos = []

    def inserir_produto(self, produto):
        self.produtos.append(produto)

    def listar_produtos(self):
        for elementos in self.produtos:
            print(elementos.nome, elementos.valor)
            
    def somar_total(self):
        soma = 0
        for produto in self.produtos:
            soma += produto.valor
        return soma

class Produto:
    def __init__(self, nome, valor):
        self.nome = nome
        self.valor = valor
    

# Testando a Agregaçã de classes:

p1 = Produto("Playstation 5", 5000.00)
p2 = Produto("Notebook", 5600.00)
p3 = Produto("Smart TV", 4500.60)
p4 = Produto("Carro", 3500.00)

carrinho = CarrihoDeCompra()

carrinho.inserir_produto(p1)
carrinho.inserir_produto(p2)
carrinho.inserir_produto(p3)
carrinho.inserir_produto(p4)

carrinho.listar_produtos()
print(carrinho.somar_total())