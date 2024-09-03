lista = [5, 8, 2, 9, 1]
lista.sort()
print(lista)
lista.sort(reverse=True)#imprimindo a lista na ordem decrescente
print(lista)
lista.insert(5, 7)
print(lista)
lista.insert(1, 3)#inserindo dois numeros a lista
print(lista)
lista[0] = 10#substituição do numero
print(lista)
lista.remove(7) #removendo o 7 da lista
print(lista)
del lista[1:3]#deletando do numero na posição 2 até 4
print(lista)