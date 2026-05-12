import os
import time

class cracks:
    def adicionar(self):
        with open("alimentos.txt", "a") as arquivo:
            al= input("Adicione um alimento: ").title()
            arquivo.write(al +"\n")
            print(" Baddie adicionada com Sucesso✅")
    def listagem(self):
            with open("alimentos.txt", "r") as arquivo:
                alimentos = arquivo.readlines()
                for linha in alimentos:
                    print(linha.strip())
    def desligar(self):
        
        for i in range(5, 0, -1):
            os.system('cls')
            if i == 1:
                print("Desligando em 1 segundo...")
            else:
                print(f'Desligando em {i} segundos...')
            time.sleep(1)
    def introduzir(self):
         os.system('cls')
         print("-------The best Cracks-------")
         time.sleep(2)
         while True:
            opcao= input("Adicionar [1] | Listar[2] | Sair[3]" + "\n").lower().strip()
            match opcao:
                case "1":
                    self.adicionar()
                    time.sleep(2)
                    os.system('cls')
                case "2":
                    self.listagem()
                    time.sleep(3)
                case "3":
                    self.desligar()
                    break
exe = cracks()
exe.introduzir()
