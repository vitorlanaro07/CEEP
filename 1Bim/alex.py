nota1 = 0
while nota1 < 0 and nota1 > 100:
    nota1 = int(input('qual a sua nota do 1° semestre \n'))




nota2 = int(input('qual a sua nota do 2° semestre \n'))
nota3 = int(input('qual a sua nota do 3° semestre \n'))
media = (nota1+nota2+nota3)/3

# if: se for tal coisa
# else: se não for tal coisa

if nota1<=100 and nota2<=100 and nota3<=100:
    if media >= 50:
        print(f'sua nota é {media} você foi aprovado')
    if media <30:
        print(f'sua nota é {media} você esta de reprovado')
    if media < 50 and media > 30:
        print(f'sua nota é {media} e você foi recuperação')
else:
    print('\n as notas não podem ser maiores que 100 \n')