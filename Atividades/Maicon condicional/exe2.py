"""Acrescente ao exercício acima a mensagem
‘Você foi REPROVADO! Estude mais.’ caso a média calculada seja menor que 8,0.
"""
nota1 = float(input("Nota 1 do aluno: "))
nota2 = float(input("Nota 2 do aluno: "))
notadosemestre = (nota1 + nota2) / 2
if(notadosemestre >= 8.0):
  print("PARABÉNS! Você foi aprovado")
else:
  print("Vc está REPROVADO")
