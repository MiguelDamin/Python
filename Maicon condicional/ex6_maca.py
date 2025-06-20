"""As maçãs custam R$ 0,30 ser forem compradas menos do que uma dúzia,
 e R$ 0,25 ser forem compradas pelo menos doze.  Escreva um algoritmo que
 leia o número de maçãs compradas, calcule e escreva o valor total da compra.
"""

numdemaca = int(input("Quantas maças você quer? "))
total = float
preco = float

if numdemaca >= 12:
    preco = 0.25
else:
    preco = 0.30

total = numdemaca * preco

print(f"O total da sua compra é ", round(total, 2))
