"""
Operador Ternário em python
"""

usuario_logado = True
msg = 'Usuário Logado' if usuario_logado else "Usuário precisa logar!"   
print(msg)


idade = input('Digite uma idade: ')

if not idade.isnumeric():
    print('Você precisa digitar uma idade válida!')
else:
    deMaior = (int(idade) >= 18)
    msgm = 'É de maior' if deMaior else 'Não é de maior'
print(msgm)
