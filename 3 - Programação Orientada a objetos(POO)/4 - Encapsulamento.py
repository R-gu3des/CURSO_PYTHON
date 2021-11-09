"""
Public, Proteceted, Private

# Usando 1 underline o atributo se torna protected: _dados
# Usando 2 underlines o atributo se torna privado: __dados

# Protected: (_NOMEDACLASSE_nomeatributo)

"""


class BancoDados():
    def __init__(self):
        self.dados = {}

    def inserirCliente(self, id, nome):
        if 'clientes' not in self.dados:
            self.dados['clientes'] = {id : nome}
        else:
            self.dados['clientes'].update({id : nome})

    def lista_clientes(self):
        for id, nome in self.dados['clientes'].items():
            print(f"Identificador: {id} -- Nome: {nome}")
    

banco = BancoDados()

banco.inserirCliente(1, "Mari")
banco.inserirCliente(2, "Roni")
banco.inserirCliente(3, "Malcon")
banco.inserirCliente(4, "Carla")





class BancoDados2():
    def __init__(self):
        self._dados = {}

    def inserirCliente(self, id, nome):
        if 'clientes' not in self._dados:
            self._dados['clientes'] = {id : nome}
        else:
            self._dados['clientes'].update({id : nome})

    def lista_clientes(self):
        for id, nome in self._dados['clientes'].items():
            print(f"Identificador: {id} -- Nome: {nome}")

banco = BancoDados2()

banco.inserirCliente(1, "Mari")
banco.inserirCliente(2, "Roni")
banco.inserirCliente(3, "Malcon")
banco.inserirCliente(4, "Carla")

banco._dados = 'Outra coisa'
print(banco._dados)





class BancoDados3():
    def __init__(self):
        self.__dados = {}

    def inserirCliente(self, id, nome):
        if 'clientes' not in self.__dados:
            self.__dados['clientes'] = {id : nome}
        else:
            self.__dados['clientes'].update({id : nome})

    def lista_clientes(self):
        for id, nome in self.__dados['clientes'].items():
            print(f"Identificador: {id} -- Nome: {nome}")

banco = BancoDados3()

banco.inserirCliente(1, "Mari")
banco.inserirCliente(2, "Roni")
banco.inserirCliente(3, "Malcon")
banco.inserirCliente(4, "Carla")

banco.__dados = 'Outra coisa'
print(banco.__dados)
print(banco.__dados)


print(banco._BancoDados3__dados) # Para acessar um dado com setado como privado, ele precisa ser passado desta maneira