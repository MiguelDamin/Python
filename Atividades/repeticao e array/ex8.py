'''Peça ao usuário para preencher um vetor com 7 números e, depois, informe um número a ser buscado. O
programa deve dizer se ele existe no vetor e em qual posição (índice).'''   

numeros = []
i = 0

for i in range(7):
    numeros.append(int(input(f"Numero {i}: ")))
    i += 1

busca = int(input("Número a ser buscado: "))
for i in range(7):
    if busca == numeros[i]:
       print(f"Esse número existe e esta na posição {i}")
       
       
            