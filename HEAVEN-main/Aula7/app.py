'''
Manipulação de arquivos: percorrer os meus diretorios, encontrar o arquivo passar o comando de abertura de arquivos, passar comando de ação

Modos de ação: 
-  "r": Leitura do arquivo
-  "w": escrita(sobrescrever o conteudo antigo)
-  "a": adiciona conteudo
-  "x": criar um arquivo 
-  "b": arquivos binarios
-  "t": texto

'''
#Criando e escrevendo arquivo

arquivo = open("primeiro_arquivo.txt", 'w')
arquivo.write('Hello monkeys')
arquivo.close()


# aplicando boA PRATICA

with open("primeiro_arquivo.txt", "r") as arquivo:
    conteudo = arquivo.read()
    print("da fina")

#Arquivo com multiplas escritas

with open('Bastand.txt', "a") as arquivo:
    arquivo.write('Kaiser\n')
    arquivo.write('Isagi\n')
    arquivo.write('Kunigami\n')
    arquivo.write('Yukimiya\n')

#lendo linha a linha 
with open('Bastand.txt', "r") as arquivo:
    for linha in arquivo:
        print(linha)

    PXG = ['lOKI', 'RIN', 'SHIDOU', 'CHARLES']

    with open('PXG.txt', "w") as arquivo:
        for f in PXG:
            arquivo.write(f + ' ')


#Converter o arquivo em uma lista
with open('PXG.txt', 'r') as arquivo:
    linhas = arquivo.readlines()
    print(type (linhas))
    print(linhas)


#Limpar quebra de linha

with open('Ubers.txt', 'a') as arquivo:
    for linha in arquivo:
        arquivo.write(linha + "\n")
        print(linha.strip())


#exemplo para cadastro
while True:
    nome = input("Digite seu time: ").title()

    with open("Seleção.txt" 'w') as arquivo:
        arquivo.write(nome + "\n")

    sair = input("Deseja sair? s/n").lower()

    if sair == 's':
        break

