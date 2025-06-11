"""Uma revendedora de carros usados paga a seus funcionários vendedores um salário fixo por mês,
mais uma comissão fixa por cada carro vendido. Além disso, ela também adiciona ao salário de
cada vendedor 5% do valor das vendas por ele efetuadas. Escrever um algoritmo que lê o número
do vendedor, o salário fixo, o número de carros por ele vendidos, o valor total de suas vendas
e a comissão fixo que recebe por carro vendido e, sem seguida, calcule o salário do vendedor
juntamente com o seu número de identificação."""

salariofix = 7000
comissaofix = 2.5
numerodevendas = float(input("Quanos carros o bicho veio vendeu? : "))
precodocarro = float(input("Preço do carro: "))
numerodevendedor = int(input("Número do vendedor: "))
valorvendas = float
valorComTodasAsComissoes = float
valorvendas = (precodocarro / 100) * comissaofix * numerodevendas + precodocarro * numerodevendas
valorComTodasAsComissoes = (valorvendas / 100) * 5 + valorvendas + salariofix
print("O número do funcionario é", numerodevendedor, "e o seu salário total desse mês é de", valorComTodasAsComissoes)

