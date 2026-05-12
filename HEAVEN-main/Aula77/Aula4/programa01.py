'''
    Programa 01 - Aula04 28/04
    Prof: Karython Gomes
    Turma: 2º DS

'''

import os
import random

lista_nomes = [
    'Noel Noa', 
    'Chris Prince', 
    'Marc Snuffy', 
    'Lavinho', 
    'Julian Loki', 
    'Michael Kaiser', 
    'Sae Itoshi', 
    'Don Lorenzo', 
    'Leonardo Luna', 
    'Isagi Yoichi', 
    'Rin Itoshi'
]

lista_sorteados = []
sorteados = 0
while sorteados < 5:
    nome_sorteado = random.choice(lista_nomes)
    print (f'Sorteado: {nome_sorteado}')
    lista_sorteados.append(nome_sorteado)

    print (f'\nLista antes de remover {len(lista_nomes)}')

    lista_nomes.remove(nome_sorteado)
    
    print (f'Lista atualizada {len(lista_nomes)}')
    sorteados +=1

print ("\nFim do programa\n")