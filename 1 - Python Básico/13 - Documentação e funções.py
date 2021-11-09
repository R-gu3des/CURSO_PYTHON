num = input("Digite um número: ")
num2 = input("Digite outro número: ")

if num.isdigit() and num2.isdigit(): # A Função isdigit() retorna se a string pode ser um número
    num = int(num)
    num2 = int(num2)

    print(num2 + num)
