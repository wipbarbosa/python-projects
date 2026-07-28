lista_compras = []
entrada = int(input("Lista de compras digite 0 para iniciar: "))
while entrada != 0:
    entrada = int(input("tente novamente: "))

while True:

    print (
        f"===== lista de compras =====\n"
        f"1 - Adicionar novo item\n"
        f"2 - Remover item\n"
        f"3 - Pesquisar produtos\n"
        f"4 - Ordenar produtos\n"
        f"5 - Mostrar produtos\n"
        f"6 - Limpar lista\n"
        f"7 - Sair\n"
        
    )
    entrada = int(input("Comando: "))
    
    if entrada == 1:
        novo_item = input(f"Digite o item que deseja adicionar: ").lower()
        lista_compras.append(novo_item)
        print(f"Novo item adicionado")
    
    elif entrada == 2:
        remover = input("Qual item deseja remover? ").lower()
        while remover not in lista_compras:
            remover = input("tente novamente").lower()
        
        lista_compras.remove(remover)
        print("Item removido com sucesso")
    
    elif entrada == 3:
        pesquisar = input("Oque procura?").lower()
        if pesquisar in lista_compras:
            print("Está na lista")
        else:
            print("Não está na lista")
    
    elif entrada == 4:
        print("Lista Ordenada")
        lista_compras.sort()
        for novo_item in lista_compras:
            print(f"-{novo_item}")
    elif entrada == 5:
        for novo_item in lista_compras:
            print(
                "Lista de Compras"
                f" - {novo_item}"
                )
    elif entrada == 6:
        lista_compras.clear()
        print(f"lista de compras limpa: {lista_compras}")

    elif entrada == 7:
        print("Programa encerrado")
        break

        