"""
Criando uma classe para tratar de erros em python

"""

class TratarError(Exception): # A classe vai herdar da classe exception
    pass


def testar():
    raise TratarError("Errado!")


try:
    testar()
except TratarError as e:
    print(f"Erro: {e}")