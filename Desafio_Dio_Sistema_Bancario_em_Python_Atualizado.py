

def menu():
    menu = """\n

    Bem-vindo(a) ao Banco Python!
    Escolha uma opção:

    [d] Depositar
    [s] Sacar
    [e] Extrato 
    [nc] Novo Conta
    [lc] Lista Contas
    [nu] Novo Usuário
    [q] Sair

    => """

    return input(menu)

def depositar(saldo, extrato, /):
    valor = float(input("Informe o valor do depósito: "))
    if valor > 0:
        saldo += valor
        extrato += f"Depósito: R$ {valor:.2f}\n"
        print(f"Depósito de R$ {valor:.2f} realizado com sucesso!")
    else:
        print("Operação falhou! O valor informado é inválido.")
    return saldo, extrato

def sacar(*,saldo, limite, extrato, numero_saques, LIMITE_SAQUES):
    print("O número máximo de saques é 3 por dia.")
    valor = float(input("Informe o valor do saque: "))
    if 0 < valor <= saldo and numero_saques < LIMITE_SAQUES and valor <= limite:
        saldo -= valor
        extrato += f"Saque: R$ {valor:.2f}\n"
        numero_saques += 1
        print(f"Saque de R$ {valor:.2f} realizado com sucesso!")
    else:
        print("Operação falhou! Verifique as condições e tente novamente.")
    return saldo, extrato

def exibir_extrato(saldo, / , * , extrato):
    print("\n================ EXTRATO ================\n")
    print(extrato if extrato else "Nenhuma transação realizada.")
    print(f"\nSaldo atual: R$ {saldo:.2f}")
    print("\n==========================================\n")

def criar_usuario(usuarios):
    cpf = input("Informe o CPF (somente números): ")
    usuario = filtrar_usuarios(cpf, usuarios)
    
    if usuario:
        print("Usuário já cadastrado.")
        return 
    
    nome = input("Informe o nome completo: ")
    data_nascimento = input("Informe a data de nascimento (dd/mm/aaaa): ")
    endereco = input("Informe o endereço (logradouro, nro - bairro - cidade/sigla estado): ")
    
    usuarios.append({
        'nome': nome,
        'cpf': cpf,
        'data_nascimento': data_nascimento,
        'endereco': endereco
    })
    
    print(f"Usuário {nome} cadastrado com sucesso!")
    

def filtrar_usuarios(cpf,usuarios):
    usuarios_filtrados = [usuario for usuario in usuarios if usuario['cpf'] == cpf]
    return usuarios_filtrados[0] if usuarios_filtrados else None

def criar_conta(agencia, numero_conta, usuarios):
    cpf = input("Informe o CPF do usuário: ")
    usuario = filtrar_usuarios(cpf, usuarios)
    
    if usuario:
        print("Conta criada com sucesso!")
        return {"agencia": agencia, "numero_conta": numero_conta, "usuario": usuario}
    
       
    print("Usuário não encontrado. Cadastre o usuário primeiro.")
   
    

def listar_contas(contas):
       
    print("\nLista de Contas:")
    for conta in contas:
        print(f"Agência: {conta['agencia']}, Número da Conta: {conta['numero_conta']}, Titular: {conta['usuario']['nome']}")

def main():
    LIMITE_SAQUES = 3
    AGENCIA = "0001"
    saldo = 0
    limite = 500
    extrato = ""
    numero_saques = 0
    usuarios = []
    contas = []
    
    while True:
        opcao = menu()

        if opcao == "d":
            saldo, extrato = depositar(saldo, extrato)

        elif opcao == "s":
            saldo, extrato = sacar(saldo=saldo, limite=limite, extrato=extrato, numero_saques=numero_saques, LIMITE_SAQUES=LIMITE_SAQUES)

        elif opcao == "e":
            exibir_extrato(saldo, extrato=extrato)

        elif opcao == "nc":
            numero_conta = len(contas) + 1
            conta = criar_conta(AGENCIA, numero_conta, usuarios)

            if conta:
                contas.append(conta)

        elif opcao == "lc":
            listar_contas(contas)

        elif opcao == "nu":
            criar_usuario(usuarios)

        elif opcao == "q":
            print("Obrigado por usar o Banco Python! Até logo!")
            break

        else:
            print("Opção inválida! Por favor, escolha uma opção válida.")


main()                    