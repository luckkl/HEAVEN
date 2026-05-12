import os
#funções de lambda

somar = lambda x, y: x+y
limpar = lambda: os.system("cls" if os.name == "nt" else "clear")


#algoritmo principal
if __name__ == "__main__":  
    try:
        x = int(input("Digite o valor de x: "))
        y = int(input("Digite o valor de y: "))
        result = somar(x, y)

        limpar()
        os.system("cls")
        print(f"O resultado da soma é: {result}")
        
    except Exception as e:
        print(f"Não foi possível realizar a soma: {e}")
