calculadora = True
sair = bool

while calculadora is True:
    operador = input("Digite a operação desejada: \n [1] +\n [2] -\n [3] x\n [4] /\n")
    

    if operador == "1":
        numero_1 = float(input("Qual o primeiro numero? "))
        numero_2 = float(input("Qual o segundo numero? "))
        resultado = numero_1 + numero_2
        print(resultado)
    
    sair = input("Deseja sair?\n [s]im: ").lower().startswith('s')

    if sair:
        calculadora = False