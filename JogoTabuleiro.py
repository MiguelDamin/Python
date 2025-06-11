jog1 = input("Nome do Jogador1: ")
jog2 = input("Nome do Jogador2: ")
dado1 = 0
dado2 = 0
psjog1 = 0
psjog2 = 0 
valordados = 0
#tabjog1 = ["."]
#tabjog2 = ["."]


import random 
def sortear_dado():
  return random.randint(1, 6)

for i in range (1,6):
  print("RODADA ", i)

  x = input(f"{jog1} pressione enter para jogar os dados: ") #Precisa do f para variavel funcionar dentro do input
  if(x == ""):
    dado1  = sortear_dado() #usando essa função eu jogo o dado, ou sorteio
    dado2 = sortear_dado() #usando essa função eu jogo o dado, ou sorteio
    print("O valor do primeiro dado é ", dado1)
    print("O valor do segundo dado é ", dado2)
    valordados = dado1 + dado2
    psjog1 = psjog1 + valordados
    if(dado1 == dado2):
      psjog1 = psjog1 + 3
      print("PARABÉNS ", jog1, "você ganhou pontuação extra + 3 casa pra frente e sua posição é", psjog1)
    else:
      print("A posição do ",jog1, "é", psjog1)

  x = input(f"{jog2} pressione enter para jogar os dados: ")
  if(x == ""):
     dado1 = sortear_dado()
     dado2 = sortear_dado()
     print("O valor do primeiro dado é ",dado1)
     print("O valor do segundo dado é ",dado2)
     valordados = dado1 + dado2
     psjog2 = psjog2 + valordados
     if(dado1 == dado2):
       psjog2 = psjog2 + 3
       print("PARABÉNS ", jog2, "você ganhou pontuação extra + 3 casa pra frente e sua posição é", psjog2)
     else:
       print("A posição do ", jog2, "é", psjog2)
if(psjog1 > psjog2):
  print(jog1, "é o vencedor")
elif(psjog1 == psjog2):
  print("DEU EMPATE")
else:
  print(jog2, "é o vencedor")




