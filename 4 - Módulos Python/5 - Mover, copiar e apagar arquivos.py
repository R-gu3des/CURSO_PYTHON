import os
import shutil

# Nesse contexto, o "r" antes da string serve para indicar que as barras estão inversas
# Que é como é passado o caminho no widows quando copiamos, porém as barras deveriam ser nesse sentido -> '/'
caminho = r'C:\Users\user\Desktop\bolsa'
novo_local = r'C:\Users\user\Desktop\Pasta_teste'


"""Mudando a pasta de local a partir do mkdir"""

# Nessa etapa estamos tentando criar uma pasta através do caminho e nome que passamos
try:
    os.mkdir(novo_local)
except FileExistsError as e:
    print(f'A pasta {novo_local} já existe!')

for raiz, diretorios, arquivos in os.walk(caminho):
    for arquivo in arquivos:
        # É preciso pegar o caminho inteiro anterior de cada arquivo
        caminho_anterior_completo = os.path.join(raiz, arquivo)
        # Depois adicionamos o novo local ao qual tentamos passar os arquivos anteriores
        novo_caminho_completo = os.path.join(novo_local, arquivo)

        """Cuidado para não perder os arquivos"""

        # Utilizamos a função shutil.move(caminho_inicial, novo_caminho) para movermos os
        # arquivos para uma nova pasta

        shutil.move(caminho_anterior_completo, novo_caminho_completo)
        print(f'Arquivo {arquivo} movido com sucesso!')



"""Agora iremos copiar alguns arquivos da pasta nova para a pasta anterior com shutil.copy(pasta, pastaDesejada)"""

for r, d, a in os.walk(novo_local):
    for arquivo in a:
        pasta_anterior = os.path.join(r, arquivo)
        pasta_da_copia = os.path.join(caminho, arquivo)
        nomeArquivo, extensao = os.path.splitext(arquivo)
        if extensao == ".txt":
            shutil.copy(pasta_anterior, pasta_da_copia)


"""Apagando arquivos de pastas os.remove(diretoria_pasta)"""

for r, d, a in os.walk(caminho):
    for arquivo in a:
        file_direc_complt = os.path.join(r, arquivo)
        if ".txt" in file_direc_complt:
            os.remove(file_direc_complt)