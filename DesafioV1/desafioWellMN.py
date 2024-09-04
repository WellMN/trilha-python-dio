menu = """

[d] Depositar
[s] Sacar sem taxa
[x] Sacar extra com taxa
[e] Extrato
[q] Sair

=> """

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3
TARIFA_SAQUE_EXTRA = 5


while True:

    opcao = input(menu)

    if opcao == "d":
        valor = float(input("Informe o valor do depósito: "))

        if valor > 0:
            saldo += valor
            extrato += f"Depósito: R$ {valor:.2f}\n"

        else:
            print("Operação falhou! O valor informado é inválido.")

    elif opcao == "s":
        valor = float(input("Informe o valor do saque: "))

        excedeu_saldo = valor > saldo

        excedeu_limite = valor > limite

        excedeu_saques = numero_saques >= LIMITE_SAQUES

        if excedeu_saldo:
            print("Operação falhou! Você não tem saldo suficiente.")

        elif excedeu_limite:
            print("Operação falhou! O valor do saque excede o limite.")

        elif excedeu_saques:
            print("Operação falhou! Número máximo de saques contratado foi excedido.\n\n Observação: Você ainda poderá efetuar saques com custo adicional.\n\n Utilize a opção com taxa. ")

        elif valor > 0:
            saldo -= valor
            extrato += f"Saque: R$ {valor:.2f}\n"
            numero_saques += 1

    elif opcao == "x":
        if numero_saques <3:
            print("Operação somente permitida após esgotar a franquia de saques")
        else:    

            valor = float(input("Informe o valor do saque adicional: "))

            excedeu_saldo = valor+TARIFA_SAQUE_EXTRA > saldo

            #Valor de limite não deve contemplar tarifas
            excedeu_limite = valor > limite 

            #excedeu_saques = numero_saques >= LIMITE_SAQUES

            if excedeu_saldo:
                print("Operação falhou! Você não tem saldo suficiente.")

            elif excedeu_limite:
                print("Operação falhou! O valor do saque excede o limite.")

            #elif excedeu_saques:
            #   print("Operação falhou! Número máximo de saques excedido.")

            elif valor > 0:
                saldo -= valor+TARIFA_SAQUE_EXTRA
                extrato += f"Saque: R$ {valor:.2f}\n"
                extrato += f"Tarifa para saque além da franquia: R$ {TARIFA_SAQUE_EXTRA:.2f}\n"
                #numero_saques += 1

            else:
                print("Operação falhou! O valor informado é inválido.")

    elif opcao == "e":
        print("\n================ EXTRATO ================")
        print("Não foram realizadas movimentações." if not extrato else extrato)
        print(f"\nSaldo: R$ {saldo:.2f}")
        print("==========================================")

    elif opcao == "q":
        break

    else:
        print("Operação inválida, por favor selecione novamente a operação desejada.")