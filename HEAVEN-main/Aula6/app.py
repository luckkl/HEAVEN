lista = ['a, b, c, d']

# print(lista)

#imprimindo valor especifico da lista
print(lista[0])

#imprimindo ultimo indice
print(lista[-1])

#imprimir intervalo
print(lista[2:4])

#ordenar esta lista
lista.sort()

#adicionando na lista
lista.append("a")

#inserindo na posição especifica
lista.insert(2,'d')

#inserindo varios valores
lista.extend(['ana','beatriz','david','roberto'])

numeros = []

for i in range(10):
    numeros.append(i * 2)
print(numeros)

#remover item da lista

#pop - remove pelo indice
lista.pop()

#removendo pelo valor (remove a promeira ocorrencia)
lista.remove('ana')

lista_numeros = [n for n in range(11)]
#removendo intervalo de valores
print (f'Lista antes de remover {lista}')
del lista[2:4]

print (f'Lista depois de remover {lista}')

'''for i in range (len(lista)):
    print((f'(i+1)º valor da lista: {lista(i)}'))'''

listanomes = ['a', 'b', 'c', 'd']

#alterando valor da lista
listanomes[1] = 'Cloud'

print(listanomes)

numeros = [1,2,3,4,5,6,7,8,9,10]
for i in range (len(numeros)):
    if numeros[i] > 5:
        numeros[i] = numeros[i] * 2
print(numeros)

numeros2 = [10,20,30,40,50]

#list comprehension
numeros2 = [n * 2 if n > 20 else n for n in numeros2]
print(numeros2)