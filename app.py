import tkinter as tk
from api.src.utils.functions.renamer import renomear_arquivos_para_extensao

# Interface gráfica
janela = tk.Tk()
janela.title("Renomeador de Arquivos")
janela.geometry("300x150")

titulo = tk.Label(janela, text="Renomear arquivos", font=("Arial", 12))
titulo.pack(pady=10)

botao_eml = tk.Button(janela, text="Renomear para .eml", command=lambda: renomear_arquivos_para_extensao("eml"))
botao_eml.pack(pady=5)

botao_docx = tk.Button(janela, text="Renomear para .docx", command=lambda: renomear_arquivos_para_extensao("docx"))
botao_docx.pack(pady=5)


janela.mainloop()
