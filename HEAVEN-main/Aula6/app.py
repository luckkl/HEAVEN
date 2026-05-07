lista = ['Luckk', 'Kiaser', 'cicrano', 'beltrano']


print(lista)

#imprimindo valor especifico da lista
print(lista[0])

#imprimindo ultimo indice
print(lista[-1])

#imprimir intervalo
print(lista[2:4])

#ordenar essa lista
#lista.sort()

#adicionando valor na lista
lista.append("Karython")

#inserindo em posição especifica
lista.insert(2, 'joão')

#inserindo varios valores
lista.extend(['lucas','kaiser','gABRIEL','loki','Hugo'])

#removendo intervalo de valores
del lista [2:4]

print(f'lista depois de remover {lista}')
listanomes= ['']

#for i in range(len(lista)):
# print(f'{i+1}º valor da lista: {lista[i]}')


numeros = [1,2,3,4,5,6,7,8,9,10]
for i in range(len(numeros)):
    if numeros[i] > 5:
        numeros[1] = numeros[i] * 2
        print(numeros)
        numeros2 = [10,20,30,40,50]
        
for i in range(len(lista)):
    print (f'(i+1)º valor da lista: {lista[i]}')

