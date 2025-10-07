# Exercicio 1
# nome = input("Qual seu nome?")
# sobrenome = input("Qual o seu sobrenome?")
# telefone = input("Qual seu telefone?")
# print(f"Meu nome eh {nome} {sobrenome} e meu numero de telefone eh {telefone}")

#Exercicio 2
# varInt = 1
# varStr = "Ola"
# varFloat = 0.67
# varBool = True 

# print(f"varInt: {varInt}, Tipo de dado: {type(varInt).__name__}") #a funçao type() retorna o tipo de dado e ".__name__" isola o tipo
# print(f"varStr: {varStr}, Tipo de dado: {type(varStr).__name__}")
# print(f"varFloat: {varFloat}, Tipo de dado: {type(varFloat).__name__}")
# print(f"varBool: {varBool}, Tipo de dado: {type(varBool).__name__}")

#3.Crie a variável num_str = “100” e converta para int e float.

# numStr = "100"

# numInt = int(numStr)
# numFloat = float(numStr)

# print(type(numInt))
# print(type(numFloat))

# 7 - Faça um programa que simule uma calculadora simples, pedindo valor_um e valor_dois, sobre eles opere (+,-,*,/) e mostre todos os resultados.

# valorUm = int(input("Informe o valor 1: "))
# valorDois = int(input("Informe o valor 2: "))

# print(f"Soma:{valorUm + valorDois} ")
# print(f"Subtracao:{valorUm - valorDois} ")
# print(f"Divisao:{valorUm / valorDois} ")
# print(f"Multiplicacao:{valorUm * valorDois} ")


# 8- Faça um programa que peça o valor de um produto e o seu desconto e então apresente o valor final.

# valorProduto = float(input("Qual o valor do produto: "))
# desconto = float(input("Qual a porcentagem do desconto: "))

# valorFinal = valorProduto - ((desconto * valorProduto) / 100)

# print(f"O valor final com desconto eh de: {valorFinal:.1f}")

print("==== MENU INICIAL ====")
print("1 - Iniciar")
print("2 - Configuraçoes")
print("3 - Sair")
print("======================")
