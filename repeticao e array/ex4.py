
"""Chico tem 1,50 metro e cresce 4 centímetros por ano, enquanto Zé tem 1,30 metro e
cresce 6 centímetros por ano. Construa um algoritmo que calcule e imprima quantos
anos serão necessários para que Zé seja maior que Chico.
"""
chico = 1.50
ze = 1.30
ano = 0 
for i in range (100):
    ano += 1
    chico = chico + 0.04
    ze = ze + 0.06
    if ze > chico:
        print(ano, "anos")
        print("Zé tera", round(ze, 2), "m")
        break





