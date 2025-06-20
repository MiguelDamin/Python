"""Acrescente as seguintes mensagens à solução do exercício anterior conforme o caso.
Caso o número de lados seja inferior a 3 Escreva: NÃO E’ UM POLÍGONO.
Caso o número de lados seja superior a 5 Escreva: POLÍGONO NÃO IDENTIFICADO.
OBS: Considere que o usuário poderá informar qualquer valor para o número de lados."""

numdelados = int(input("Número de lados do polígno: "))
if numdelados < 3:
    print("Não é um poligno")
elif numdelados > 5:
    print("POLIGNO NÃO IDENTIFICADO")
elif numdelados == 3:
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
else:
    print("PENTAGONO")


