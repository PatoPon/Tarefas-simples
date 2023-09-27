#interface.py

import tkinter as tk
from tkinter import messagebox
import logica

def adicionar():
    nova_tarefa = entrada_tarefa.get()
    logica.adicionar_tarefa(tarefas, nova_tarefa)
    entrada_tarefa.delete(0, tk.END)
    atualizar_lista()

def deletar():
    inp = entrada_tarefa.get()
    try:
        selecao = int(inp)
    except ValueError:
        selecao = str(inp)
    logica.deletar_tarefa(tarefas, selecao)
    entrada_tarefa.delete(0, tk.END)
    atualizar_lista()

def salvar():
    if tarefas:
        logica.salvar_tarefas(tarefas, 'tarefas.txt')
        messagebox.showinfo("Salvo!", "Tarefas salvas com sucesso!")
    else:
        messagebox.showinfo("ERRO", "Nenhuma tarefa para salvar.")

def carregar():
    if logica.carregar_tarefas(tarefas, 'tarefas.txt'):
        atualizar_lista()
        messagebox.showinfo("Carregado!", "Tarefas carregadas com sucesso!")
    else:
        messagebox.showinfo("ERRO", "Nenhuma tarefa para carregar.")

janela = tk.Tk()
janela.title("Lista de Tarefas")
janela.iconbitmap("icon.ico")
janela.resizable(False, False)

largura_janela = 800
altura_janela = 420

x_pos = (janela.winfo_screenwidth() - largura_janela) // 2
y_pos = (janela.winfo_screenheight() - altura_janela) // 2

janela.geometry(f"{largura_janela}x{altura_janela}+{x_pos}+{y_pos}")

tarefas = []

entrada_tarefa = tk.Entry(janela, font=("Arial", 14))
entrada_tarefa.pack(pady=10)

lista_tarefas = tk.Listbox(janela, selectmode=tk.SINGLE, font=(
    "Arial", 12), width=70, height=15)
lista_tarefas.pack()

frame_botoes = tk.Frame(janela)
frame_botoes.pack(side=tk.BOTTOM, padx=10, pady=10)

btn_adicionar = tk.Button(frame_botoes, text="Adicionar",
                          command=adicionar, font=("Arial", 12),
                          bg="lime")
btn_deletar = tk.Button(frame_botoes, text="Deletar",
                        command=deletar, font=("Arial", 12),
                        bg="red")
btn_salvar = tk.Button(frame_botoes, text="Salvar",
                       command=salvar, font=("Arial", 12),
                       bg="yellow")
btn_carregar = tk.Button(frame_botoes, text="Carregar",
                         command=carregar, font=("Arial", 12),
                         bg="yellow")

btn_adicionar.pack(side=tk.LEFT, padx=5)
btn_deletar.pack(side=tk.LEFT, padx=5)
btn_salvar.pack(side=tk.LEFT, padx=5)
btn_carregar.pack(side=tk.LEFT, padx=5)

def atualizar_lista():
    lista_tarefas.delete(0, tk.END)
    for indice, tarefa in enumerate(tarefas, start=1):
        lista_tarefas.insert(tk.END, f"{indice}. {tarefa}")

janela.mainloop()