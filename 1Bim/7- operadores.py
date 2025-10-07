# Operadores relacionais

# Maior: 5 > 10 ? False
# Maior ou Igual: 5 >= 10 ? False
# Menor: 5 < 10 ? True
# Menor ou Igual: 10 <= 10 ? True
# Igual: 10 == 10 ? True
# Diferente: 5 != 10 ? True

# Podemos operar em cima de variaveis ou valores!
# print("-------------------------")
# print("O resultado dessa operaçao eh: ",5 > 6)

# x = "texto"
# y = "texto maior"
# z = "casca"

# print("var x eh diferente de var y?", x != y) #true

# print("o tipo de dado de x eh o mesmo que o de y?", type(x) == type(y)) #true

# print("x eh maior que y?", x > y) #false

# print("x eh menor ou igual a z?", x >= z); #true

# idadeVitor = 25
# idadePermitida = 18

# print("Vitor pode entrar na festa para maiores de idade?", idadePermitida <= idadeVitor)

# print("-------------------------")


# #Operadores Logicos (AND, OR, NOT)

# print("exemplo1:", 18 > 25 and 10 < 20) 
# print("exemplo2:",10 > 9 and 5 < 6)
# print("exemplo3:",10 != x and idadeVitor >= idadePermitida)

# print("exemplo4:",10 > 20 or 1 < 2)

# print("exemplo5:", "texto" != "lingua" or 2 < 2)

# print("exemplo6:", not(5 == 5))
# print("exemplo6:", not(5 > 6))
# print("-------------------------")


#if, elif, else

# 1. Peça dois números e exiba qual é o maior.
# numberOne = int(input("Informe um numero 1:"))
# numberTwo = int(input("Informe um numero 2:"))
# if (numberOne > numberTwo):
#     print("Numero 1 eh maior")
# elif (numberOne < numberTwo):
#     print("Numero 2 eh maior")
# else:
#     print("Numeros iguais")

#Peça a idade e classifique: 
# criança, adolescente, adulto ou idoso.
idade = int(input("qual a idade?"))

if(idade < 12):
    print("eh criança")
elif(idade < 18):
    print("eh adolescente")
elif(idade < 60):
    print("eh adulto")
else:
    print("eh idoso")

# 2. Peça dois números e exiba se são iguais ou diferentes.
# 3. Peça um número e informe se é positivo ou negativo.
# 4. Peça um número e informe se é par ou ímpar.
# 5. Peça a idade do usuário e diga se ele é maior de idade.

# idadePessoa = int(input("Qual sua idade?"))

# if(idadePessoa >= 18):
#     print("eh maior de idade")
# else:
#     print("eh menor de idade")

    

# nota1 = 6.0
# nota2 = 6.0
# nota3 = 6.0

# media = (nota1 + nota2 + nota3) / 3
# print(f'media: {media:.1f}')

# if media >= 6:
#     print("aprovado")
# elif media >= 5:
#     print("recuperaçao")
# else:
#     print("reprovado")

# print("-------------------------")

# x = 1
# y = 2
# z = 3

# if x > y or z > y:
#     print("pelo menor um valor precisa ser verdadeiro")


# if x < y and z < y:
#     print("os dois valores precisam ser verdadeiro")
# elif x < y and y < z:
#     print("deu bom!")
    