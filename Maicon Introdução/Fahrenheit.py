"""Escreva um algoritmo para ler uma temperatura em graus Fahrenheit,
calcular e escrever o valor correspondente em graus Celsius: C = ((F – 32)*5)/9"""

temperaturaemfahrenheit = float(input("Escreva a temperatura em Fahrenheit: "))
graus = (temperaturaemfahrenheit - 32) * 5/9
print(graus)