"""
Associação - usa | Agregação - Tem | Composição - É dono | Herança é 
"""

class Cliente:
    pass

class Aluno:
    pass


# Nessas duas calasses, tanto aluno quanto cliente são pessoas:
# Dessa forma nós podemos criar uma classe que servirá de base para as outras duas

class Pessoa:
    def __init__(this, nome, idade):
        this.idade = idade
        this.nome = nome
        this.nomeClasse = this.__class__.__name__
    def falar(self):
        print(self.nome + " está falando")

       

class Cliente(Pessoa): # No python essa é a meneira de se informar que uma classe está herdando de outra
    def comprar(self):
        print(f"{self.nome} está comprando...") # Podemos passar métodos específicos para classes que estão herdando de outra 



class Aluno(Pessoa):
    def estudar(self):
        print(f"{self.nome} está estudando...")


c1 = Cliente("Rayanne", 24)
print(c1.nome)

a1 = Aluno("Rogerio", 42)
print(a1.idade)

c1.falar()
c1.comprar()
print("Clase: " + c1.nomeClasse)

a1.falar()
a1.estudar()
print("Classe: " + a1.nomeClasse)