"""Escreva um algoritmo para ler uma temperatura em graus Celsius,
calcular e escrever o valor correspondente em graus Fahrenheit: F = C * 9 / 5 + 32"""

celsius = int(input("Graus em celsius: "))
fahrenheit = (celsius * 9/5) + 32
print(fahrenheit)