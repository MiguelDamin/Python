"""Escrever um algoritmo que lê 5 valores para a,
um de cada vez, e conta quantos destes valores são negativos, escrevendo esta informação. """

a = []
b = 0

for i in range (5):
    a.append(int(input(f"Valor do array {i}: ")))
    if a[i] < 0:
       b += 1

print(f"O número de negativos é {b}")

