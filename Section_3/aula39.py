"""
Iterando strings com while

nome = 'Luiz Otavio'

nova_string = '*L*u*i*z* *O*t*a*v*i*o*"
"""

nome = 'João Xavier'
n = 0
nova_string = ""

while n < len(nome):
    nova_string = f"{nova_string}" + "*" + f"{nome[n]}" 
    if n == len(nome) - 1:
        print(nova_string)
    n += 1;