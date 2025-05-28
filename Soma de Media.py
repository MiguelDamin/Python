nome = input("Nome do aluno? \n")
idade = 0
idade = int(input("Idade do Aluno: "))
nota1 = float(input("Nota 1: "))
nota2 = float(input("Nota 2: "))
nota3 = float(input("Nota 3: "))
notafinal = (nota1 + nota2 + nota3) / 3
if(notafinal >= 7):
   print("Aluno se chama ", nome, " e sua idade é ", idade, ",e está Aprovado com nota %.2f" % notafinal)
elif(notafinal < 5):
     print("Aluno se chama ", nome, " e sua idade é ", idade, " ,e está Reprovado com nota %.2f" % notafinal)
elif(notafinal >= 5 and notafinal < 7):
     print("Aluno se chama ", nome, " e sua idade é ", idade, " ,e está de Recuperação com nota %.2f" % notafinal)
