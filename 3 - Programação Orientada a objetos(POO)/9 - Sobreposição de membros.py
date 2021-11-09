class Pessoa:
    def __init__(self, nome, idade):
        self.idade = idade
        self.nome = nome
        self.nomeClasse = self.__class__.__name__
    def falar(self):
        print(self.nome + " está falando")


class Cliente(Pessoa):
    def comprar(self):
        print(f"{self.nome} está comprando...")

class Aluno(Pessoa):
    def estudar(self):
        print(f"{self.nome} está estudando...")

# Nesse caso o cliente Vip vai herdar de cliente, que herda de Pessoa.
# Cliente VIP tem tudo de Pessoa e tudo de Cliente

class ClienteVIP(Cliente):
    # Se você quiser adicionar atributos ao construtor de uma classe que está herdando, você também pode fazer um super
    def __init__(self, nome, idade, sobrenome):
        super().__init__(nome, idade)
        self.sobrenome = sobrenome # E podemos criar esse atributo extra, usando a mesma métodologia do primeiro construtor


    def falar(self):
        #super().falar() # É possível usar um super para fazer um override de um método em uma classe que está herdando ao invés de recriar o método por completo
        Pessoa.falar(self) # também é possível fazer um override selecionando de que classe você deseja sobrescrever assim.
        print(f"Eu sou um cliente VIP")
# Já que o método falar já existe em cliente, o método falar aqui vai fazer uma sobreposição(Override)
# Se não houvesse esse método na classe ClienteVIP, o método iria ser procurado nas classes anteriores e pararia ná primeira que encontrasse.

