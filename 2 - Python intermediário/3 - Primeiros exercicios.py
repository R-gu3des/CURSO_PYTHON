"""
Exércicios complexos - 1
"""


def saudacao(saudacao, nome):
    return saudacao, nome

print(saudacao("Olá,","Renato"))

def soma(num1,num2,num3):
    return num1 + num2 + num3

print(soma(5,7,20))

def percentual(num, porcentagem):
    return num + (num * porcentagem) / 100

print(percentual(100, 10))

def fizbu(parametro):
    frase = ''
    if parametro % 2 == 0:
        frase = 'Fizz'
    elif parametro % 5 == 0 and parametro % 3 == 0:
        frase = 'FizzBuzz'
    elif parametro % 5 == 0:
        frase = 'buzz'
    else:
        return parametro

    return frase

print(fizbu(23))