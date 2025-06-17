"""Escreva um algoritmo para ler 2 valores e uma das seguintes operações a
serem executadas (codificada da seguinte forma: 1.Adição, 2.Subtração, 3.Divisão,
 4.Multiplicação). Calcular e Escreva o resultado dessa operação sobre os dois valores lidos.
"""

valor1 = int(input("Numero 1 "))
valor2 = int(input("Número 2: "))
operacao = input("1 pra adição, 2 pra subtração, 3 pra divisão e 4 para multiplicação: ")

if operacao == "1":
    total = valor1 + valor2
    print(f"O valor é {total}")
elif operacao == "2":
    total = valor1 - valor2
    print(f"O valor total é: {total}")
elif operacao == "3":
    total = valor1 / valor2 
    print(f"O valor total é: {total}")
elif operacao == 4:
    total = valor1 * valor2
    print(f"O valor total é: {total}")
else: 
    print("OPERACAO INVALIDA")