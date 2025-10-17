
opcao = ""
lista_nomes_paciente = []
lista_idade_paciente = []
id_paciente = 0

while opcao != 0:
    print("---- MENU ----")
    print("1 - Cadastrar Paciente")
    print("2 - Listar Paciente")
    # print("3 - Buscar Paciente")
    print("0 - Sair")
    opcao = int(input("Informe qual opção: "))


    if opcao == 1:
        print("-------------------------------------------")
        nome_temp = input(f"Informe o nome do paciente {id_paciente}:")
        lista_nomes_paciente.append(nome_temp)
        idade_temp = int(input(f"Informe a idade do paciente {id_paciente}:"))
        lista_idade_paciente.append(idade_temp)

    elif opcao == 2:
        if len(lista_nomes_paciente) != 0:
            contador = 0
            while contador < len(lista_nomes_paciente):
                print("-------------------------------------------")
                print(lista_nomes_paciente[contador])
                print(lista_idade_paciente[contador])
                contador += 1
        else:
            print("-------------------------------------------")
            print("Precisa ter pelo menos paciente cadastrado")
            print("-------------------------------------------")

