def retornaInteiro(valor):
    try:
        valor = int(valor)
        return valor    
    except ValueError as erro:
        pass
    except:
        try:
            valor = float(valor)
            return valor
        except ValueError '':
            pass


numero = retornaInteiro(input('Digite um número: '))

print(numero * 5)


while True:
    if numero is None:
        print('Isso não é um número')
    else:
        print(numero * 5)

