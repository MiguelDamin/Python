
"""A prefeitura de uma cidade fez uma pesquisa entre seus habitantes,
coletando dados sobre o salário e número de filhos. A prefeitura deseja saber:
      a) média do salário da população; 
      b) média do número de filhos; 
      c) maior salário; 
      d) percentual de pessoas com salário até R$100,00. 
O final da leitura de dados se dará com a entrada de um salário negativo. (Use o comando WHILE)  """
# declaração

salario = []
filhos = []
filhosMedia= float
mediasalarial = 0
pessoas = 0 
filhoscontagem = 0
pobres = 0


for i in range (1000):
    salario.append(float(input("Salario ou digite 0 pr fechar: ")))
    if salario[i] == 0 :
       break
    else:
      pessoas += 1
      filhos.append(int(input("Filhos ou enter: ")))
    if salario[i] <= 100:
       pobres +=1


      
      
filhosMedia =  sum(filhos) / pessoas
mediasalarial = sum(salario) / pessoas
mediapobres = pobres / pessoas * 100
maiorsalario = max(salario)
print("O maior salario é", maiorsalario, "R$")
print("A media salarial é", mediasalarial, "R$")
print("A media de fihos é",  filhosMedia)
print("A porcentagem de pobres é", mediapobres, "%")






