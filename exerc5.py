distancia = int(input("Digite a distancia entre sua cidade e local de destino:"))

aviao = (distancia * 10.0)/60
carro = (distancia * 1.6)/60
onibus = (distancia * 1.3)/60

print(f'O tempo de viagem será de:{aviao} minutos de avião {carro:.2f} horas de carro {onibus:.2f} de onibus')