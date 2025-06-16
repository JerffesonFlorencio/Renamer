import os
from tkinter import filedialog
from tkinter import filedialog, messagebox


def renomear_arquivos():
    pasta = filedialog.askdirectory()
    if not pasta:
        return

    arquivos_renomeados = 0
    for nome_arquivo in os.listdir(pasta):
        caminho_antigo = os.path.join(pasta, nome_arquivo)

        if not os.path.isfile(caminho_antigo):
            continue

        nome_sem_espacos = nome_arquivo.replace(" ", "")
        if not nome_sem_espacos.lower().endswith(".docx"):
            nome_sem_espacos = os.path.splitext(nome_sem_espacos)[0] + ".docx"

        caminho_novo = os.path.join(pasta, nome_sem_espacos)

        if caminho_antigo != caminho_novo:
            os.rename(caminho_antigo, caminho_novo)
            arquivos_renomeados += 1

    messagebox.showinfo("Concluído", f"{arquivos_renomeados} arquivo(s) renomeado(s) com sucesso.")