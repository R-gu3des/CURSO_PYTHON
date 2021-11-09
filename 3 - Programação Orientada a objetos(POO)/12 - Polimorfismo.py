"""
Polimorfismo é o principio que permite que classes derivadas de uma mesma 
superclasse tenham métodos iguais (de mesma assinatura)
mas comportamentos diferentes.

# Mesma assinatura = Mesma quantidade e tipo de parâmetros
"""


# Durante a aula anterior nós utilizamos um pouco de polimorfismo

# EX de polimorfismo simples

from abc import ABC, abstractmethod

class A(ABC):
    @abstractmethod
    def fala(self, mensagem):
        pass

class B(A):
    def fala(self, mensagem):
        print(f"B está falando {mensagem}...")
    

class C(A):
    def fala(self, mensagem):
        print(f"C está falando {mensagem}...")

b = B()
c = C()

b.fala("Hello world!")
c.fala("Bla bla bla")