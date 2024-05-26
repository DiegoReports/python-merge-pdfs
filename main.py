import PyPDF2
import os #manipular arquivos

merger = PyPDF2.PdfMerger()

# LISTANDO FILES
lista_arquivos = os.listdir("arquivos")
lista_arquivos.sort()

# PERCORRENDO FILES
for arquivo in lista_arquivos:
    if ".pdf" in arquivo:
          merger.append(f"arquivos/{arquivo}")

# GERANDO ARQUIVO DE SAIDA
merger.write("PDF Final.pdf")
