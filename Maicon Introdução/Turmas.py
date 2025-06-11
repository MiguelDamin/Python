turmac = 60
turmad = 20
repC = int(input("Quantos forma reprovados na turma C "))
apD = int(input("Quantos foram aprovados na turma D: "))

apC = turmac - repC
repD = turmad - apD


totalduasturmas = turmac + turmad
totalrep = (totalduasturmas - apD) - apC
porcenatgem = (totalrep / totalduasturmas) * 100
print("O número de alunos reprovados na turma C é", repC)
print("O número de alunos reprovados na turma D é", repD)
print("O total de alunos é", totalduasturmas, "e a porcentagem de reprovados é", porcenatgem, "%")
