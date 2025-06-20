"""Escreva um algoritmo para ler o número de lados de um polígono regular, e a medida do lado.
 Calcular e imprimir o seguinte:
Se o número de lados for igual a 3, Escreva: TRI NGULO e o valor do seu perímetro;
Se o número de lados for igual a 4 Escreva: QUADRADO e o valor da sua área;
Se o número de lados for igual a 5 Escreva: PENTÁGONO."""


numdelados = int(input("Número de lados do polígno: "))

if numdelados == 3:
    print("TRIANGULO")
    lado1 = int(input("Valor do lado 1: "))
    lado2 = int(input("Valor do lado 2: "))
    lado3 = int(input("Valor lado 3: "))
    perimetro = lado1 + lado2 + lado3
    print(f"Perimetro é {perimetro}")
elif numdelados == 4:
    print("QUADRADO")
    lado1 = int(input("Valor dos lados do quadrado: "))
    area = lado1 * lado1
    print(f"O valor da área é: {area}")
elif numdelados == 5:
    print("PENTAGONO")
