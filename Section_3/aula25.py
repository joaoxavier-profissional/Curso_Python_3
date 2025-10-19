"""
Interpolação básica de strings
s - string
d e i - int
f - float
x e X - Hexadecimal
"""

nome = 'João'
preco = 1000.1234
variavel = '%s, o preço é R$%.2f' %(nome, preco)
print(variavel)
print('O hexadecimal de %d é %04x' % (15, 15))