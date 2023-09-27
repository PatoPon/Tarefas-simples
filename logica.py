# logica.py

def adicionar_tarefa(tarefas, nova_tarefa):
    if nova_tarefa:
        tarefas.append(nova_tarefa)


def deletar_tarefa(tarefas, texto):
    try:
        if type(texto) == int:
            tarefas.pop(int(texto)-1)
        else:
            tarefas.remove(texto)
    except IndexError:
        pass

def salvar_tarefas(tarefas, arquivo):
    with open(arquivo, 'w') as f:
        for tarefa in tarefas:
            f.write(tarefa + '\n')

def carregar_tarefas(tarefas, arquivo):
    tarefas.clear()
    try:
        with open(arquivo, 'r') as f:
            tarefas.extend(f.read().splitlines())
        return True
    except FileNotFoundError:
        return False
    except Exception as e:
        return False