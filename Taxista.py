hodometroinc = int(input("Hodometro Inicial: "))
hodometrofim = int(input("Hodometro Final: "))
litrosgastos = int(input("Quantos Litros foram gastos: "))
dinheirododia = float(input("Dinheiro do Dia: "))
combustivel = 4.50
kml = (hodometrofim - hodometroinc) / litrosgastos
print(round(kml), "KM/L")

lucro =  dinheirododia - (litrosgastos * combustivel)
print("O lucro é", lucro)