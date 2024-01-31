import os
import datetime
import tkinter as tk

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

def atualizar_lista(contagem_por_diretorio_e_data):
    lista_resultados.delete(0, tk.END)
    for diretorio, contagem_por_data in contagem_por_diretorio_e_data.items():
        for data, contagem in contagem_por_data.items():
            lista_resultados.insert(tk.END, f"{diretorio:<10} {contagem:<11} {data}")

# Defina seus diretórios aqui
diretorios = ["/caminho/do/seu/diretorio1", "/caminho/do/seu/diretorio2"]

# Criar janela principal
janela = tk.Tk()
janela.title("Contagem de Arquivos por Data")

# Criar lista para exibir os resultados
lista_resultados = tk.Listbox(janela, width=50, height=20)
lista_resultados.pack(pady=10)

# Botão para atualizar a busca
botao_atualizar = tk.Button(janela, text="Atualizar", command=atualizar_busca)
botao_atualizar.pack()

# Atualizar a busca inicial
atualizar_busca()

# Iniciar o loop da interface gráfica
janela.mainloop()
