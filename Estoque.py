print(" seja bem- vindo")
lista_de_produtos = []
while True:
    print(" escolha uma das opções: ")
    print("1: adicionar produto")
    print("2: listar produtos")
    print("3: remover produto")
    print("4: editar quantidade")
    print("5: calcular valor total")
    print("6: sair")
    try:
        num = int(input("digite um número de 1 a 6: "))
    except:
        print("Valor inválido!")
        continue
    if num == 1:
        print(" Você optou por adicionar produto")
        nome = input("digite o nome do produto: ")
        while True:
            try:
                quantidade = int(input("digite a quantidade desejada: "))
                break
            except:
                print("Valor invàlido!")
        while True:
            try:
                preco = float(input("digite o preço: "))
                break
            except:
                print("Valor inválido!")
        produto = {"nome": nome, "quantidade": quantidade, "preco": preco}
        lista_de_produtos.append(produto)
    elif num == 2:
        print(" Você optou por listar produtos")
        for produto in lista_de_produtos:
            print("nome:", produto["nome"], "| quantidade:", produto["quantidade"], "| preco : ", produto["preco"])
    elif num == 3:
        print("Você optou por remover produto")
        nome_remover = input(" digite o produto que você quer remover: ")
        encontrado = False
        for produto in lista_de_produtos:
            if produto["nome"] == nome_remover:
                print("Você optou por remover : ", produto["nome"])
                lista_de_produtos.remove(produto)
                encontrado = True
        if encontrado == False:
            print("Esse produto não existe no seu estoque")
    elif num == 4:
        print("Você optou por editar quantidade")
        nome_digitado = input("digite o produto que você quer editar a quantidade: ")
        encontrado = False
        for produto in lista_de_produtos:
            if produto["nome"] == nome_digitado:
              print("Você escolheu editar a quantidade do: ", produto["nome"])
              while True:
                try: 
                  nova_quantidade = int(input("digite a nova quantidade do produto a ser editado: "))
                  break
                except:
                  print("Valor inválido!")
              produto["quantidade"] = nova_quantidade
              encontrado = True
        if encontrado == False:
            print("Esse produto não existe no seu estoque: ")
    elif num == 5:
        print("Você optou por calcular o valor total")
        valor_total = 0
        for produto in lista_de_produtos:
            valor_total += produto["preco"] * produto["quantidade"]
        print(" o valor total dos seus produtos equivale a : ", valor_total)
    elif num == 6:
        print("Você optou por sair")
        break
    else:
        print("opção inválida")
