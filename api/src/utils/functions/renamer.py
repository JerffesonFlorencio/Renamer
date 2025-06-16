import os
from tkinter import filedialog
from tkinter import filedialog, messagebox


def renomear_arquivos_para_extensao(extensao):
    pasta = filedialog.askdirectory(title="Selecione a pasta com os arquivos")
    if not pasta:
        return

    for nome_arquivo in os.listdir(pasta):
        caminho_antigo = os.path.join(pasta, nome_arquivo)
        if os.path.isfile(caminho_antigo):
            nome_base = os.path.splitext(nome_arquivo)[0].replace(" ", "")  # Remove espaços
            novo_nome = f"{nome_base}.{extensao}"
            caminho_novo = os.path.join(pasta, novo_nome)
            os.rename(caminho_antigo, caminho_novo)
    print(f"Arquivos renomeados para .{extensao} com sucesso.")
    
