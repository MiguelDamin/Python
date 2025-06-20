"""Escreva um algoritmo para ler as coordenadas (X,Y) de um ponto no sistema cartesiano e
Escreva o quadrante ao qual o ponto pertence. Caso o ponto não pertença a nenhum quadrante,
escreva se ele está sobre o eixo X, eixo Y ou na origem. Considere que o usuário poderá informar
qualquer valor para as coordenadas.
"""


# B quad (  x,y   )
# A quad ( -x,y   )
# C quad ( -x,-y  )
# D quad (  x,-y  )

x = int(input("Diga o X: "))
y = int(input("Diga o Y: "))

if x > 0 and y > 0:
    print("B")
elif x < 0 and y < 0:
    print("C")
elif x > 0 and y < 0:
    print("D")
elif x < 0 and y > 0:
    print("A")
elif x == 0 and y == 0:
    print("Está na origem")
elif x > 0 and y ==0:
    print("Está somente no eixo X positivo")
elif x< 0 and y ==0:
    print("Está no eixo X negativo")
elif x == 0 and y>0:
    print("Está somente no eixo Y positivo")
else:
    print("EStá no eixo Y negativo")
