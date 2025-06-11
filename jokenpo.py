"""Desafio: "Pedra, Papel ou Tesoura"
Regras:
    O usuário joga contra o computador.
    Cada rodada, o usuário escolhe pedra, papel ou tesoura.
    O computador escolhe aleatoriamente.
    O programa decide quem ganhou.
    O jogo pode ter 3 rodadas, e no final mostra quem venceu mais."""
import random
pedra1 = "pedra"
tesoura2 = "tesoura"
papel3 = "papel"
suapontuação = 0
pontuaçãodopc = 0

def sortear_jogada():
    return random.choice(["pedra", "tesoura", "papel"]) #return random choice pq sao strings se fosse numero seria return random.randit
#TROCAR PARA STRING E SER MAIS NORMAL O JOGO

for i in range (0,3):
    print(f"RODADA {i}")
    jogada = input("PEDRA: 1, TESOURA: 2, PAPEL: 3. FAÇA SEU JOGO: ")
    jogadaDoPc = sortear_jogada()
    print(f"O Computador jogou {jogadaDoPc}")
    if jogada ==  "pedra" and jogadaDoPc == "tesoura":
      print("Você ganhou")
      suapontuação += 1
    elif jogada == "tesoura" and jogadaDoPc == "pedra":
        print("O computador venceu")
        pontuaçãodopc += 1
    elif jogada == "pedra" and jogadaDoPc == "papel":
        print("O computador ganhou")
        pontuaçãodopc += 1
    elif jogada == "papel" and jogadaDoPc == "pedra":
        print("Você ganhou")
        suapontuação += 1
    elif jogada == "tesoura" and jogadaDoPc == "papel":
        print("Você ganhou")
        suapontuação += 1
    elif jogada == "papel" and jogadaDoPc == "tesoura":
        print("O computador ganhou")
        pontuaçãodopc += 1
    else: 
        print("EMPATE")

print(f"Pontuação do Jogador: {suapontuação}")
print(f"Pontuação da Maquina: {pontuaçãodopc}")
if suapontuação > pontuaçãodopc:
    print("Quem venceu mais foi o Humano")
elif pontuaçãodopc > suapontuação:
    print("O PC venceu mais")
else:
    print("EMPATE GERAL")



