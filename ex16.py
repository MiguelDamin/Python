"""Escreva um algoritmo para ler 3 valores e escreva o maior deles.
 Considere que o usuário não informará valores iguais."""

num1 = int(input("Num1: "))
num2 = int(input("Num2: "))
num3 = int(input("Num3: "))

if num1 > num2:
    if num1 > num3:
       print(f"{num1} é o maior")
    else:
        print(f"{num3} é o maior")
elif num2 > num3:
    print(F"{num2} é o maior")
else:
    print(f"{num3} é o maior")
