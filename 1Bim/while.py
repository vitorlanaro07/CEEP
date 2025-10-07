
valor1,valor2, cont = 0, 0, 0

while cont < 2:
    while (valor1 < 20) or (valor1 > 40):
        valor1 = int(input("Informe um valor entre (20-40):"))
        if valor1 < 20:
            print("menor que 20")
        elif valor1 > 40:
            print("maior que 40")
        else:
            cont += 1

    while (valor2 < 41) or (valor2 > 60):
        if (valor2 < 41) or (valor2 > 60):
            valor2 = int(input("Informe um valor entre (41-60):"))
            if valor2 < 41:
                print("menor que 41")
            elif valor2 > 60:
                print("maior que 60")
            else:
                cont += 1
    # if valor3 == "" or valor3 < 18:
    #     valor3 = int(input("Entre com o valor 3:"))
    #     if valor3 < 18:
    #         print("menor de idade")
    #     else:
    #         cont += 1
