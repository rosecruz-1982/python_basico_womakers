#Conversão de temperatura

def celsius(graus):
    temp_celsius = int(graus - 32)/1.8
    print(f'A temperatura em graus celsius é: {temp_celsius}')

def fahrenheit(graus):
    temp_fahrenheit = int(graus*1.8)+32
    print(f'A temperatura em graus Fahrenheit é: {temp_fahrenheit}')


escolha = int(input("Digite a conversão desejada: (1) - Converter para Graus Celsius  (2) - Converter para Graus Fahrenheit:"))
if escolha == 1:
    graus=int(input(f'Digite a temperatura que deseja converter:'))
    celsius(graus)
else:
    graus=int(input(f'Digite a temperatura que deseja converter:'))
    fahrenheit(graus)