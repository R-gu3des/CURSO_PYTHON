"""
O que são dataclasses? O módulo dataclasses fornece um decorador e funções
para criar automaticamente métodos, como __init__(), __repr__(), __eq__() (etc)
em classes definidas pelo usuário.
basicamente dataclasses são syntax sugar para criar classe normais.
Foi originalmente descrito ma PEP 557.
Adicionado na versão 3.7 do python.
leia a documentação: http://docs.python.org/pt-br/3/library/dataclasses.html
"""

from dataclasses import dataclass
from dataclasses import asdict, astuple #Transformam uma classe em um dicionário e uma tupla respectivamente

@dataclass(eq=True, repr=True, order=True, init=True) # Posso alterar as configurações padrões de uma classe
class Pessoa:
    nome: str
    sobrenome: str

    def __post_init__(self):
        self.nome_completo = f"{self.nome}, {self.sobrenome}"

    # @property
    # def nome_complet(self):
    #     return f"{self.nome}, {self.sobrenome}"


p1 = Pessoa("A", "Roger")
p2 = Pessoa("C", "Joi Boy")
p3 = Pessoa("B", "Anakin")
p4 = Pessoa("D", "Marcelo")

pesoas = [p1, p2, p3, p4]

print(sorted(pesoas, key=lambda x: x.nome))

print(asdict(p1))
print(astuple(p1))

