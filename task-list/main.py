entrada = 0
lista_tarefas = []

while entrada != 5:
    
    sair = 0
    print (
        f"=========MENU=========\n"
        f"1 - Adicionar tarefa\n"
        f"2 - Mostrar tarefas\n"
        f"3 - Remover tarefas\n"
        f"4 - Ordenar tarefas\n"
        f"5 - Sair\n"
            
    )
    entrada = int(input("Escolha: "))

    if entrada == 1:               
        nova_tarefa = input("Adicione uma nova tarefa a lista: ")
        lista_tarefas.append(nova_tarefa)
       
    elif entrada == 2:
        if len(lista_tarefas) == 0:
            print("Nenhuma tarefa cadastrada.")
        else:
            for tarefa in lista_tarefas:
                print(f"- {tarefa}")
        
        
    elif entrada == 3:
            remover = (input("Qual tarefa deseja remover?  "))
            while remover not in lista_tarefas:
                 print("tarefa nao encontrada")
                 remover = input("tente novamente")
            lista_tarefas.remove(remover)
            print("Tarefa removida")
    elif entrada == 4:
        print("Lista ordenada:")

        for tarefa in lista_tarefas:
            print(f"- {tarefa}")

    elif entrada == 5:
        print("programa encerrado")
    
    else:
        print("comando não localizado")