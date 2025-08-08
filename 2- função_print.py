#Função print()

# a função print() apresenta o valor no console
# se você quer apresentar a mensagem "Olá, me chamo Fulano"
# na função, esse texto deve estar entre aspas: ""
# exemplo:
# saudacao = "Olá"
# apresentacao = "me chamo"
# nome = "Vitor"
#
# print(saudacao +" meu nome "+  nome + str(5))



# ou... seu texto deve estar armazenado numa variável que a função usará
# como parametro. Parametro é o valor que colocamos entre parentes: ()
# exemplo
# nome = "Olá me chamo Vitor"
# print(nome)
#
# # ou
#
# # dentro da função print() podemos usar conectores de: , (virgula) ou + (concatenação)
# # exemplo:
# nome = "Vitor"
# print("Olá me chamo", nome)
#
# # ou
saudacao= "Olá"
# apresentacao = "me chamo"
nome = "Vitor"
# print(saudacao, apresentacao, nome)
#
# # ou
# nesse exemplo o sinal de +(mais) concatenou ("me chamo" + nome) ou seja, uniu
print(saudacao,"me chamo: \n    " + nome)

# varías formas para apresentar a mesma mensagem