import os
from sys import path
from PIL import Image


def main(imagens_folder):
    if not os.path.isdir(imagens_folder):
        raise NotADirectoryError(f"{imagens_folder} não existe")

    for root, dirs, files in os.walk(imagens_folder):
        for file in files:
            caminho_completo = os.path.join(root, file)
            nome_arquivo, extensao = os.path.splitext(file)
            novo_arquivo = nome_arquivo + "_CONVERTIDO" + extensao
            caminho_completo_NA = os.path.join(root, novo_arquivo)
            print(caminho_completo_NA)


if __name__ == "__main__":
    imagens_folder = r"C:\Users\user\Pictures"
    main(imagens_folder)