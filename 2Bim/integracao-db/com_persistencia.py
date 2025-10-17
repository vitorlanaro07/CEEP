

opcao = ""
# lista_nomes_paciente = []
# lista_idade_paciente = []


while opcao != 0:
    print("---- MENU ----")
    print("1 - Cadastrar Paciente")
    print("2 - Listar Paciente")
    # print("3 - Buscar Paciente")
    print("0 - Sair")
    opcao = int(input("Informe qual opção: "))


    if opcao == 1:
        print("-------------------------------------------")
        nome_temp = input(f"Informe o nome do paciente:")
        idade_temp = input(f"Informe a idade do paciente:")

        with open('dados.txt', "a") as f:

            f.write(f"Nome do Paciente: ")
            f.write(nome_temp)
            f.write("\n") # \n é um caractere especial para pular uma linha
            f.write(f"Idade do Paciente: ")
            f.write(idade_temp)
            f.write("\n") 
            
            print("Dados escritos com sucesso!")
            print("-------------------------------------------")
    elif opcao == 2:
        with open("dados.txt", "r") as f:
            print(f.read())
            f.close()
        # if len(lista_nomes_paciente) != 0:
        #     contador = 0
        #     while contador < len(lista_nomes_paciente):
        #         print("-------------------------------------------")
        #         print(lista_nomes_paciente[contador])
        #         print(lista_idade_paciente[contador])
        #         contador += 1
        # else:
        #     print("-------------------------------------------")
        #     print("Precisa ter pelo menos paciente cadastrado")
        #     print("-------------------------------------------")

