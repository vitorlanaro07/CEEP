marca = "Porsche"
modelo = "911"
ano = 2011
cor = "Laranja"
novo = False
valor = 500.000

#Os principais tipos de dados são
# strings/str, que é traduzido para "texto" = "oi, eu sou uma string"
print(type(marca))

#para numeros temos int (inteiros) float(numeros flutuantes ou decimais)
print(type(ano))
print(type(valor))

#e para verdadeiros/falso = True/False temos o tipo bool, conhecido também
# como booleano
print(type(novo))

#há mais tipos de dados, porém esses são os mais básicos.

#conversão de dados / type casting
# para converter em:
# int = int()
# str = str()
# float = float()
# boolean = bool() - valido apenas para 1 e 0

x = 1
x2 = "1"
x3 = "1.2"

# print(x + x2) #erro
print(int(x) + int(x2) + float(x3))
print(str(x) + " = um")
# print(x + " = um") #erro