"""Escreva um algoritmo para ler 3 valores e escrevê-los em ordem crescente.
 Considere que o usuário não informará valores iguais."""

num1 = int(input("Num1: "))
num2 = int(input("Num2: "))
num3 = int(input("Num3: "))

if num1 < num2:
    if num1 < num3:
        if num2 < num3:
            print(num1, num2, num3)
        else:
            print(num1, num3, num2)
if num2 < num1:
    if num2< num3:
        if num3 < num1:
           print(num2, num3, num1)
        else:
            print(num2, num1, num3)
if num3 < num2:
    if num3< num1:
        if num1 < num2:
            print(num3, num1, num2)
        else:
            print(num3, num2, num1)


  