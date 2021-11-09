# Faça uma lista de tarefas com as seguintes opções de tarefas:
# Adicionar tarefas
# Listar tarefas
# Desfazer (Desfaz a última ação)
# Reafazer (Refaz a última ação)

lista = []
ultima_alteracao = ''

while True:
    # Menu do código
    print('Menu Lista de tarefas')
    print('\n1 - Adicionar tarefas')
    print('2 - Listar tarefas\n3 - Desfazer\n4 - Refazer')

    opcao = input("Digite qual opção você deseja executar: ")
    if opcao == '1':
        with open('arquivo.txt','w+') as a1:
            tarefa = input("Digite uma tarefa para adicionar a lista: ")
            lista.append(tarefa)
            ultima_alteracao = lista[-1]
            for c in lista:
                a1.write(f'{c}\n')
    elif opcao == '2':  
        with open("arquivo.txt","r+") as a2:
            for linha in a2.readlines():
                print('Todas as tarefas: ') 
                print(linha, end="")
    elif opcao == '3':
        with open("arquivo.txt","w") as a3:
            lista.remove(ultima_alteracao)
            for c in lista:
                a3.write(f'{c}\n')
    elif opcao == '4':
        lista.append(ultima_alteracao)
        with open("arquivo.txt","w") as a4:
            for i in lista:
                a4.write(f'{i}\n')
    elif opcao == '5':
        print('Até a próxima!')
        break
    else:
        print('Opção inválida!!')