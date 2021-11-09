class A:
    def falar(self):
        print("Estou falando em A")

class B(A):
    def falar(self):
        print("Estou falando em B")

class C(A):
    def falar(self):
        print("Estou falando em C")


# Heranças múltiplas

class D(B, C):
    pass

d = D()
d.falar()

# Caso a classe herde de duas classes que possuam o mesmo método, a classe que for passada primeiro é que terá o método executado
# Como no exemplo acima o resultado para d.falar() => "Estou falando em B"

class D(B, C):
    def falar(self):
        print("Estou falando em D")

d = D()
d.falar()

# Nesser caso, já que a função "falar" também foi criada em D, o que será executado é => "Estou falando em D"



class LogMixIn():
    @staticmethod
    def write(msg):
        with open('arquivo.log', 'a+') as file:
            file.write(msg + "\n")

    def logInfo(self, msg):
        self.write(f"INFO: {msg}")

    def log_erro(self, msg):
        self.write(f"ERRO: {msg}")


class Eletronico:
    def __init__(self, nome):
        self._nome = nome
        self._ligado = False

    def ligar(self):
        if self._ligado:
            print(f"{self._nome} já está ligado!")
            return
        else:
            self._ligado = True
            print(f"O {self._nome} ligou!")
            return
    def desligar(self):
        if self._ligado:
            self._ligado = False
            print(f"O {self._nome} foi desligado!")
            return
        else:
            print(f"O {self._nome} já está desligado!")
            return

class Smartphone(Eletronico, LogMixIn):
    def __init__(self, nome):   
        super().__init__(nome)
        self._conectado = False

    def conectar(self):
        if self._ligado:
            if self._conectado:
                erro = f"{self._nome} já está conectado!"
                print(erro)
                self.log_erro(erro)
                return
            else:
                self._conectado = True
                info = f"{self._nome} foi conectado!"
                print(info)
                self.logInfo(info)
                return
        elif not self._ligado:
            info = f"{self._nome} está desligado!"
            print(info)
            self.logInfo(info)
            return
    def desconectar(self):
        if self._ligado:
            if self._conectado:
                info = f"{self._nome} foi desconectado!"
                print(info)
                self.logInfo(info)
                self._conectado = False
                return
            else:
                erro = f"{self._nome} já está desconectado!"
                print(erro)
                self.log_erro(erro)
                return
        else:
            erro = f"{self._nome} está desligado"
            print(erro)
            self.log_erro(erro)
            return


galaxy = Smartphone("S21")

galaxy.ligar()
galaxy.ligar()

galaxy.desligar()
galaxy.desligar()

galaxy.conectar()

galaxy.ligar()
galaxy.conectar()

galaxy.desconectar()
galaxy.desconectar()
