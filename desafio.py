menu = """

[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair

=> """

saldo = 0
limite = 500
numero_saques = 0
LIMITE_SAQUES = 3
saques = []
depositos = []

while True:
    opcao = input(menu)

    if opcao == "d":
        valor = int(input("Digite o valor que deseja depositar: "))
        if valor <= 0:
            print("Por favor, digite um valor maior que zero para efetuar o depósito.")
            break
        
        saldo += valor
        depositos.append(valor)
        print(f"Você depositou {valor} reais. Seu novo saldo é de: {saldo} reais.")

    elif opcao == "s":
        if saldo == 0:
            print("Desculpe, você não tem saldo disponível")
            break

        if numero_saques == LIMITE_SAQUES:
            print(f"Desculpe, você já fez os {LIMITE_SAQUES} saques diários.")
            break

        valor = int(input("Digite o valor que deseja sacar: "))
        if valor > 500:
            print(f"Seu limite de saque é de {limite} reais.")
            break

        if valor > saldo:
            print(f"Você não tem saldo suficiente para sacar esse valor. Seu saldo é de: {saldo} reais.")
            break   

        saldo -= valor
        numero_saques += 1
        saques.append(valor)
        print(f"Você sacou {valor} reais. Seu novo saldo é de: {saldo} reais.")

    elif opcao == "e":
        if saques:
            print(f"Você realizou {len(saques)} saques. Foram eles:")
            for saque in saques:
                print("R$ %.2f" % saque) 

        if depositos:
            print(f"Você efetuou {len(depositos)} depósitos. Foram eles:")
            for deposito in depositos:
                print("R$ %.2f" % deposito)

        print("Seu saldo atual é de R$ %.2f" % saldo)

    elif opcao == "q":
        break

    else:
        print("Operação inválida, por favor selecione novamente a operação desejada.")
