lista = ['janeiro','fevereiro','março','abril','maio','junho','julho','agosto','setembro','outubro','novembro','dezembro']
if 'junho' in lista:
    print('junho esta na lista')#verificando se junho esta na lista
lista.insert(2, 'abril')#adicionando abril na terceira posição 
lista[6] = 'dezembro' #subistituindo a posição 6 por dezembro
lista.pop(12)#eliminando o ultimo da lista
print(lista)  # imprimindo o resultado da lista
