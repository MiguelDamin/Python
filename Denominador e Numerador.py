"""Leia o denominador e o numerador, resolva o cálculo com os valores informados."""
"""O numerador representa a parte que será dividida. Já o denominador contém o número que dividirá a parte"""
denominador = float(input("Selecione o seu denominador: "))
numerador = float(input("Selecione o seu númerador que será dividido: "))
solucao = numerador / denominador
print("A resolução da fração é ", round(solucao, 2))