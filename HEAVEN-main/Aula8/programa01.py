import modulo as ma

def main():
    while True:
        print("\n== Calculadora ==")
        print("1. somar")
        print("2. subtração")
        print("3. multiplicar")
        print("4. Dividir")
        print("5. Limpar terminal")
        print("0. Sair")
        print("")
        
        opcao = input("Digite a opcao desejada: ")
        
        match opcao:
            case '1':
                print('------ SOMA --------')
                num1 = int(input('Digite um numero: '))
                num2 = int(input('Digite outro numero: '))
                print(f'resultado: {ma.soma(num1, num2)}')
            
            case '2':   
                print('------ SUBTRACAO --------')
                num1 = int(input('Digite um numero: '))
                num2 = int(input('Digite outro numero: '))
                print(f'resultado: {ma.subtracao(num1, num2)}')

            case '3':
                print('------ MULTIPLICACAO --------')
                num1 = int(input('Digite um numero: '))
                num2 = int(input('Digite outro numero: '))
                print(f'resultado: {ma.multiplicacao(num1, num2)}')

            case '4':
                print('------ DIVISAO --------')
                num1 = int(input('Digite um numero: '))
                num2 = int(input('Digite outro numero: '))
                print(f'resultado: {ma.divisao(num1, num2)}')

            case '5':
                ma.limpar_terminal()

            case '0':
                print("Encerrando...")
                break

            case _:
                print("Opção inválida!")

if __name__ == "__main__":
    main()