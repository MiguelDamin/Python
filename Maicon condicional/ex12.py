"""Escreva um algoritmo para ler o número de gols marcados
 pelo Grêmio e o número de gols marcados pelo Inter em um GRENAL.
 Escreva o Nome do Vencedor. Caso não haja vencedor deverá ser impresso a palavra EMPATE."""

grebbio = input("Número de gols do grebbio: ")
INTER = input("Número de gols do Inter: ")

if grebbio > INTER:
    print("Grêmio é o venedor")
elif INTER > grebbio:
    print("INTERZÃO É O VENCEDOR")
else:
    print("EMPATE")
     