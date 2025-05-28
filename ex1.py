nome = input("Qual seu nome? \n") #variavel de texto é string

idade = 0
idade = int(input("Qual sua idade? \n")) #variavel de numero inteiro é int e real é float
saldoBancario = float(input("Qual é seu saldo bancario? \n"))



# print("Hello World, meu nome é %s e minha idade é %d " % (nome, idade)) #

print("Hello World, meu nome é ", nome, "e minha idade é ", idade)

if(idade > 18):
    print("Você é maior de idade")
else:
    print("Você é menor de idade")

if(saldoBancario < 10000):
    print("Você é pobre")
else:
    print("Você é rico")
