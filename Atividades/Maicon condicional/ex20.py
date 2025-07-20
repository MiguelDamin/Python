"""Escreva um algoritmo para ler as coordenadas (X,Y) de um ponto no sistema cartesiano e
 Escreva o quadrante ao qual o ponto pertence. Se o ponto estiver sobre os eixos, ou na origem,
 Escreva NÃO ESTÁ EM NENHUM QUADRANTE. Considere que o usuário poderá informar qualquer valor para
  as coordenadas."""


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
else:
    print("NÃO ESTA EM UM PLANO CARTESIANO")




