"""Escreva um algoritmo para ler as dimensões de uma cozinha retangular
 (comprimento, largura e altura), calcular e escrever a quantidade de
  caixas de azulejos para se colocar em todas as suas paredes
  (considere que não será descontado a área ocupada por portas e janelas).
  Cada caixa de azulejos possui 2m2. """
"""multiplicar a largura de cada parede pela altura do ambiente,"""
import math
comprimento = float(input("Comprimeto da cozinha: "))
largura = float(input("Largura da cozinha: "))
altura = float(input("Altura da cozinha: "))
m2 = comprimento * largura
caixaazulejo = m2 / 2
arredonadado = math.ceil(caixaazulejo)
print("O número de caixa é", arredonadado)
