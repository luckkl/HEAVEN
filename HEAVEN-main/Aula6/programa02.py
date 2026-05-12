carros = []
proximo_id = 1

import os
import time

while True:
    print("\n==== Sistema de Carros =====")
    print ('1 - Cadastrar carro')
    print ('2 - Listar carro')
    print ('3 - Atualizar carro')
    print ('4 - Deletar carro')
    print ('0 - Sair')

    opcao = input ('Escolha uma opção: ')

    #register
    if opcao == '1':
        modelo = input("Digite o modelo do carro ").title()
        preco = float(input('Digite o preço: '))
        marca = input("Digite a marca: ").title()

        carro = {
            "id"    :proximo_id,
            "modelo"    :modelo,
            "preco"     :preco,
            "marca"     :marca
        }

        carros.append(carros)
        proximo_id += 1

        print ("Carro cadastrado com sucesso.")

    #read
    elif opcao == '2':
        if not carros:
            print ("Nenhum carro cadastrado.")
        else:
            print('\n Lista de carros:')
            for carro in carros:
                print(f'ID: {carro['id']} | Modelo: {carro['modelo']} | preco {carro['preco']} | marca: {carro['marca']}')

    #Update
    elif opcao == '3':
        if not carros:
            print ("Nenhum carro cadastrado.")
        else:
            id_busca = int(input('Digite o ID do carro para atualizar: '))
            encontrado = False

            for carro in carros:
                if carro ['id'] == id_busca:
                    carro ['modelo'] = input("Novo modelo: ").title()
                    carro ['preco'] = float(input("Novo preco: ")).title()
                    carro ['marca'] = input("Nova marca: ").title()

                print ("Carro atualizado com sucesso.")
    
    #delete
    elif opcao == '4':
        print ("Lista de carros: ")
        print(f'ID: {carro['id']} | Modelo: {carro['modelo']} | preco {carro['preco']} | marca: {carro['marca']}')
        id_busca = int(input("Digite o ID do carro para poder deletar: "))

        encontrado = False

        for carro in carros:
            if carro['id'] == id_busca:
                carros.remove(carro)
                print("Carro deletado com sucesso.")
                encontrado = True
            break

        if not encontrado:
            print ("Carro não encontrado.")

        #quit
        elif opcao == '0':
            print ("Saindo do sistema...")
            time.sleep(2)
            break
    else:
         print ("Opção invalida.")