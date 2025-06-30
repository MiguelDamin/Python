'''Peça 4 notas, calcule a média e armazene uma mensagem no vetor de saída dizendo se o aluno foi
“Aprovado” ou “Reprovado” (média ≥ 6).'''

notas = []


for i in range(4):
    notas.append(float(input(f"Nota {i}: ")))

mediafinal = sum(notas) / 4
if mediafinal >= 6:
    print("Aprovado")
else:
    print("Reprovado")
