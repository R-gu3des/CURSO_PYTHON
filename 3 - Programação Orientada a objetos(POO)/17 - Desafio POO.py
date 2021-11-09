from abc import ABC, abstractmethod

class Conta():
    def __init__(self, agencia, numeroConta, saldo):
        self.agencia = agencia
        self.numeroConta = numeroConta
        self.saldo = saldo

    def deposito(self, valor):
        self.saldo += valor
        print("Deposito efetuado com sucesso!")
        return

    def detalhes(self):
        print(f"Agência: {self.agencia}")
        print(f"Conta: {self.numeroConta}")
        print(f"Saldo: {self.saldo}")
        return


    @abstractmethod
    def sacar(self,valor):
        ...
        

class Poupanca(Conta):
    def sacar(self, valor):
        if (self.saldo - valor) < 0:
            print("Saldo insuficiente!")
            return
        else:
            print("Saque concluido com sucesso!")
            self.saldo -= valor
            self.detalhes()
            return


class ContaCorrente(Conta):
    def __init__(self, agencia, numeroConta, saldo, limite=-200):
        super().__init__(agencia, numeroConta, saldo)
        self.limite = limite
    def sacar(self, valor):
        if (self.saldo - valor) >= self.limite:
            print("A transação foi concluida!")
            self.saldo -= valor
            self.detalhes()
            return
        else:
            print("Saldo insuficiente!")
            return


class Pessoa():
    def __init__(self, nome, idade):
        self._nome = nome
        self.idade = idade

    @property
    def nome(self):
        return self._nome

    @nome.setter
    def nome(self, n):
        self._nome = n
    
    @property
    def idade(self):
        return self.idade

    @idade.setter
    def idade(self, numero):
        self.idade = numero   

class Cliente(Pessoa):
    def __init__(self, nome, idade):
        super().__init__(nome, idade)

    def iniseirConta(self, c):
        self.conta = c

class Banco():
    
    def __init__(self):
        self.agencias = [1111,2222,3333]
        self.clientes = []
        self.contas = []

    def inserirClientes(self, cliente):
        self.clientes.append(cliente)
        
    def inserirContas(self, conta):
        self.contas.append(conta)

    def autenticar(self, cliente):
        if cliente not in  self.clientes:
            return False
        if cliente.conta not in self.contas:
            return False
        if cliente.conta.agencia not in self.agencias:
            return False
        
        return True