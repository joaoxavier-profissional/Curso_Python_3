"""
Exercicio
Peça ao usuario para digitar seu nome
Peça ao usuario para digitar sua idade
Se nome  idade forem digitados:
    Exiba:
        Seu nome é {nome}
        Seu nome invertido é {nome invertido}
        Se nome contem (ou não) espaços
        Seu nome tem {n} letras
        A primeira letra do seu nom é {letra}
        A ultima letra do seu nome é {letra}
Se nada for digitado em nome ou idade:
    exiba "Desculpe, você deixou campos vazios."
"""

nome = input("Digite o seu nome: ")
idade = input("Digite a sua idade: ")


if(nome and idade):
    print(f"Seu nome é {nome}")
    print(f"Seu nome invertido é {nome[::-1]}")
    if(" " in nome):
        print("Variavel nome contém espaço")
        nome = nome.replace(" ", "")
    else:
        print("Variavel nome não contem espaço")
    print(f"Seu nome tem {len(nome)} caracteres")
    print(f"A primeira letra do seu nome é {nome[0]}")
    print(f"A ultima letra do seu nome é {nome[-1]}")
else:
    print("Desculpe, você deixou campos vazios")


