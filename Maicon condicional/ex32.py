"""Um mercado está vendendo frutas com a seguinte tabela de preços:
Até 5 Kg
Morango: R$ 5,00 p/Kg
Maçã: R$ 3,00 p/Kg

Acima de 5 Kg
Morango: R$ 4,00 p/Kg
Maçã:R$ 2,00 p/Kg
"""
precomorangoMnr5 = 5.00
precomorango5 = 4.00
precomaçãMnr5 = 3.00
precomaçã5 = 2.00
fruta = input("Qual fruta vc quer(mornago/maçã)? ")
kg = float(input("Quantos Kg de fruta vc quer? "))

if kg > 5 and fruta == "morango":
    total = kg * precomorango5
    print(f"O preço é {precomorango5}")
elif kg < 5 and fruta =="morango":
    total = kg * precomorangoMnr5
    print(f"O preço é {precomorangoMnr5}")
if kg > 5 and fruta == "maçã":
    total = kg * precomaçã5
    print(f"O preço total é {precomaçã5}")
else:
    total = kg * precomaçãMnr5
    print(f"O preço total é {precomaçãMnr5}")






