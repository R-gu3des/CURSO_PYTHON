"""
ZIP - Compactando e descompactando arquivos
"""

from zipfile import ZipFile
import os
import zipfile

caminho = 'C:/Users/user/Pictures/'

# Adiciona todos os arquivos do caminho em um arquivo zip
with ZipFile('arquivo.zip', 'w') as zip:
    for arquivo in os.listdir(caminho):
        caminho_completo = os.path.join(caminho, arquivo)
        print(arquivo)
        zip.write(caminho_completo)

# lê todos os arquivos de dentro do zip
with ZipFile('arquivo.zip', 'r') as zip:
    for arquivo in zip.namelist():
        print(arquivo)

# Descompacata os arquivos na pasta 'Descompacatdo'(Só existirá apos a execução do arquivo)
with ZipFile('arquivo.zip', 'r') as zip:
    zip.extractall('Descompacatdo')