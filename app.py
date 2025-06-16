import tkinter as tk
from api.src.utils.functions.renamer import renomear_arquivos

# Interface gráfica
janela = tk.Tk()
janela.title("Renomeador de Arquivos")
janela.geometry("300x150")

titulo = tk.Label(janela, text="Renomear arquivos para .docx", font=("Arial", 12))
titulo.pack(pady=10)

botao = tk.Button(janela, text="Selecionar Pasta e Renomear", command=renomear_arquivos)
botao.pack(pady=10)

janela.mainloop()
