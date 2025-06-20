"""Escreva um algoritmo para ler 3 valores e escreva a soma dos 2 maiores.
 Considere que o usuário não informará valores iguais."""

num1 = int(input("Num1: "))
num2 = int(input("Num2: "))
num3 = int(input("Num3: "))
nummaior= int
maior2 = int
soma = int

if num1 > num2:
    if num1 > num3:
       print(f"{num1} é o maior")
       nummaior = num1
       if num2 > num3:
          maior2 = num2
       else:
           maior2 = num3
    else:
        print(f"{num3} é o maior")
        nummaior = num3
        if num1 > num2:
            maior2 = num1
        else:
           maior2 = num2
elif num2 > num3:
    print(F"{num2} é o maior")
    nummaior = num2
    if num3 > num1:
        maior2 = num3
    else:
        maior2 = num1
       

else:
    print(f"{num3} é o maior")
    nummaior = num3
    if num2 > num3:
        maior2 = num2
    else:
        maior2 = num3

soma = maior2 + nummaior

print(f"A soma dos dois maiores é {soma}")




