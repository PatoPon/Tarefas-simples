def adicionar_tarefa():

    tar = str(input("Qual a nova tarefa? "))
    tarefas.append(tar)
    comecar()

def ver_tarefas():

    if (len(tarefas) == 0): print("Você não tem tarefas!"); return comecar()

    for i in range(len(tarefas)):
        print(f'{i+1}. {tarefas[i]}')
    
    comecar()

def deletar_tarefa():

    try:
        numero_tarefa = int(input("Qual o número da tarefa que deseja deletar? "))
        if 1 <= numero_tarefa <= len(tarefas):
            tarefas.pop(numero_tarefa - 1)  # Subtrai 1 para ajustar o índice da lista
            print(f"Tarefa {numero_tarefa} deletada com sucesso.")
            comecar()
        else:
            print("Número de tarefa inválido.")
            deletar_tarefa()
    except ValueError:
        print("Por favor, insira um número válido.")
        deletar_tarefa()

def salvar_tarefas():

    if (len(tarefas) == 0): print("Você não tem tarefas!"); return comecar()
    
    with open('tarefas.txt', 'w') as arquivo:
        for tarefa in tarefas:
            arquivo.write(tarefa + '\n')
    print("Tarefas salvas com sucesso!")
    comecar()

def carregar_tarefas():
    tarefas.clear()
    try:
        with open('tarefas.txt', 'r') as arquivo:
            tarefas.extend(arquivo.read().splitlines())
        print("Tarefas carregadas com sucesso!")
        comecar()
    except FileNotFoundError:
        print("Arquivo de tarefas não encontrado. Tente salvar um novo arquivo!")
        comecar()

def sair():
    print("Saindo...")

tarefas = []

opcoes = {
    "1": adicionar_tarefa,
    "2": ver_tarefas,
    "3": deletar_tarefa,
    "4": salvar_tarefas,
    "5": carregar_tarefas,
    "6": sair
}

def comecar():

    opcao = input("1 para adicionar, 2 para ver, 3 para deletar, 4 para salvar, 5 para carregar e 6 para sair ")

    if opcao in opcoes:
        opcoes[opcao]()
    else:
        print("Tente novamente!")
        comecar()

comecar()