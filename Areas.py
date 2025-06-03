"""Dados 3 valores positivos (a, b, c), calcular: (a) área do triângulo retângulo com base a e altura b;
(b) área do retângulo com base a e altura c; (c) área do trapézio com base maior a, base menor b e altura c."""




"""Área  do triangulo retangulo"""

"""Área do retangulo """

"""Área do trapézio"""

"""Outputs"""
a = int(input("Valor A: "))
b = int(input("Valor B: "))
c = int(input("Digite a hipotenusa: "))

valordotriangulo = (a * b) / 2
print("Area do triangulo : ", valordotriangulo)

base = int(input("Digite a base do retânguolo: "))
altura = int(input("Altura do retangulo: "))
valorretangulo = base * altura
print("A área do retãngulo é: ", valorretangulo)

basemaior = int(input("Digite a base maior do trapezio: "))
basemenor = int(input("Digite a base menor do trapezio"))
alturatrapezio = int(input("Digite a altura do trapezio: "))
valordotrapezio = (basemaior + basemenor) * alturatrapezio / 2
print("A área do trapezio é: ", valordotrapezio)
