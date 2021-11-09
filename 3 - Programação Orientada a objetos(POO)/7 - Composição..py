class Cliente():
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade
        self.enderecos = []

    def inserir_endereco(self, cidade, estado):
        self.enderecos.append(Endereco(cidade,estado))

    def listar_enderecos(self):
        print(f"Cliente: {self.nome}")
        for endereco in self.enderecos:
            print(f'Cidade: {endereco.cidade}, Estado: {endereco.estado}')

    # Função para deletar elemento
    def __del__(self):
        print(f"{self.nome} Foi deletado.")

    
class Endereco():
    def __init__(self, cidade, estado):
        self.cidade = cidade
        self.estado = estado

    def __del__(self):
        print(f"{self.cidade} Foi deletada.")

c1 = Cliente("Marcelo", 23)


c1.inserir_endereco("Camaragibe", "Pernambuco")
c1.inserir_endereco("Recife", "pernambuco")
c1.inserir_endereco("Belo Horizonte","Minas Gerais")
c1.inserir_endereco("Campina Grande","Rio Grande do Sul")

c1.listar_enderecos()

del c1

# Todos os objetos que estão dentro da classe cliente seram deletados depois que a classe cliente for apagada