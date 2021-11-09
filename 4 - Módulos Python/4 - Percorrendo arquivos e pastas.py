"""
Para percorrer pelas pastas do próprio computador nós utilizaremos o módulo 'os' do python
"""
import os

caminhoDoArquivo =  "C:/Users/user/Downloads"
valorDePesquisa = "JUJUTSU"

# Maneiras de precorrer pelas pastas


# Imprimindo nome dos arquivos
for raiz, diretorios, arquivos in os.walk(caminhoDoArquivo):
    print(raiz, diretorios, arquivos)
    for arquivo in arquivos:
        print(arquivo)

print('\n','*=' * 25, '\n')

# Imprimindo caminho completo de cada arquivo
for raiz, diretorios, arquivos in os.walk(caminhoDoArquivo):
    for arquivo in arquivos:
        caminho_completo = os.path.join(raiz, arquivo)
        print(caminho_completo)

print('\n','*=' * 25, '\n')

# Separando nome do arquivo e extensão
for raiz, diretorios, arquivos in os.walk(caminhoDoArquivo):
    for arquivo in arquivos:
        nome_arquivo, extensao_arquivo = os.path.splitext(arquivo)
        print(nome_arquivo, extensao_arquivo, sep=' ** ')

print('\n','*=' * 25, '\n')

# Procurando arquivo de acordo com seu termo:
for raiz, diretorios, arquivos in os.walk(caminhoDoArquivo):
    for arquivo in arquivos:
        try:
            if valorDePesquisa in arquivo:
                caminho_completo = os.path.join(raiz, arquivo)
                nome_arquivo, extensao = os.path.splitext(arquivo)
                tamanho_arquivo = os.path.getsize(caminho_completo)
                print(f"\nArquivo encontrado: {arquivo}\nCaminho: {caminho_completo}\nNome do arquivo: {nome_arquivo}\nExtensão: {extensao_arquivo}\nTamanho: {tamanho_arquivo}")

            # Algumas exceções que podem ser encontradas:
        except PermissionError as e:
            print("Você não tem permissão para ler este arquivo!")
        except FileNotFoundError as e:
            print("Arquivo não encontrado!")
        except Exception as e:
            print("Erro desconhecido!")