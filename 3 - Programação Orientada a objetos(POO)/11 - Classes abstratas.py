"""
Classes abstratas - Uma classe abstrata vai te forçar a implementar alguns métodos
"""

from abc import ABC, abstractmethod

# ABC é o abstratc method class

class A(ABC):
    @abstractmethod
    def falar(self):
        ...
    # Ex: Se temos o método falar, dentro da classe A, a classe B que vai herdar de A também vai precisar implementar

class B(A):
    def falar(self):
        print("Falando... Class B")
    
# a = A()
# a.falar() => erro


b = B()
b.falar()


# Criando uma conta de Banco

class Conta(ABC): # Essa é a maneira de dizer que a conta é abstrata...
    def __init__(self, agencia, numeroConta, saldo):
        self._agencia = agencia
        self._numeroConta = numeroConta
        self._saldo = saldo

    # Gets e Sets
    @property
    def agencia(self):
        return self._agencia

    @property
    def numeroConta(self):
        return self._numeroConta
    
    @property
    def saldo(self):
        return self._saldo

    @saldo.setter
    def saldo(self, valor):
        if not isinstance(valor, (int, float)): # o isinstance nos permite analisar se o valor é um inteiro ou um float
            raise ValueError("O saldo precisa ser númerico") 
        self._saldo = valor

    def depositar(self, valor):
        if not isinstance(valor, (int, float)):
            raise ValueError("Você precisa inserir um valor númerico para o depósito!")
        print(f"Saldo depositado: {valor}")
        self.saldo += valor
        self.detalhes()
    def detalhes(self):
        print(f"Agência: {self.agencia}", end=" ")
        print(f"Número da conta: {self.numeroConta}", end=" ")
        print(f"Saldo: {self.saldo}")

    @abstractmethod       
    def sacar(self):
        ...


class ContaPoupanca(Conta):
    def sacar(self, valor):
        if  self.saldo < valor:
            print("Saldo insuficiente!")
            return
        print(f"Saldo retirado {valor}")
        self.saldo -= valor
        self.detalhes()

cp = ContaPoupanca("Banco BBB", 123, 500.00)
cp.sacar(300)
cp.depositar(600)

# conta = Conta("Banco BBB", 123, 500.00)
# print(conta) -> Não é possível intanciar uma conta com o método abstrato
 



class ContaCorrente(Conta):
    def __init__(self, agencia, numeroConta, saldo, limite=100):
        super().__init__(agencia, numeroConta, saldo)
        self._limite = limite

    @property
    def limite(self):
        return self._limite
    
    def sacar(self, valor):
        if (self.saldo + self.limite) < valor:
            print("Saldo insuficiente!")
            return
        print(f"Saldo retirado {valor}")
        self.saldo -= valor
        self.detalhes()


contaC = ContaCorrente('Banco ABC', 1456, 0, 500)
contaC.depositar(500)
contaC.sacar(700)
contaC.detalhes()
