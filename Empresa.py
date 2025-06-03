"""Considere que o aumento dos funcionários de uma empresa é de 8% do salário atual
mais um percentual de produtividade discutido com a empresa. Escrever um algoritmo que
lê o número do funcionário, seu salário atual e o índice de produtividade discutido com a empresa.
Então, escreve o número do funcionário, seu aumento e o valor de seu novo salário. """

funcionarioandrey = int(input("Número do funcionário: "))
salario = (1200.00 / 100) * 8 + 1200
porcentagemdiscutida = float(input("Porcentagem de aumento salarial discutida com a empresa: "))
salariocaumento = float
salariocaumento= (salario / 100) * porcentagemdiscutida + salario
print("O número do funcionario é", funcionarioandrey, "e o total que o funcionario ganhara será: ", salariocaumento)
