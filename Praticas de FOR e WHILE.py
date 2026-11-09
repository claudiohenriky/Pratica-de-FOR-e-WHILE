opcao = -1

while opcao != 0:
    print("\n===========================================================================")
    print("     SISTEMA DE PRÁTICA: WHILE E FOR     ")
    print("===========================================================================")
    print("1 - Testar Estrutura WHILE (Contagem Regressiva)")
    print("2 - Testar Estrutura FOR (Gerador de Tabuada)")
    print("0 - Sair do Sistema")

    opcao = int(input("\nEscolha uma opção: "))

    if opcao == 1:
        print("\n--- [DEMO WHILE}: Contagem Regressiava ---")
        inicio = int(input("Digite um número inteiro para iniciar "))

        while inicio >= 0:
            print(f"Contagem:{inicio}")
            inicio = inicio - 1
            
        print("✨ Fim da contagem!")

    elif opcao == 2:
        print("\n--- [DEMO FOR]: Gerador de Tabuada ---")
        num = int(input("Digite o numero da tabuada desejada: "))

        print(f"\nTabuada do {num}:")
        for i in range(1, 11):
            print(f"{num} x {i:2d} = {num * i}")

        print("✨ Tabuada gerada com sucesso!")

    elif opcao == 0:
        print("\nEncerrando o programa... Até logo!")

    else:
        print("\n❌ Opção inválida! Tente novamente.")
