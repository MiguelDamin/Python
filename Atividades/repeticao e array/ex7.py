
'''Solicite 6 números, armazene em um vetor, e informe qual é o maior e qual é o menor número digitado.'''

numeros = []

for i in range(6):
    numeros.append(int(input(f"Número {i} ")))

maiornumero = max(numeros)
menornumero = min(numeros)

print(F"O maior número é {maiornumero}")
print(f"O menor número é {menornumero}")
