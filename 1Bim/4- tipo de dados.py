marca = "Porsche"
modelo = "911"
ano = 2011
cor = "Laranja"
ehNovo = False
valor = 500.000

# print(x)
# x = type("casa")

# print(type(valor))


#Os principais tipos de dados são
# strings/str, que é traduzido para "texto" = "oi,
# eu sou uma string"
# print(type(marca))

#para numeros temos int (inteiros) e
# float(numeros flutuantes ou decimais)
# print(type(ano))
# print(type(valor))
#
# e para verdadeiros/falso = True/False temos o tipo bool, conhecido também
# como booleano
# print(type(ehNovo))
#
#  mais tipos de dados, porém esses são os mais básicos.
# conversão de dados / type casting
# para converter em:
# int = int() converte  os tipos float, str
# str = str() converte os tipos float, int, bool
# float = float() converte os tipos int, str
# boolean = bool() - valido apenas para 1 e 0

var_tipo_int = 10
var_tipo_float = 10.05
var_tipo_bool = True
var_tipo_str = "texto"

print(var_tipo_int)
print(type(var_tipo_int))

var_tipo_int = str(var_tipo_int)
print(var_tipo_int[1])
print(type(var_tipo_int))

var_tipo_int = int(var_tipo_int) + 0.05
print(var_tipo_int)
print(type(var_tipo_int))


var_tipo_int = bool(var_tipo_int)
print(var_tipo_int)
print(type(var_tipo_int))

# x = 0
# print(x, type(x))

# x = bool(x)
# print(x,type(x))

# x = 1
# x2 = "1"
# x3 = "1.2"
#
# # print(x + x2) #erro
# print(int(x) + int(x2) + float(x3))
# print(str(x) + " = um")
# # print(x + " = um") #erro