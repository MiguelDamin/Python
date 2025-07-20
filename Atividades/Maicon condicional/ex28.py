"""Um posto está vendendo combustíveis com a seguinte tabela de descontos:
--------------------------------------------------------------------------------
Combustível             Litros               Desconto
Álcool                 Até 20                 3%
                      Mais de 20               5%
Gasolina               Até 15                   3,5% 
                     Mais de 15                6%
--------------------------------------------------------------------------------
Escreva um algoritmo que leia o número de litros vendidos,
 o tipo de combustível (codificado da seguinte forma: 1-álcool 2-Gasolina),
 calcule e imprima o valor a ser pago pelo cliente, sabendo-se que o preço da gasolina
 é de R$ 1,90 o litro e o álcool R$ 1,28.
"""

gasolina = float
gasolina = 1.90
alcool = float
alcool = 1.28
desconto = float
precototal = float
precosemdesconto = float



tipodagasolina = float(input("Selecione o 1-alcool e 2-gasolina: "))
if tipodagasolina == 1:
    tipodagasolina = alcool
else:
    tipodagasolina = gasolina

numdelitros = float(input("Números de litros que você quer abastecer: "))

if tipodagasolina == alcool and numdelitros <= 20:
    desconto = 3
    precosemdesconto = numdelitros * tipodagasolina
    precototal = precosemdesconto - ((precosemdesconto / 100) * desconto ) 
    print(f"O preço total a pagar é R$", round(precototal, 2))
elif tipodagasolina == alcool and numdelitros > 20:
    desconto = 5
    precosemdesconto = numdelitros * tipodagasolina
    precototal = precosemdesconto - ((precosemdesconto / 100) * desconto ) 
    print(f"O preço total a pagar é R$", round(precototal, 2))
elif tipodagasolina == gasolina and numdelitros <= 15:
    desconto = 3.5
    precosemdesconto = numdelitros * tipodagasolina
    precototal = precosemdesconto - ((precosemdesconto / 100) * desconto ) 
    print(f"O preço total a pagar é R$", round(precototal, 2))
elif tipodagasolina == gasolina and numdelitros >= 15:
    desconto = 6
    precosemdesconto = numdelitros * tipodagasolina
    precototal = precosemdesconto - ((precosemdesconto / 100) * desconto ) 
    print(f"O preço total a pagar é R$", round(precototal, 2))
    
    



