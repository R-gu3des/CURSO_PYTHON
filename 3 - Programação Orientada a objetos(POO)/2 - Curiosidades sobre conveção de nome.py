"""
Curiosidades sobre convenções de nome
"""

class Pessoa():
    ano_atual = 2021

    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def pegar_ano_atual(self):
        print(self.ano_atual - self.idade)

    @classmethod
    def por_data_nasc(cls, nome, ano_nascimento):
        idade = cls.ano_atual - ano_nascimento
        return cls(nome, idade)


p1 = Pessoa.por_data_nasc("Carla", 22)
print(p1)