"""Escreva um algoritmo para ler as 4 notas obtidas por um aluno em 4 avaliações. Calcular a média usando
 a seguinte fórmula:
Média = (N1 + (N2 * 2) + (N3 * 3) + N4) / 7
	A seguir imprima o conceito do aluno baseado na seguinte tabela:
Média
Conceito
9,0 ou acima de 9,0 =                A
entre 7,5 (inclusive) e 9,0 =     B
entre 6,0 (inclusive) e 7,5 =     C
abaixo de 6,0 =                   D

"""


nota1 = float(input("NOta1: "))
nota2 = float(input("Nota2: "))
nota3 = float(input("NOta3: "))
nota4 = float(input("Nota4: "))
media = (nota1 +(nota2 * 2)+ (nota3 *3) + nota4) / 7

if media >= 9:
    print("Você tirou A")
elif media >= 7.5 and media < 9:
    print("Você tirou B")
elif media >= 6.0 and media < 7.5:
    print("Você tiou C")
else:
    print("Você tirou D")

