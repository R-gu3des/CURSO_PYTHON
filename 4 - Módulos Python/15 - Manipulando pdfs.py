"""
Documentação: https://pythonhosted.org.PyPDF2/

Maneiras de instalar:

pip install pypdf2 # virtualenv
pipenv install pypdf2 #pipenv

"""

import PyPDF2
import os

from PyPDF2 import pdf

# União do pdfs
"""
novo_pdf = PyPDF2.PdfFileMerger()
caminho_dos_pdfs = r"C:\Users\user\Documents\pdfs"

for root, dirs, files in os.walk(caminho_dos_pdfs):
    for file in files:
        caminho_completo = os.path.join(root, file)

        arquivo_pdf = open(caminho_completo, 'rb') # Mood para ele em bites (read bites)
        novo_pdf.append(arquivo_pdf)

with open(f'{caminho_dos_pdfs}/novo_arquivo.pdf', 'wb') as pdf:
    novo_pdf.write(pdf)
"""

# Separando os pdfs:
with open()
