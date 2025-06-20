"""Escreva um algoritmo que leia as medidas dos lados de um triângulo e escreva Se ele é EQUILÁTERO,
ISÓSCELES ou ESCALENO. OBS: Equilátero: 3 lados iguais; Isósceles: 2 lados iguais; Escaleno: 3 lados diferentes.
"""
lado1 = int(input("Lado1 do triangulo: "))
lado2 = int(input("Lado2 do triangulo: "))
lado3 = int(input("Lado3 do triangulo: "))

if lado1 == lado3 and lado1 == lado2:
    print("Equilatero")
elif lado1 != lado3 and lado1 != lado2 and lado2 != lado3:
    print("Escalenos")
else:
    print("Isoceles")
