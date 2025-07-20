'''Solicite 10 números, armazene em um vetor e calcule a soma de todos os valores.'''

numeros = []

for i in range(10):
    numeros.append(int(input(f"Número {i}: ")))

somadosnumeros = sum(numeros)
print(f"A soma dos numeros é {somadosnumeros}")