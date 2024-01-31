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
    atualizar_lista(contagem_por_diretorio_e_data)

def criar_lista_valores(coluna):
    valores_unicos = set()
    for row_id in tree.get_children():
        valor = tree.item(row_id)["values"][colunas.index(coluna)]
        valores_unicos.add(valor)
    return list(valores_unicos)

def aplicar_filtro(coluna):
    filtro = dropdown_filtro[coluna].get()
    for row_id in tree.get_children():
        valor = tree.item(row_id)["values"][colunas.index(coluna)]
        if valor != filtro:
            tree.detach(row_id)
        else:
            tree.reattach(row_id, '', '')
            tree.selection_add(row_id)

def atualizar_filtros():
    for coluna in colunas:
        dropdown_filtro[coluna]["values"] = criar_lista_valores(coluna)
        dropdown_filtro[coluna].set('')

def atualizar_lista(contagem_por_diretorio_e_data):
    tree.delete(*tree.get_children())  # Limpar a tabela antes de atualizar
    for diretorio, contagem_por_data in contagem_por_diretorio_e_data.items():
        for data, contagem in contagem_por_data.items():
            tree.insert("", tk.END, values=(diretorio, contagem, data))

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

# Definir as colunas
colunas = ["Nome", "Quantidade", "Data"]

# Criar dropdowns para filtragem
dropdown_filtro = {}
for coluna in colunas:
    frame_filtro = tk.Frame(janela)
    frame_filtro.pack(pady=5)
    label_filtro = tk.Label(frame_filtro, text=f"Filtrar por {coluna}:")
    label_filtro.grid(row=0, column=0)
    valores_filtro = criar_lista_valores(coluna)
    dropdown_filtro[coluna] = ttk.Combobox(frame_filtro, values=valores_filtro)
    dropdown_filtro[coluna].grid(row=0, column=1)
    dropdown_filtro[coluna].bind("<<ComboboxSelected>>", lambda event, coluna=coluna: aplicar_filtro(coluna))

# Botão para atualizar a busca
botao_atualizar = tk.Button(janela, text="Atualizar", command=atualizar_busca)
botao_atualizar.pack()

# Botão para limpar filtros
botao_limpar_filtros = tk.Button(janela, text="Limpar Filtros", command=atualizar_filtros)
botao_limpar_filtros.pack()

# Atualizar a busca inicial
atualizar_busca()

# Iniciar o loop da interface gráfica
janela.mainloop()
