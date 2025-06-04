compdapista = float(input("Comprimento da Pista em Metros: "))
NumTotalVoltas = float(input("Numero Total de Voltas: "))
NumAbsDesejado = float(input("Número de Abastecimento desejado: "))
ConsumoCombustiveldoCarro = float(input("Consumo de Combustivel do Carro KM/L: "))
compdapistaemkm = compdapista / 1000
minlitrosnecessario = (NumTotalVoltas / NumAbsDesejado) * compdapistaemkm / ConsumoCombustiveldoCarro
print("O número de litros necessário ate o primeiro ponto de abastecimento é de", round(minlitrosnecessario, 2))
