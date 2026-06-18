restaurante = [
    [1, "lanche", 5, 1],
    [2, "refrigerante", 10, 2],
    [3, "doce", 15, 5]
]
produtoID = 11
while True:
    print("restaurante")
    print("1 - Novo item")
    print("2 - produto ")
    print("3 -Id")
    print("4 - Mudar quantidade")
    print("5 - Sair")
    opcao = input("Escolha uma opcao: ")
    if opcao == "1":
        print("\n Novo item")
        nome = input("Nome do produto: ")
        qtd = int(input("Quantidade que chegou: "))
        restaurante.append([produtoID, nome, 0, qtd])
        print(f"Adicionado o id é {produtoID}")
        produtoID = produtoID + 1
    elif opcao == "2":
        print("\n Itens no estoque:")
        if len(restaurante) == 0:
            print("Falta de produto")
        else:
            for item in restaurante:
                print(f"id: {item[0]} | {item[1]} | {item[2]} | {item[3]}")
    elif opcao == "3":
        print("\nBuscar por ID:")
        id_busca = int(input("Digite o id "))
        encontrou = False
        for item in restaurante:
            if item[0] == id_busca:
                print(f" id: {item[0]} | {item[1]} |  {item[2]} | {item[3]}")
                encontrou = True
                break
        if encontrou== False:
            print("Não tem o id")
    elif opcao == "4":
        print("Mudar Quantidade")
        id_busca = int(input("Digite o id: "))
        encontrou = False
        for item in restaurante:
            if item[0] == id_busca:
                encontrou = True
                print(f"Produto: {item[1]} (Tem {item[3]} no estoque)")
                print("1 - Adicionar | 2 - Excluir ")
                tipo = input("Vai fazer o que ")
                quantos = int(input("Quantas unidades "))
                if tipo == "1":
                    item[3] = item[3] + quantos
                    print(f"Atualizado! Agora tem {item[3]} unidades.")
                elif tipo == "2":
                    if item[3] >= quantos:
                        item[3] = item[3] - quantos
                        print(f" Sobraram {item[3]} unidades.")
                    else:
                        print(f" Não tem como retirar essa quantidade{item[3]}.")
                break
        if encontrou == False:
            print("não tem o id")
    elif opcao == "5":
        print("Saindo")
        break


##FIZ COM RYAN
