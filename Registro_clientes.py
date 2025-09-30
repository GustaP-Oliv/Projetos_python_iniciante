#com esse código consegui fazer o que eu queria e lembrei de adicionar o campo id e cep

# Registro de Clientes em Python com Interface Gráfica
import tkinter as tk
from tkinter import messagebox, simpledialog
import json
import os

ARQUIVO = "clientes.json"

# Funções de arquivo
def carregar_clientes():
    if os.path.exists(ARQUIVO):
        with open(ARQUIVO, "r") as f:
            return json.load(f)
    return []

def salvar_clientes(clientes):
    with open(ARQUIVO, "w") as f:
        json.dump(clientes, f, indent=4)

# Funções do sistema 
def gerar_id():
    if clientes:
        return max(c["id"] for c in clientes) + 1
    else:
        return 1

def cadastrar_cliente():
    nome = simpledialog.askstring("Cadastro", "Nome do cliente:")
    if not nome:
        return
    email = simpledialog.askstring("Cadastro", "Email do cliente:")
    telefone = simpledialog.askstring("Cadastro", "Telefone do cliente:")
    
    sexo = simpledialog.askstring("Cadastro", "Sexo do cliente (M/F/Outro):")
    if sexo and sexo.lower() == "outro":
        sexo = simpledialog.askstring(
            "Cadastro", 
            "Informe a denominação (Ex: Não-binário, Agênero, Prefiro não informar):"
        )

    idade = simpledialog.askinteger("Cadastro", "Idade do cliente:")
    cpf = simpledialog.askstring("Cadastro", "CPF do cliente:")
    cep = simpledialog.askstring("Cadastro", "CEP do cliente:")

    cliente = {
        "id": gerar_id(),
        "nome": nome,
        "email": email,
        "telefone": telefone,
        "sexo": sexo,
        "idade": idade,
        "cpf": cpf,
        "cep": cep
    }
    clientes.append(cliente)
    salvar_clientes(clientes)
    atualizar_lista()
    messagebox.showinfo("Sucesso", f"Cliente {nome} cadastrado!")

def remover_cliente():
    selecionado = lista.curselection()
    if not selecionado:
        messagebox.showwarning("Erro", "Selecione um cliente para remover!")
        return
    indice = selecionado[0]
    removido = clientes.pop(indice)
    salvar_clientes(clientes)
    atualizar_lista()
    messagebox.showinfo("Removido", f"Cliente {removido['nome']} removido.")

def buscar_cliente():
    termo = simpledialog.askstring("Buscar", "Digite o nome do cliente:")
    if not termo:
        return
    resultados = [c for c in clientes if termo.lower() in c["nome"].lower()]
    if resultados:
        nomes = "\n".join([
            f"ID:{c['id']} | {c['nome']} | {c['email']} | {c['telefone']} | {c['sexo']} | {c['idade']} anos | CPF: {c['cpf']} | CEP: {c['cep']}"
            for c in resultados
        ])
        messagebox.showinfo("Resultados", nomes)
    else:
        messagebox.showinfo("Resultados", "Nenhum cliente encontrado.")

def atualizar_lista():
    lista.delete(0, tk.END)
    for c in clientes:
        lista.insert(
            tk.END,
            f"ID:{c['id']} | {c['nome']} | {c['email']} | {c['telefone']} | {c['sexo']} | {c['idade']} anos | CPF: {c['cpf']} | CEP: {c['cep']}"
        )

# Janela principal
clientes = carregar_clientes()

root = tk.Tk()
root.title("Sistema de Clientes")
root.geometry("500x300")

# Lista de clientes
lista = tk.Listbox(root, width=135, height=16
)
lista.pack(pady=4)

# Botões
frame = tk.Frame(root)
frame.pack()

btn_add = tk.Button(frame, text="Cadastrar", command=cadastrar_cliente)
btn_add.grid(row=0, column=0, padx=5)

btn_remover = tk.Button(frame, text="Remover", command=remover_cliente)
btn_remover.grid(row=0, column=1, padx=5)

btn_buscar = tk.Button(frame, text="Buscar", command=buscar_cliente)
btn_buscar.grid(row=0, column=2, padx=5)

btn_sair = tk.Button(frame, text="Sair", command=root.quit)
btn_sair.grid(row=0, column=3, padx=5)

# Atualiza lista inicial
atualizar_lista()

root.mainloop()

