"""
Faça um programa que peça ao usuario para digitar um numero inteiro,
informe se este numero é par ou ímpar. Caso o usuario não digite um número inteiro, informe que não é um numero inteiro
"""

input_user = input("Digite um numero: ");

try:
    if (int(input_user) % 2 == 0):
        print("Numero é par")
    else:
        print("Numero é impar")
except:
    print(f"Usuario não digitou um numero")


"""
Faça um programa que pergunte a hora ao usuario e, baseando-se no horario descrito, exiba a saudação apropriada. 
Ex. Bom dia 0-11, Boa tarde 12-17 e Boa noite 18-23
"""

input_user_hora = input("Que horas são? ")

if(int(input_user_hora) < 12):
    print("Bom dia")
elif(int(input_user_hora) < 17):
    print("Boa tarde")
else:
    print("Boa noite")

"""
Faça um programa que peça o primeiro nome do usuario. Se o nome tiver 4 letras ou menos
escreva "Seu nome é curto"; Se tiver entre 5 e 6 letras, escreva "Seu nome é normal"; maior que 6 escreva "Seu nome é muito grande".
"""

input_user_nome = input("Digite o seu nome: ")

if len(input_user_nome) <= 4:
    print("Seu nome é curto")
elif len(input_user_nome) <= 6:
    print("Seu nome é normal")
else:
    print("Seu nome é muito grande")