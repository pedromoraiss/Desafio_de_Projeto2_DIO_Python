def menu():
    menu = """
    ================ MENU ================

    [d] Depositar
    [s] Sacar
    [e] Extrato
    [q] Sair
    [nu] Novo usuário
    [nc] Nova Conta

    ======================================
    => """
    return input(menu)

def deposito(valor, saldo, extrato):
    if valor > 0:
        saldo += valor
        extrato += str(f"Depósito:\tR$ {valor:.2f}\n")
    else:
        print("Operação falhou! O valor informado é inválido.")
    return saldo, extrato

def saque(*, saldo, valor, extrato, limite, numero_saques, LIMITE_SAQUES):
    excedeu_saldo = valor > saldo
    excedeu_limite = valor > limite
    excedeu_saques = numero_saques >= LIMITE_SAQUES

    if excedeu_saldo:
        print("Operação falhou! Você não tem saldo suficiente.")
    elif excedeu_limite:
        print("Operação falhou! O valor do saque excede o limite.")
    elif excedeu_saques:
        print("Operação falhou! Número máximo de saques excedido.")
    elif valor > 0:
        saldo -= valor
        extrato += f"Saque:\t\tR$ {valor:.2f}\n"
        numero_saques += 1
    else:
        print("Operação falhou! O valor informado é inválido.")
    return saldo, extrato, numero_saques

def exibir_extrato(saldo, /, *, extrato):
        print("\n================ EXTRATO ================")
        print("Não foram realizadas movimentações." if not extrato else extrato)
        print(f"\nSaldo: R$ {saldo:.2f}")
        print("==========================================")

def criar_usuario(lista_usuarios): #função para criar os novos usuarios
    cpf = input("Digite o seu CPF (somente os números): ")
    usuario = filtrar_usuario(cpf, lista_usuarios) #Usa a função filtrar_usuario para verificar se existe usuario com cpf cadastrado

    if usuario:
        print("Já existe usuário com esse CPF!")
        return
    
    nome = input("Informe seu nome completo: ")
    data_nascimento = input("Informe a data de nascimento (DD/MM/AAAA): ")
    endereco = input("Informe seu endereço: ")

    lista_usuarios.append({
        "nome": nome,
        "data_nascimento": data_nascimento,
        "cpf": cpf,
        "endereco": endereco
    })

    print("Usuário criado com sucesso!")


def filtrar_usuario(cpf, lista_usuarios):
    usuarios_filtrados = [usuario for usuario in lista_usuarios if usuario["cpf"] == cpf] # Verifica se o usuario na lista de usarios ja tem cpf cadastrado, se sim ele retornao usuario;
    return usuarios_filtrados[0] if usuarios_filtrados else None #Se usuarios_filtrados nao for uma lista vazia ele vai retornar o primeiro elemento

def criar_conta(agencia, numero_conta, lista_usuarios):
    cpf = input("Informe o CPF do usuário: ")
    usuario = filtrar_usuario(cpf, lista_usuarios)

    if usuario:
        print("Conta criada com sucesso!")
        return {"agencia": agencia, "numero_conta": numero_conta, "usuario": usuario}
    
    print("Usuário não encontrado!")

def main ():
    LIMITE_SAQUES = 3
    AGENCIA = "0001"

    saldo = 0
    limite = 500
    extrato = ""
    numero_saques = 0
    lista_usuarios = []
    lista_contas = []

    while True:

        opcao = menu()

        if opcao == "d":
            valor = float(input("Informe o valor do depósito: "))

            saldo, extrato = deposito(valor, saldo, extrato)    

        elif opcao == "s":
            valor = float(input("Informe o valor do saque: "))

            saldo, extrato, numero_saques = saque(saldo = saldo, valor = valor, extrato = extrato, limite = limite, numero_saques = numero_saques, LIMITE_SAQUES = LIMITE_SAQUES)

        elif opcao == "e":
            exibir_extrato(saldo, extrato = extrato)

        elif opcao == "nu":
            criar_usuario(lista_usuarios)
        
        elif opcao == "nc":
            numero_conta = len(lista_contas) + 1
            conta = criar_conta(AGENCIA, numero_conta, lista_usuarios)

            if conta:
                lista_contas.append(conta)

        elif opcao == "q":
            break
        else:
            print("Operação inválida, por favor selecione novamente a operação desejada.")

main()
