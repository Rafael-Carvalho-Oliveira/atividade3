# Variável

notas = []

# Declaração de variável

numero_usuario1 = float(input('Digite uma nota: '))
notas.append(numero_usuario1)

numero_usuario2 = float(input('Digite uma nota: '))
notas.append(numero_usuario2)

numero_usuario3 = float(input('Digite uma nota: '))
notas.append(numero_usuario3)

numero_usuario4 = float(input('Digite uma nota: '))
notas.append(numero_usuario4)

numero_usuario5 = float(input('Digite uma nota: '))
notas.append(numero_usuario5)

# Soma e quantidade das variáveis

quantidade_notas = len(notas)

soma = sum(notas)

media = soma / quantidade_notas

# Imprime a soma e a quantidade das variáveis

print(f'As notas são {notas}')
print(f'A soma das notas são {soma}')
print(f'A média é {media:.1f}')

# Para saber se o aluno alcançou a média

if media >= 7:
    print(f'O aluno foi aprovado com a média {media:.1f}')

elif media >=5 or 6.9:
    print(f'O aluno ficou de recuperação com a média {media:.1f}')

else:
    print(f'O aluno foi reprovado com a média {media:.1f}')