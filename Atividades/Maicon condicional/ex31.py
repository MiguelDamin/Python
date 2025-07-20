"""Escreva um algoritmo que leia o valor de 3 ângulos de um triângulo e
escreva Se o triângulo é ACUT NGULO, RET NGULO ou OBTUS NGULO. OBS: Retângulo: um ângulo reto.
Obtusângulo: um ângulo obtuso; Acutângulo: 3 ângulos agudos.
"""

angulo1 = int(input("Angulo 1: "))
angulo2 = int(input("Angulo 2: "))
angulo3 = int(input("Angulo 3: "))

if angulo1 < 90 and angulo2< 90 and angulo3<90:
    print("Acutangulo")
elif angulo1 == 90 and angulo2 == 90 and angulo3 == 90:
    print("Retângulo") 
else:
    print("Obtusângulo")

