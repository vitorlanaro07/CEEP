# quando usamos a função input() o valor que ela
# nos traz é uma String
# para fazer operações matematicas com
# valores numericos, precisa ser convertido
# para o tipo correto!

print("Olá, informe seu nome:")
nome = input()

print("Olá, informe sua idade:")
idade = int(input())

print("Seu nome é:",nome)
print("Sua idade é:",idade)

print(int(idade) + 2)