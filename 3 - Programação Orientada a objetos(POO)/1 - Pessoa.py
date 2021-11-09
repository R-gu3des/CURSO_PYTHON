# Estamos representando a classe pessoa como um objeto

# Devemos iniciar uma classe com uma letras maiscula

# class Pessoa:
#     nome = 'Ruan'
#     idade = 22
#     altura = 1.78
#     peso = 78

# p1 = Pessoa()
# p1.nome ='Renato'
# p1.peso = 50
# p1.idade = 20
# p1.altura = 1.70
# p2 = Pessoa()

# print(p1.nome)


#  O self deve ser instânciado obrigatoriamente em uma função de uma classe

from datetime import datetime

class Pessoa:
    def falar(self):
        print(f'{self.nome} está falando!!')
        return


p1 = Pessoa()
p1.nome = 'Ruan'



# O self não deve ser considerado quando passamos atributos para a função '__init__'
# O self serve para indicar que o atributo está sendo referênciado a um objeto especifico que será criado a partir da classe

class Pessoa2:

    ano_atual = int(datetime.strftime(datetime.now(), '%Y'))

    def __init__(self, nome, idade, comendo=False, falando=False):
        self.nome = nome
        self.idade = idade
        self.comendo = comendo
        self.falando = falando



    def comer(self, alimento): # Sempre que criarmos uma nova função em uma classe devemos criar o parâmetro self
        # Para não gerar um 'erro' em que a pessoa come mais de uma vez, podemoms fazer:

        if self.comendo:
            print(f"{self.nome} já está comendo!!")
            return
        print(f'{self.nome} começou a comer {alimento}!!')
        self.comendo = True



    def parar_de_comer(self):
        if self.comendo:
            print(f"{self.nome} terminou de fazer a sua refeição!!")
            self.comendo = False
            return
        print(f"{self.nome} ainda não fez a sua refeição!!")



    def falar(self, frase):
        if self.comendo:
            print(f"{self.nome} não pode falar comendo!!")
            return    
        elif not self.falando:
            print(f"{self.nome} disse: '{frase}'")
            self.falando = True



    def pararDeFalar(self):
        if self.falando:
            print(f"{self.nome} parou de falar!!")
            self.falando = False
            return
        print(f'{self.nome} não está falando!!')


    def pegarDataDenascimento(self):
        data_de_nascimento = self.ano_atual - self.idade
        return data_de_nascimento
# Instanciando uma pessoa e]de uma classe pessoa2

p = Pessoa2('Ruan',22,False,False)

print(p.nome, p.idade, p.falando, p.comendo)

p.falar('hello world!!')
p.parar_de_comer()
p.comer("torta de limão")
p.comer("Maçã")
p.pararDeFalar()
p.pararDeFalar()
p.parar_de_comer()
p.falar('Eae pessoal, como vão?')


print(p.nome, p.idade, p.falando, p.comendo)

# Instânciando mais de uma pessoa para ver a independência entre os objetos:

p2 = Pessoa2("Amanda", 35)
p3 = Pessoa2("Roger", 40)

p2.falar('Oi gente, tudo bom?')
p3.falar('Hoje eu acordei feliz!')

print(p2.pegarDataDenascimento(p2.idade))