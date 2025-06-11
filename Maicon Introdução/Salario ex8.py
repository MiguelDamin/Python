"""Escreva um algoritmo para ler o salário mensal e o percentual de reajuste.
Calcular e escrever o valor do novo salário. """

salariomensal = float(input("Qual o salário mensal: "))
ajuste = float(input("Percentual de reajuste: "))
novosalario = (salariomensal / 100) * ajuste + salariomensal 
print(novosalario)