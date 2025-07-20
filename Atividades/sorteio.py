"""O programa escolhe um número secreto entre 1 e 100.
O jogador tem 7 tentativas para adivinhar.
A cada tentativa, o programa responde:
    “🔺 Muito alto!” se o chute for maior que o número.
    “🔻 Muito baixo!” se for menor.
    “🎯 Acertou!” se for igual.
Se acabar as tentativas e o usuário não acertar, mostra o número secreto."""
import random
numsecreto = int
def sortear_numero():
    return random.randint(1,100)
numsecreto = sortear_numero()
#print(numsecreto)

for i in range(1,7):
    numerotry = int(input("Tente acertar o número de 1 a 100: "))
    if numerotry == numsecreto:
        print("Parabéns você acertou o número")
        break
    elif numerotry > numsecreto:
        print("Muito Alto!")
    else:
        print("Muito Baixo!")
    if i == 7: 
        print(f"Acabou as chances infelizmente )=, o número era {numsecreto}")
    


