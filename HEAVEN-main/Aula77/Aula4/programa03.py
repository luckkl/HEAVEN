'''

    Sistema: Calculadora

'''
while True:
    print(30*"-", "Calduladora", 30*"-")
    num1 = int(input("Digite um numero: "))
    num2 = int(input("Digite outro numero: "))
    print ("1. Soma")
    print ("2. Subtração")
    print ("3. Multiplicção")
    print ("4. Divisão")
    opcao = input ('Digite a operação: (+,-,/,*)')

    match opcao:
        case '+':
            resultado = 1 + 2
            print (f'{num1} + {num2} = resultado')
            break
        case '-':
            if num1 != 0 and num2 != 0:
                resultado = 1 - 2
                print (f'{num1} - {num2} = resultado')
                break
            else:
                print ("Bruh.")
                break
        case "/":
            resultado = 1 / 2
            print (f'{num1} / {num2} = resultado')
            break
        case "*":
            resultado = 1 * 2
            print (f'{num1} * {num2} = resultado')
            break
        case _:
            pass
            print ("Digite um numero valido.")