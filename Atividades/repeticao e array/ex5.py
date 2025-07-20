'''Escreva um algorítmo que leia 5 arrays, cada um contendo as notas de 5  alunos, 
e calcule a média de cada array que é a média final.'''

miguelnota = []
matheusnota = []
juniornota = []
maiconnota = []

for i in range(5):
    miguelnota.append(float(input(f"Nota {i} do miguel: ")))
    matheusnota.append(float(input(f"Nota {i} do matheus: ")))
    juniornota.append(float(input(f"Nota {i} do Junior")))
    maiconnota.append(float(input(f"Nota {i} de Maicon: ")))

mediamiguel = sum(miguelnota) / 5
mediamatheus= sum(matheusnota) / 5
mediajunior = sum(juniornota) / 5
mediamaicon = sum(maiconnota) / 5

print(f"A nota final de Miguel é {mediamiguel}")
print(f"A nota final de Mathe é {mediamatheus}")
print(f"A nota final de Junior é {mediajunior}")
print(f"A nota final de Maicon é {mediamaicon}")

