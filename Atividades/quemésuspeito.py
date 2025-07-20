pergunta1 = input("Telefonou para a vitima?\n")
pergunta2 = input("Esteve no Local do Crime?\n")
pergunta3 = input("Mora perto da vitima? \n")
pergunta4 = input("Devia para vitima? \n")
pergunta5 = input("Já trabalhou com a vitima? \n")
numerodeSim = 0

if pergunta1 == "sim": #elif se uma form vdd esquece o resto, if verifica uma por uma
    numerodeSim += 1
if pergunta2 == "sim":
    numerodeSim += 1
if pergunta3 == "sim":
    numerodeSim += 1
if pergunta4 == "sim":
    numerodeSim += 1
if pergunta5 == "sim":
    numerodeSim += 1

print(f"Você falou sim para {numerodeSim} perguntas")
if numerodeSim == 2:
    print("Você é suspeito")
elif numerodeSim == 3 or numerodeSim == 4:
    print("Você é cumplice")
elif numerodeSim == 5:
    print("Você é assasino")
