"""Escreva um algoritmo para ler o ano de nascimento de uma pessoa e Escreva uma mensagem
que diga Se ela poderá ou não votar este ano (não é necessário considerar o mês em que ela nasceu)."""

anonasc = int(input("Ano do Seu Nascimento: "))
idade = 0  
idade = 2025 - anonasc
if(idade >= 18):
 print("Você podera votar esse ano")
else: 
 print("Você é de menor, não poderá votar esse ano )=, FAZ O L")
