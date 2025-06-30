
'''crie uma calculadora que executa calculos simples como soma, subtração, multiplicação e divisão.
A calculadora deve receber dois números e uma operação, e retornar o resultado do cálculo.
nota: utlize funções para cada operação e uma função principal que chama as outras funções.'''

num = []


def soma(num):
    resultado = sum(num)
    return resultado
def subtração(num):
    resultado = num[0] - num[1]
    return resultado
def divisão(num):
    resultado = num[0] / num[1]
    return resultado
def mult(num):
    resultado = num[0] * num[1]
    return resultado

for i in range(2):
    num.append(float(input(f"Número {i}: ")))

operacao = input("TIPO DE CONTA(+, -, /, *): ")

if operacao == "+":
   resultadoop = soma(num)
elif operacao == "-":
    resultadoop = subtração(num)
    
elif operacao == "/":
    resultadoop = divisão(num)
elif operacao == "*":
    resultadoop = mult(num)

print(resultadoop)