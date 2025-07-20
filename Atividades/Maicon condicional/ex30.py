"""Escreva um algoritmo que leia a idade de 2 homens e 2 mulheres
(considere que a idade dos homens será sempre diferente, assim como das mulheres).
 Calcule e escreva a soma das idades do homem mais velho com a mulher mais nova, e
  o produto das idades do homem mais novo com a mulher mais velha."""

home1 = int(input("Idade do Primeiro Homem: "))
home2 = int(input("Idade do Segundo Homem: "))
mulher1 = int(input("Idade da Primeira Mulher: "))
mulher2 = int(input("Idade da Segunda Mulher: "))


if home1 > home2:
    print(f"Homem1 com {home1} anos de idade é o mais velho ")
    homeMaisVelho = home1
    homeMaisNovo = home2
else:
    print(f"Homem2 com {home2} anos de idade é o mais velho ")
    homeMaisVelho = home2
    homeMaisNovo = home1
if mulher1 < mulher2:
    print(f"Mulher1 com {mulher1} anos é a mais nova" )
    mulherMaisNova = mulher1
    mulherMaisVelha = mulher2
else:
    print(f"Mulher2 com {mulher2} anos é a mais nova" )
    mulherMaisNova = mulher2
    mulherMaisVelha = mulher1

soma = homeMaisVelho + mulherMaisNova
produto = homeMaisNovo * mulherMaisVelha

print(f"A soma das idades do homem mais velho com a mulher mais nova é igual a {soma}")
print(f"O produto das idades do homem mais novo com a mulher mais velha é igual a {produto}")





