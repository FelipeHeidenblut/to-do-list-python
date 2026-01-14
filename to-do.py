# DEFINIÇÃO DAS FUNÇÕES
def adicionar_tarefa():
    with open("to_do_list.txt", "a") as arquivo:
        texto = input("Digite a nova tarefa:\n") + "\n"
        arquivo.write(texto)

def listar_tarefas():
    try:
        with open("to_do_list.txt", "r") as arquivo:
            conteudo = arquivo.read()
            print("\nSUAS TAREFAS:\n")
            print(conteudo)

    except:
        print("Lista ainda não criada")


# INICIO DO PROGRAMA
print("Iniciando o seu To-do List...")

while True:
    try:
        print("Escolha a opção desejada\n")
        opcao = int(input("1- Nova tarefa\n2- Listar tarefas\n0- Sair:\n"))

        if opcao == 1:
            adicionar_tarefa()
        elif opcao == 2:
            listar_tarefas()
        elif opcao == 0:
            print("Encerrando o programa...")
            break
        else:
            print("Opção inválida!")
    
    except:
        print("Digite apenas números!")
