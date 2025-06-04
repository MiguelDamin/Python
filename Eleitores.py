
brancos = int(input("Quantos votos foram brancos: "))
nulos = int(input("Quantos votos foram nulos: "))
validos = int(input("Quantos votos foram validos: "))
eleitores = brancos + nulos + validos
print("O número de eleitores foi de", eleitores)

porcentualbranco = brancos / eleitores * 100
porcentualnulos = nulos / eleitores * 100
porcentualvalidos = validos / eleitores * 100
print("O percentual de voto em brancos é de", round(porcentualbranco),"%")
print("O percentual de voto em nulos é de", round(porcentualnulos),"%")
print("O percentual de voto em validos é de", round(porcentualvalidos),"%")

