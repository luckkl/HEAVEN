# Função com parametro & retorno
'''def função_segundo_grau(a, b, c):
    print("Olá, mundo!")
    return a, b, c 

#chamando a função e armazendando o valor em uma variável
x = função_segundo_grau(1, 2, 3)
print(x)'''

'''def soma(a, b):
    resultado = a + b
    return resultado

resultado = soma(10, 10)
print(resultado)

num1 = int(input("Digite o primeiro número: "))
num2 = int(input("Digite o segundo número: "))

resultado = soma(num1, num2)  
print(resultado)'''

'''def mostrar_msg():
    print(f'Olá mundo das funçoes!')
    
mostrar_msg()

def mostrar_saudacao(nome):
    print(f'Olá {nome}, sejam bem-vindo!')
    
mostrar_saudacao('U')'''

#função recursiva

def fatorial(n):
    # n!
    # caso um certo idiota (eu) esquecer o que fatorial e, e quando o numero se multiplica
    return 1 if n == 0 else n * fatorial(n - 1)
