import os
import datetime
import tkinter as tk
from tkinter import ttk

def contar_arquivos_por_data(diretorios):
    contagem_por_diretorio_e_data = {}

    for diretorio in diretorios:
        arquivos = [arquivo for arquivo in os.listdir(diretorio) if arquivo.endswith(".txt")]

        contagem_por_data = {}
        for arquivo in arquivos:
            caminho_completo = os.path.join(diretorio, arquivo)
            data_modificacao = datetime.date.fromtimestamp(os.path.getmtime(caminho_completo))
            data_modificacao_str = data_modificacao.strftime("%d/%m/%Y")
            contagem_por_data[data_modificacao_str] = contagem_por_data.get(data_modificacao_str, 0) + 1

        nome_diretorio = os.path.basename(diretorio)  # Obter apenas o nome do diretório
        contagem_por_diretorio_e_data[nome_diretorio] = contagem_por_data

    return contagem_por_diretorio_e_data

def atualizar_busca():
    contagem_por_diretorio_e_data = contar_arquivos_por_data(diretorios)
    atualizar_tabela(contagem_por_diretorio_e_data)

def aplicar_filtro_nome():
    filtro = entrada_filtro_nome.get().strip().lower()
    if filtro:
        filtrar_resultados("Nome", filtro)

def aplicar_filtro_data():
    filtro = entrada_filtro_data.get().strip()
    if filtro:
        filtrar_resultados("Data", filtro)

def filtrar_resultados(coluna, filtro):
    for row_id in tree.get_children():
        valor = tree.item(row_id)["values"][colunas.index(coluna)].lower()
        if filtro in valor:
            tree.selection_add(row_id)
        else:
            tree.selection_remove(row_id)

# Defina seus diretórios aqui
diretorios = ["/caminho/do/seu/diretorio1", "/caminho/do/seu/diretorio2"]

# Criar janela principal
janela = tk.Tk()
janela.title("Contagem de Arquivos por Data")

# Criar uma tabela para exibir os resultados
tree = ttk.Treeview(janela, columns=("Nome", "Quantidade", "Data"), show="headings")
tree.heading("Nome", text="Nome")
tree.heading("Quantidade", text="Quantidade")
tree.heading("Data", text="Data")
tree.pack(fill="both", expand=True)

# Entrada de texto para filtrar por nome
frame_filtro_nome = tk.Frame(janela)
frame_filtro_nome.pack(pady=5)
label_filtro_nome = tk.Label(frame_filtro_nome, text="Filtrar por Nome:")
label_filtro_nome.grid(row=0, column=0)
entrada_filtro_nome = tk.Entry(frame_filtro_nome)
entrada_filtro_nome.grid(row=0, column=1)
botao_filtro_nome = tk.Button(frame_filtro_nome, text="Aplicar Filtro", command=aplicar_filtro_nome)
botao_filtro_nome.grid(row=0, column=2)

# Entrada de texto para filtrar por data
frame_filtro_data = tk.Frame(janela)
frame_filtro_data.pack(pady=5)
label_filtro_data = tk.Label(frame_filtro_data, text="Filtrar por Data:")
label_filtro_data.grid(row=0, column=0)
entrada_filtro_data = tk.Entry(frame_filtro_data)
entrada_filtro_data.grid(row=0, column=1)
botao_filtro_data = tk.Button(frame_filtro_data, text="Aplicar Filtro", command=aplicar_filtro_data)
botao_filtro_data.grid(row=0, column=2)

# Botão para atualizar a busca
botao_atualizar = tk.Button(janela, text="Atualizar", command=atualizar_busca)
botao_atualizar.pack()

# Atualizar a busca inicial
atualizar_busca()

# Iniciar o loop da interface gráfica
janela.mainloop()
