'''Um sistema gerador de boletin escolar que recebe 4 notas do alunos e devolve se ele foi aprovado
ou reprovado. utilize funções para cada operação.
extra: Utilizando python, gere um pdf com as notas do aluno e a situação dele.'''


notas = []
notafn = float
def media(notas):
    notafn = sum(notas) / 4
    return notafn

for i in range(4):
    notas.append(float(input(f"Nota {i}: ")))

media(notas)
if notafn >= 6:
    print("Aprovado")
else:
    print("Reprovado")



#INACABADO, FINAL DE SEMANA -- TERMINAR.





