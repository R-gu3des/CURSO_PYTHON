"""
Exercício - 1
"""

numero = input("Digite um valor: ")

if numero.isdigit() :
    numero = int(numero)
    print(f"O número é: {numero}")
else:
    print('O valor não pôde ser convertido!')

hora = int(input('Digite uma hora: '))

if hora >= 0 and hora <= 11:
    print("Bom Dia !!")
elif hora >= 12 and hora <= 17:
    print("Boa Tarde!!")
elif hora >= 18 and hora <= 23:
    print('Boa noite!!')
else:
    print("Isso não é um número válido")



nome = input("Digite o seu primeiro nome: ")

if len(nome) <= 4 :
    print('Seu nome é muito pequeno')
elif numero == 5 or numero == 6:
    print("Seu nome é normal")
else:
    print("Seu nome é muito grande")