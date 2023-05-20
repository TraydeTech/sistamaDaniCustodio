'''
Criado por Jefferson Trayde
Data da criação 20/05/2023
Para empresa Dani Custodio Festas e Eventos

'''

clientes = []
produtos = []
tipoEvento = []

# CADASTRO DOS CLIENTES

def cadastrar_cliente():
    nome = input("Digite o nome do cliente: ")
    email = input("Digite o email do cliente: ")
    telefone = input("Digite o telefone do cliente: ")
    endereco = input("Digite o endereço completo:" )
    cliente = {"nome": nome, "email": email, "telefone": telefone, "endereco": endereco}
    clientes.append(cliente)
    print("Cliente cadastrado com sucesso!")

# CADASTRO DOS PRODUTOS

def cadastrar_produto():
    nome = input("Digite o nome do produto: ")
    preco = float(input("Digite o preço do produto: "))
    quantidade = int(input("Digite a quantidade em estoque: "))
    produto = {"nome": nome, "preco": preco, "quantidade": quantidade}
    produtos.append(produto)
    print("Produto cadastrado com sucesso!")

# CADASTRO DO TIPO DE EVENTO
    
def cadastrar_tipoEvento():
    evento = input("Digite o tipo do evento: ")
    diaDoEvento = input("Digite o dia que será realizado o evento: ")
    local = input("Digite o local do evento: ")
    endDoEvento = input("Digite o endereço completo do local a onde sera o Evento: ")
    evento = {"evento": evento, "local": local, "endDoEvento": endDoEvento, "diaDoEvento": diaDoEvento}
    tipoEvento.append(evento)
    print("Evento registrado com sucesso!")

# PESQUISA DOS CLIENTES

def exibir_clientes():
    print("---- Lista de Clientes ----")
    for cliente in clientes:
        print("Nome:", cliente["nome"])
        print("Email:", cliente["email"])
        print("Telefone:", cliente["telefone"])
        print("Endereço:",cliente["endereco"] )
        print("--------------------------")

# PEQUISA DOS PRODUTOS

def exibir_produtos():
    print("---- Lista de Produtos ----")
    for produto in produtos:
        print("Nome:", produto["nome"])
        print("Preço:", produto["preco"])
        print("Quantidade:", produto["quantidade"])
        print("--------------------------")

# PEQUISA DOS EVENTOS

def exibir_tipoEventos():
    print("---- Lista dos Eventos ----")
    for evento in tipoEvento:
        print("Evento:", evento["evento"])
        print("Dia do evento:", evento["diaDoEvento"])
        print("Local:", evento["local"])
        print("Endereço do evento:", evento["endDoEvento"])
        print("--------------------------")


# MENU DE CASTROS DE CLIENTES E PRODUTOS

def menu():
    while True:
        print("===== Cadastro de Clientes, Produtos e Eventos =====")
        print("1 - Cadastrar Cliente")
        print("2 - Cadastrar Produto")
        print("3 - Cadastrar Evento")
        print("4 - Exibir Clientes")
        print("5 - Exibir Produtos")
        print("6 - Exibir Eventos")
        print("0 - Sair")
        opcao = input("Digite a opção desejada: ")

        if opcao == "1":
            cadastrar_cliente()
        elif opcao == "2":
            cadastrar_produto()
        elif opcao == "3":
            cadastrar_tipoEvento()
        elif opcao == "4":
            exibir_clientes()
        elif opcao == "5":
            exibir_produtos()
        elif opcao == "6":
            exibir_tipoEventos()
        elif opcao == "0":
            print("Saindo do programa...")
            break
        else:
            print("Opção inválida. Por favor, tente novamente.")

menu()

