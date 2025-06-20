"""Analise o seguinte algoritmo e escreva o que será impresso ao ser executado. Considere que para
cada execução serão informados os seguintes valores para A e B:
a) A=5 e B=2 = amarelo, azul, verde, roxo, lima, vermelho
b) A=2 e B=10 = amarelo, ciano, manga, vermelho
c) Cite um conjunto de valores que deverão ser informados para A e B para que seja impresso:
 Amarelo, Ciano, Lima e Vermelho. = a diferente de 5 , b diferente de 10

"""
#A = 2 e B = 2 -- amarelo, ciano, lima e vermelho
#A=5 = amarelo, azul, verde, roxo
#A=2 = AMARELO, CIANO
#B=2 = lima, vermelho
#B=10 = mango e vermelho
a = int(input("Num de cor A: "))
b = int(input("Num de cor B: "))

if a == 5 and b == 2:
    print("Amarelo, Azul, verde, roxo, lima, vermelho")
elif a == 2 and b == 10:
    print("amarelo, ciano, manga, vermelho")
elif a ==2 and b == 2:
    print("Amarelo, Ciano, Lima e Vermelho")