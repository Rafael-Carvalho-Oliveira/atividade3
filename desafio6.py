#CRIANDO UMA LISTA VAZIA
lista = []

#AQUI O USUÁRIO IRÁ INSIRIR 4 NÚMEROS NA LISTA
numero1 = int(input("Digite um número: "))
lista.append(numero1)
numero2 = int(input("Digite um número: "))
lista.append(numero2)
numero3 = int(input("Digite um número: "))
lista.append(numero2)
numero4 = int(input("Digite um número: "))
lista.append(numero4)

#ORDENANDO A LISTA EM ORDEM CRESCENTE
lista.sort()

#FAZENDO ELE MOSTRAR O PRIMEIRO NÚMERO(0) E O ÚLTIMO(3)
print(lista[-1])
print(lista[0])