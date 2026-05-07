import time

carros = []
proximo_id = 1

while True:
    print("\n==== Sistema de Carros =====")
    print('1 - Cadastrar carro')
    print('2 - Listar carros')
    print('3 - Atualizar carro')
    print('4 - Deletar carro')
    print('0 - Sair')

    opcao = input('Escolha uma opção: ')

    # CREATE
    if opcao == '1':
        modelo = input("Digite o modelo do carro: ").title()
        preco = float(input('Digite o preço: ').replace(',', '.'))
        marca = input("Digite a marca: ").title()

        carro = {
            "id": proximo_id,
            "modelo": modelo,
            "preco": preco,
            "marca": marca,
        }

        carros.append(carro)

        with open("sistema.txt", "a") as arquivo:
            arquivo.write(f"{modelo},{marca},{preco}\n")

        proximo_id += 1

        print("✅ Carro cadastrado com sucesso!")

    # READ
    elif opcao == '2':

        try:
            with open("sistema.txt", "r") as arquivo:

                linhas = arquivo.readlines()

                if not linhas:
                    print("Nenhum carro cadastrado.")

                else:
                    print("\nLista de carros:")

                    for linha in linhas:
                        dados = linha.strip().split(",")

                        carro = {
                            "modelo": dados[0],
                            "marca": dados[1],
                            "preco": dados[2]
                        }

                        print(
                            f"Modelo: {carro['modelo']} | "
                            f"Marca: {carro['marca']} | "
                            f"Preço: {carro['preco']}"
                        )

        except FileNotFoundError:
            print("Arquivo ainda não existe.")

    # UPDATE
    elif opcao == '3':
        print("⚠️ Update ainda não altera o TXT.")

    # DELETE
    elif opcao == '4':
        print("⚠️ Delete ainda não altera o TXT.")

    # SAIR
    elif opcao == '0':
        print("Saindo do sistema...")
        time.sleep(2)
        break

    else:
        print("❌ Opção inválida.")