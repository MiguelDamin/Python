
"""Escrever um algoritmo que lê um valor N inteiro e positivo e que imprime a 
tabuada de N para valores de 1 a 10."""

numero = int(input("Numero inteiro: "))
a = [0]*11
i=0
for i in range (1, 11):
    a[i] = i * numero

g=0
for g in range (1, 11):
    print(numero, "X", g, "=", a[g])



