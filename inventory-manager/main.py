inventario = []

while True:
    print(
        f"Menu de configuração do inventario\n"
        f"1 - Adicinar Produto\n"
        f"2 - Exibir Produtos\n"
        f"3 - Procurar produtos\n"
        f"4 - Atualizar Produtos\n"
        f"5 - Remover Produtos\n"
        f"6 - Sair\n"
        )
    entrada = int(input("Digite a opção escolhida:"))

    if entrada == 1:
        print ("Adicionar Produto")
        produto = {

        "nome": input(f"nome: ").lower(),
        "preço": float(input("preço: ")),
        "estoque": int(input(f"estoque: "))
        }

        inventario.append(produto)
        print("Produto adicionado com sucesso!")
    
    elif entrada == 2:
        if len(inventario) == 0:
            print("Inventario vazio")

        else:
            print("=" * 25)
            print("Lista de Produtos: ")
            
            for produto in inventario:
                print("=" * 25)


                for key, value in produto.items():
                    print(f"{key.capitalize():<8}: {value}")

                print("=" * 25)
    
    elif entrada == 3:
        if len(inventario) == 0:
            print("Inventario vazio")
        
        else:
            print("=" * 25)
            print("Procurar produtos:")
            procura_produto = input("Qual produto voce procura? ").lower()
            found = False

            for produto in inventario:
                if procura_produto == produto["nome"]:
                    print("Produto encontrado!")
                    print("=" * 25)
                    for key,value in produto.items():
                        print(f"{key.capitalize():<8}: {value}")
                        print("=" * 25)
                    found = True
                    break
            if not found:
                print("Produto não encontrado.")


    elif entrada == 4:
        if len(inventario) == 0:
            print("Inventario vazio")

        else:
            print("Atualizar produtos")
            atualizar_inventario = input("Qual produto quer atualizar?").lower()
            inventario_found = False

            for produto in inventario:

                if (atualizar_inventario == str(produto.get("nome", "")).lower() or
                    atualizar_inventario == str(produto.get("preço", "")) or
                    atualizar_inventario == str(produto.get("estoque", ""))):
                    print("Encontrado!")
                    print("=" * 25)

                    inventario_found = True
            
                    atualizar_produto = input("Oque deseja atualizar no produto?")
                    produto_found = False

                    for value in produto:
                        if atualizar_produto == value:
                            print("Encontrado")
                            novo_valor = input("Diagite o novo valor:")
                            produto[atualizar_produto] = novo_valor
                            produto_found = True
                            break
                    if not produto_found:
                        print("Campo não encontrado.")

            if not inventario_found:
                print("Produto não encontrado.")
            break
    
    elif entrada == 5:
        if len(inventario) == 0:
            print("Inventario vazio")

        else:
            remover_produto = input("Qual produto deseja remover?").lower()
            found = False


            for produto in inventario:
                if produto["nome"] == remover_produto:
                    inventario.remove(produto)
                    print(f"Produto '{remover_produto}' removido com sucesso!")
                    found = True
                    break

            if not found:
                print("Produto não encontrado no inventário.")

    
    elif entrada == 6:
        break
    else:
        print("Digite um codigo correto")

