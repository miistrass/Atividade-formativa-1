while True:
    # Opções do menu principal
    print("Escolha uma das opções")
    print("1. Estudantes")
    print("2. Professores")
    print("3. Disciplinas")
    print("4. Turmas")
    print("5. Matrículas")
    print("0. Sair")

    # Coleta da escolha
    opcao = int(input("Digite uma opção válida: "))

    if opcao > 0 and opcao <= 5:
        print(f"Você escolheu a opção: {opcao}")

        while True:
            # Menu secundário
            print(f"Menu de operações - Opção {opcao}")
            print("1. Listar")
            print("2. Criar")
            print("3. Atualizar")
            print("4. Excluir")
            print("5. Voltar ao menu anterior")
            opcao_secundaria = int(input("Digite uma opção válida: "))

            if opcao_secundaria < 5:
                print(f"Você escolheu a opção {opcao_secundaria}.")

            elif opcao_secundaria == 5:
                print("Você escolheu voltar ao menu anterior")
                break

            else:
                print("Você digitou uma opção secundária inválida.")

    elif opcao == 0:
        print("Você pediu para sair")
        break
    else:
        print("Você não digitou uma opção válida, por favor, digite uma opção válida: ")

