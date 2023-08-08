menu = """

[1] Depositar
[2] Sacar
[3] Extrato
[0] Sair

=> """

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_DE_SAQUE = 3

while True:
    
    opcao = input(menu)

    if opcao == "1":
        valor = float(input("Informe o valor do depósito:"))

        if valor > 0:
            saldo += valor
            extrato += f"Depósito: R$ {valor:.2f}\n"
        else:
            print("Valor inválido, operação cancelada!")
    
    elif opcao == "2":
        valor = float(input("Digite o valor do saque:"))
        
        excedeu_saldo = valor > saldo
        excedeu_limite = valor > limite
        excedeu_saques = numero_saques >= LIMITE_DE_SAQUE

        if excedeu_saldo:
            print("Falha! Saldo Insuficiente!")
        elif excedeu_limite:
            print("Falha! O valor informado excede o limite!")
        elif excedeu_saques:
            print("Falha! Excede o número de saque!")
        elif valor > 0:
            saldo -= valor
            extrato += f'Saque: R$ {valor:.2f}'
            numero_saques += 1
        else:
            print("Falha! O valor informado é inválido!")

    elif opcao == "3":
        print("\n===============EXTRATO===============")
        print("Não foram realizadas movimentações!"if not extrato else extrato)
        print(f"\nSaldo: R$ {saldo:.2f}")
        print("=======================================")

    elif opcao == "0":
        break

    else:
        print("Operação inválida!")
    
    

        



